import streamlit as st
from components.df_index import df_index, get_period_prices
from components.daily_chart import daily_chart
from components.daily_return import daily_return_card
from components.daily_metrics import daily_metrics
from components.constituents_chart import constituents_chart
from utils.load_data import load_data
from components.historical_chart import historical_chart

paths = {
    "^GSPC": "./data/sp500_constituents.json",
    "^NDX": "./data/nasdaq100_constituents.json",
    "^DJI": "./data/dow_constituents.json",
    "^FCHI": "./data/cac40_constituents.json",
    "^N225": "./data/nikkei225_constituents.json",
    "^KS11": "./data/kospi200_constituents.json",
    "^GDAXI": "./data/dax40_constituents.json",
    "^FTSE": "./data/ftse100_constituents.json",
}

def full_analysis(ticker: str):
    df = load_data(ticker, "max", "1d")

    st.header("Historical price")
    historical_chart(df)
    st.divider()

    st.header("Components")
    constituents_chart(paths[ticker])
