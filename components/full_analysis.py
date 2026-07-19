import streamlit as st
from components.df_index import df_index, get_period_prices
from components.daily_chart import daily_chart
from components.daily_return import daily_return_card
from components.daily_metrics import daily_metrics
from utils.load_data import load_data
from components.historical_chart import historical_chart


# HEIGHT = 500

def full_analysis(ticker: str):
    df = load_data(ticker, "max", "1d")

    st.header("Historical price")
    historical_chart(df)