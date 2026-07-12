import streamlit as st
import plotly.express as px
import pandas as pd
import yfinance as yf
from components.sidebar import render_sidebar

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("FINANCE DASHBOARD")

settings = render_sidebar()

df = yf.download(
    "^GSPC",
    period="5y",
    interval="1d",
    auto_adjust=True,
    progress=False,
)

# Remove the ticker level
df.columns = df.columns.get_level_values(0)

# Make Date a normal column
df = df.reset_index()

st.dataframe(df.head())

fig = px.line(
    df,
    x="Date",
    y="Close",
    title="S&P 500 (Last 5 Years)",
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    template="plotly_white",
)

st.plotly_chart(fig, use_container_width=True)