# Finance Dashboard

Finance Dashboard is a Streamlit application for exploring major market indexes and chatting with a simple LLM-powered assistant.

The project combines live market data, charting, and lightweight analytics to present a quick overview of several global indexes. It also includes a chatbot page that sends user prompts to the configured Gemini model through LiteLLM.

## What the app does

- Loads historical and intraday data for several major indexes with the `yfinance` Python SDK.
- Displays a per-index market card with a daily return, daily metrics, and an intraday chart.
- Wraps the LLM call in a small service layer so the chatbot stays isolated from the UI code.

## Project structure

```text
finance_dash/
├── app.py
├── pages/
│   ├── 1_Stock_Index.py
│   └── 2_Chatbot.py
├── components/
├── services/
├── utils/
├── requirements.txt
├── Makefile
└── README.md
```

## Pages

### Home page: `app.py`

The home page acts as the project landing page. It explains what the dashboard contains and which pages are available.

It is not a data-heavy view. Instead, it gives the user a fast introduction to the app and points them to the two working pages.

### Stock Index page: `pages/1_Stock_Index.py`

This page is the market dashboard.

It iterates over the supported indexes:
```
- S&P 500 (US)
- NASDAQ 100 (US)
- Dow Jones (US)
- CAC 40 (FR)
- Nikkei 225 (JP)
- KOSPI (KR)
- DAX 40 (DE)
- FTSE 100 (UK)
```

For each index:

- downloads historical and intraday data with `yfinance`,
- computes and renders the daily return card,
- opens an expandable detail section,
- renders daily metrics such as high, low, volume, and volatility,
- and draws a one-minute intraday line chart.

### Chatbot page: `pages/2_Chatbot.py`

This page provides a simple conversational interface.

How it works:

- user messages are stored in Streamlit session state,
- each prompt calls the Gemini model through LiteLLM,
- and the assistant reply is shown back in the chat UI.

The chatbot depends on a `GEMINI_API_KEY` environment variable loaded from `.env`.

## How the Makefile works

The `Makefile` provides a few common commands for local development.

```bash
make install
make up
make dev
make clean
```

- `make install` installs the Python dependencies.
- `make up` starts the app with Streamlit.
- `make dev` starts Streamlit with auto-reload enabled so that changes refresh the app automatically.
- `make clean` removes `__pycache__` folders and compiled Python files.

## Stack and technologies

- Streamlit: app and UI management
- Plotly: chart rendering
- Pandas: data manipulation and analysis
- yfinance: fetching intraday and historical financial data
- LiteLLM: LLM provider abstraction
- uv: dependency and command execution through the Makefile

## Setup and run

1. Install the dependencies.

```bash
make install
```

2. Create a `.env` file with your Gemini key.

```bash
GEMINI_API_KEY=your_api_key_here
```

3. Start the app.

```bash
make up
```

4. Open the Streamlit URL shown in the terminal.

## Notes

- Market data comes from Yahoo Finance through `yfinance`.
- The chatbot only works if the Gemini API key is configured.
- The app layout is designed for wide screens, which gives the charts and cards more room.