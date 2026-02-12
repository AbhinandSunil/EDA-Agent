# LLM-Powered Trading Data EDA & Research Agent
This project implements an AI-driven exploratory data analysis and quantitative research agent that automates data profiling, visualization, trading signal generation, and report writing.

The system combines traditional data science pipelines with LLM-powered reasoning to produce both executive-friendly summaries and technical quantitative analysis, mimicking workflows used in trading desks and data science teams.

## Key Features
### Automated Data Preparation

- Cleans and normalizes structured datasets
- Detects missing values, duplicates, and statistical summaries
- Generates a full automated EDA profiling report

### Time-Series Visualization

- Automatically detects numeric time-series columns
- Generates and saves trend plots

### Quantitative Trading Signal Generation

- Implements moving average crossover strategy
- Produces BUY/SELL trading signals for research prototyping

### Multi-Level AI Reporting

- Executive Summary (non-technical, business-readable)
- Technical Quantitative Analysis
- Actionable Trading / Business Recommendations

### Professional Report Export

- Generates structured TXT and PDF reports
- Includes automated AI-generated insights

### Professional Trading Dashboard (Streamlit + Plotly)

- Interactive candlestick charts
- Moving average overlays (fast & slow MA)
- Volume and volatility analysis
- Dynamic KPI cards (price, volume, highs, trend signal)
- Date range and asset filtering

## System Architecture

**1. Data Ingestion & Cleaning Layer** <br>
&nbsp;&nbsp;&nbsp;Preprocesses structured datasets for analysis.

**2. EDA & Visualization Layer** <br>
&nbsp;&nbsp;&nbsp;Computes statistics and generates visualizations.

**3. Signal Generation Layer** <br>
&nbsp;&nbsp;&nbsp;Produces baseline quantitative trading signals.

**4. LLM Research Agent** <br>
&nbsp;&nbsp;&nbsp;Generates executive summaries, technical reports, dashboard, and actionable insights.

**5. Reporting Layer** <br>
&nbsp;&nbsp;&nbsp;Exports results to HTML, TXT, and PDF formats.

**6. Interactive UI Layer** <br>
&nbsp;&nbsp;&nbsp;Streamlit-based interface for non-technical users.



## Tech Stack

- Python
- Pandas, NumPy – Data processing
- Plotly – Financial visualization (candlestick, volume)
- Streamlit – Interactive dashboard UI
- Ollama (Llama 3.2) – Local LLM inference
- ydata-profiling – Automated EDA reports


## Project Structure

```
trading-eda-agent/
│
├── app.py # Streamlit dashboard (main UI)
├── eda_agent.py # Automated EDA + AI summarization pipeline
├── requirements.txt # Python dependencies
├── all_stocks_5yr.csv # Sample trading dataset (or user dataset)
│
├── outputs/
│ ├── eda_report.html # Auto-generated EDA report
│ ├── eda_report.pdf # PDF summary report
│ ├── report.txt # AI analyst textual summary
│ └── signals.csv # Generated trading signals
│
├── plots/ # Generated charts
└── README.md
```

## How to Run

### 1. Install Dependencies 
- pip install -r requirements.txt
  
### 2. Start Ollama (Local LLM)
- ollama serve
- ollama pull llama3.2
  
### 3. Run Automated EDA Agent
- python eda_agent.py

**Generates:**
- eda_report.html
- report.txt
- signals.csv

### 4. Launch Dashboard
- streamlit run app.py
**Open browser at:** <br>
&nbsp;http://localhost:8501


## Dashboard Capabilities

- Interactive candlestick trading chart
- Moving average crossover trend signal
- Volatility and returns metrics
- AI-generated trading commentary
- Natural language Q&A with dataset


## Example AI Analyst Output

- **Trend Summary:** Market shows bullish momentum with increasing moving average crossover.
- **Key Risks:** Elevated volatility and declining volume indicate potential trend reversal risk.
- **Actionable Insight:** Monitor MA crossover and volume confirmation before entering long positions.


## Output

<img width="1893" height="1006" alt="image" src="https://github.com/user-attachments/assets/d43dc2dc-c4f4-4bf3-b449-4c8c16178f3b" />


## Why This Project Matters

This project demonstrates: <br>
- Building AI-powered data products
- Integrating LLMs into analytics workflows
- Financial time-series visualization
- End-to-end ML system engineering
- Product-style dashboard development <br>
It is designed to mirror real quant research tools and fintech analytics platforms.


## Future Improvements

- Backtesting engine with equity curve & Sharpe ratio
- Multi-asset portfolio analytics
- Real-time market data ingestion
- ChatGPT-style conversational dataset interface
- Cloud deployment (HuggingFace / AWS / Render)
