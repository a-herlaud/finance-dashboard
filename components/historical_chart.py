import plotly.express as px
import pandas as pd
import streamlit as st

def historical_chart(df: pd.DataFrame):
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
    
    st.plotly_chart(fig, width='stretch')