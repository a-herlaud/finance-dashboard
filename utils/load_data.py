import yfinance as yf
import pandas as pd

def load_data(ticker: str):
    df = yf.download(
        ticker,
        period="5y",
        interval="1d",
        auto_adjust=True,
        progress=False,
    )


    # Remove the ticker level
    df.columns = df.columns.get_level_values(0)

    # Make Date a normal column
    df = df.reset_index()
    return df