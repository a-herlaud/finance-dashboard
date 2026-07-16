import yfinance as yf
import pandas as pd

def load_data(ticker: str, period: str, interval: str):
    df = yf.download(
        ticker,
        period=period,
        interval=interval,
        auto_adjust=True,
        progress=False,
    )


    # Remove the ticker level
    df.columns = df.columns.get_level_values(0)

    # Make Date a normal column
    df = df.reset_index()
    return df