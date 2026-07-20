import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor
import json

import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"


def parse_wiki_index(url: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
        )
    }

    html = requests.get(url, headers=headers, timeout=30)
    html.raise_for_status()

    index = pd.read_html(StringIO(html.text))[1]

    return index


def fetch_price(symbol: str):
    try:
        ticker = yf.Ticker(symbol)

        hist = ticker.history(period="5d")

        if hist.empty:
            return symbol, None

        close_price = hist["Close"].iloc[-1]

        return symbol, close_price

    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return symbol, None


def index_to_json(index_info, index_name):
    index_info.to_json(
        f"./data/{index_name}_constituents.json",
        orient="records",
        indent=2,
    )


index = parse_wiki_index(url)
symbols = index["Symbol"].str.replace(".", "-", regex=False).tolist()

# Parallel download
with ThreadPoolExecutor(max_workers=20) as executor:
    results = dict(executor.map(fetch_price, symbols))

index["price"] = index["Symbol"].map(
    lambda s: results.get(s.replace(".", "-"))
    # lambda s: results.get(s)
)


total = index["price"].dropna().sum()
index["weight"] = index["price"] / total

index = index.rename(
    columns={
        "Symbol": "symbol",
        "Company": "name",
        "Sector": "sector",
    }
)

cols = [
    "symbol",
    "name",
    "sector",
    "price",
    "weight",
]

index = index[cols].sort_values("price", ascending=False)


index_to_json(index, "dow")

