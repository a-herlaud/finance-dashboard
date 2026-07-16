import streamlit as st
from components.df_index import df_index, get_period_prices
from components.daily_chart import daily_chart
from components.daily_return import daily_return_card
from components.daily_metrics import daily_metrics
from utils.load_data import load_data


HEIGHT = 500

def full_index(ticker: str, index_name: str):
    df = load_data(ticker, "5y", "1d")
    df_daily = load_data(ticker, "2d", "1m")
    df_metrics = df_index(df)

    head1, head2 = st.columns(2)
    with head1:
        st.header(index_name)

    with head2:
        prices = get_period_prices(df["Close"], 2)
        daily_return_card(prices)

    with st.expander("Details"):
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True, height=HEIGHT):
                daily_metrics(df_daily)

        with col2:
            with st.container(border=True, height=HEIGHT):
                # fig.update_layout(height=HEIGHT)
                daily_chart(df_daily)