import streamlit as st
import pandas as pd
import numpy as np

def daily_metrics(df: pd.DataFrame):
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df.set_index("Datetime").sort_index()
    df = df.loc[df.index.normalize() == df.index.normalize().max()]
    returns = df["Close"].pct_change().dropna()

    metrics = {
        "High Price": df["Close"].max(),
        "Low Price": df["Close"].min(),
        "Volume": df["Volume"].sum(),
        "Annualized Volatility": returns.std() * np.sqrt(252 * 390) * 100,
        "Volatility": returns.std() * 100,
    }

    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="High Price",
            value=f"{metrics['High Price']:,.2f}"
        )

    with col2:
        st.metric(
            label="Low Price",
            value=f"{metrics['Low Price']:,.2f}"
        )

    st.divider()

    # Row 2: Volume alone
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Volume",
            value=f"{metrics['Volume']/1e9:.2f}B"
        )


    st.divider()
    # Row 3: Volatility metrics
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Volatility",
            value=f"{metrics['Volatility']:.2f}%"
        )

    with col2:
        st.metric(
            label="Annualized Volatility",
            value=f"{metrics['Annualized Volatility']:.2f}%"
        )