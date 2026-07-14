import plotly.express as px
import pandas as pd

def fig_index(df: pd.DataFrame):
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
    return fig