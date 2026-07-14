import streamlit as st
import pandas as pd

def daily_return_card(prices: pd.DataFrame):
        daily_return = (prices.iloc[1] - prices.iloc[0]) / prices.iloc[1]
        st.metric(
            label="Daily Return",
            value=f"{prices.iloc[0]:.6}$",
            delta=f"{daily_return:.2%}",
        )