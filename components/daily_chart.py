import plotly.express as px
import pandas as pd
from utils.get_open_hours import get_open_hours
import streamlit as st


def daily_chart(
    df: pd.DataFrame,
):
    df = df.copy()



    market_open, market_close = get_open_hours(df)

    df["Datetime"] = pd.to_datetime(df["Datetime"]).dt.tz_localize(None)

    # Create complete trading session (1-minute intervals)
    trading_minutes = pd.DataFrame({
        "Datetime": pd.date_range(
            start=market_open,
            end=market_close,
            freq="1min",
        )
    })



    # Add existing prices, leave future minutes as NaN
    df = trading_minutes.merge(
        df[["Datetime", "Close"]],
        on="Datetime",
        how="left",
    )

    fig = px.line(
        df,
        x="Datetime",
        y="Close",
    )

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Price",
        template="plotly_white",
        xaxis=dict(
            range=[market_open, market_close]
        )
    )

    st.plotly_chart(fig, width="stretch")