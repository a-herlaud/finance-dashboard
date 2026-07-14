import streamlit as st
import pandas as pd
import yfinance as yf
from components.sidebar import render_sidebar
from components.full_index import full_index

indexes = {
    "S&P 500": "^GSPC",
    "NASDAQ 100": "^NDX",
    "Dow Jones": "^DJI",
    "CAC 40": "^FCHI",
    "Nikkei 225": "^N225",
    "KOSPI": "^KS11",
    "DAX 40": "^GDAXI",
    "FTSE 100": "^FTSE",
}

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("FINANCE DASHBOARD")

render_sidebar()

for name, ticker in indexes.items():
    st.divider()
    full_index(ticker, name)