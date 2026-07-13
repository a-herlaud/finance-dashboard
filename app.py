import streamlit as st
import plotly.express as px
import pandas as pd
import yfinance as yf
from components.sidebar import render_sidebar
from datetime import datetime

HEIGHT = 500

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

def get_period_prices(prices, days):
    return prices.iloc[-days:].dropna()

def get_period_returns(prices):
    return prices.pct_change().dropna()

def simple_return(prices):
    return prices.iloc[-1] / prices.iloc[0] - 1

def cumulative_return(returns):
    return (1 + returns).prod() - 1

def annualized_return(returns):
    total_return = (1 + returns).prod()
    years = len(returns) / 252
    return total_return ** (1 / years) - 1

periods = {
    "1D": 1,
    "1M": 21,
    "YTD": (datetime.now().date() - datetime(datetime.now().year,1,1).date()).days,
    "1Y": 252,
    "5Y": 252*5
}

metrics = {}

for name, days in periods.items():
    prices = get_period_prices(df['Close'], days)
    r = get_period_returns(prices)

    metrics[name] = {
        "Simple return": simple_return(prices),        
        "Cumulative return": cumulative_return(r),
        "Open": prices.iloc[0],
        "Close": prices.iloc[-1],
    }

df_metrics = pd.DataFrame(metrics)




fig = px.line(
    df,
    x="Date",
    y="Close",
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    template="plotly_white",
)

head1, head2 = st.columns(2)
with head1:
    st.header("S&P 500")

with head2:
    price = get_period_prices(df["Close"], 2)
    daily_return = (price.iloc[0] - price.iloc[1]) / price.iloc[0]
    st.metric(
        label="Daily Return",
        value=f"{price.iloc[0]:.6}$",
        delta=f"{daily_return:.2%}",
    )

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True, height=HEIGHT):
        st.dataframe(df_metrics, height=HEIGHT, width='stretch')

with col2:
    with st.container(border=True, height=HEIGHT):
        fig.update_layout(height=HEIGHT)
        st.plotly_chart(fig, width='stretch')