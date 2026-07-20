import plotly.express as px
import pandas as pd
import streamlit as st

def constituents_chart(data_path: str):
    
    df = pd.read_json(data_path)

    fig = px.treemap(
        df,
        path=["sector", "name"],
        values="weight",
        color="sector",
        hover_data={
            "symbol": True,
            "weight": ":.2%",
        }
    )

    fig.update_traces(textinfo="label+percent parent")
    st.plotly_chart(fig, width='stretch')
