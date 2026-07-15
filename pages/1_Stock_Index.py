import streamlit as st
from components.sidebar import render_sidebar
from components.full_index import full_index

st.set_page_config(page_title="Stock Indexes", layout="wide")

st.title("STOCK INDEXES")

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

render_sidebar()

for name, ticker in indexes.items():
    st.divider()
    full_index(ticker, name)