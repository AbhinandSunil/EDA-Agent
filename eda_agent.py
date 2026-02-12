import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
import os
from openai import OpenAI
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ========== CONFIG ==========
DATA_PATH = "all_stocks_5yr.csv"

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Dummy key
)

# ========== LOAD DATA ==========
df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

missing_report = df.isnull().sum()
summary_stats = df.describe().to_string()

# ========== EDA REPORT ==========
profile = ProfileReport(df, title="Trading Data EDA Report")
profile.to_file("eda_report.html")

# ========== PLOT ==========
os.makedirs("plots", exist_ok=True)
num_cols = df.select_dtypes(include="number").columns

if len(num_cols) > 0:
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df[num_cols[0]])
    plt.title(f"Trend: {num_cols[0]}")
    plt.savefig("plots/trend.png")
    plt.close()

    # Moving Average Signals
    df["ma_fast"] = df[num_cols[0]].rolling(5).mean()
    df["ma_slow"] = df[num_cols[0]].rolling(20).mean()
    df["signal"] = (df["ma_fast"] > df["ma_slow"]).astype(int).diff()
    df.to_csv("signals.csv")

# ========== PROMPTS ==========
exec_prompt = f"""
Explain this dataset to a non-technical business person in simple language.
Summary:
{summary_stats}
Missing values:
{missing_report}
Keep it short.
"""

tech_prompt = f"""
You are a quantitative trading analyst.
Summary stats:
{summary_stats}
Missing values:
{missing_report}
Give patterns, insights, and risks.
"""

action_prompt = f"""
Based on this dataset, give 3 actionable business or trading recommendations in bullet points.
"""

def ask_llm(prompt):
    return client.chat.completions.create(
        model="llama3.2:3b",  # CHANGE TO YOUR MODEL NAME
        messages=[{"role":"user","content":prompt}],
        temperature=0.2
    ).choices[0].message.content

executive_summary = ask_llm(exec_prompt)
technical_summary = ask_llm(tech_prompt)
actionable_insights = ask_llm(action_prompt)

# ========== SAVE TEXT REPORT ==========
with open("report.txt", "w") as f:
    f.write("EXECUTIVE SUMMARY\n" + "="*50 + "\n" + executive_summary + "\n\n")
    f.write("ACTIONABLE INSIGHTS\n" + "="*50 + "\n" + actionable_insights + "\n\n")
    f.write("TECHNICAL ANALYST REPORT\n" + "="*50 + "\n" + technical_summary)

# ========== PDF EXPORT ==========
styles = getSampleStyleSheet()
doc = SimpleDocTemplate("eda_report.pdf", pagesize=letter)
story = []

def add_section(title, text):
    story.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
    story.append(Spacer(1, 12))
    for line in text.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))
    story.append(Spacer(1, 12))

add_section("Executive Summary", executive_summary)
add_section("Actionable Insights", actionable_insights)
add_section("Technical Analyst Report", technical_summary)

doc.build(story)

print("✅ FULL AI REPORT GENERATED (TXT + PDF + HTML)")
