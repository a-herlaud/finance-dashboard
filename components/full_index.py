import streamlit as st
from components.df_index import df_index, get_period_prices
from components.fig_index import fig_index
from components.daily_return import daily_return_card
from utils.load_data import load_data


HEIGHT = 500

def full_index(ticker: str, index_name: str):
    df = load_data(ticker)

    df_metrics = df_index(df)

    fig = fig_index(df)

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
                st.dataframe(df_metrics, height=HEIGHT, width='stretch')

        with col2:
            with st.container(border=True, height=HEIGHT):
                fig.update_layout(height=HEIGHT)
                st.plotly_chart(fig, width='stretch')