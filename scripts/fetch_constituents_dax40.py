import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor
import json

import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/DAX"


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

    index = pd.read_html(StringIO(html.text))[4]

    return index


def fetch_market_cap(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info

        # Sometimes fast_info doesn't include marketCap
        market_cap = info.get("marketCap")

        if market_cap is None:
            market_cap = ticker.info.get("marketCap")

        return symbol, market_cap

    except Exception:
        return symbol, None


def index_to_json(index_info, index_name):
    index_info.to_json(
        f"./data/{index_name}_constituents.json",
        orient="records",
        indent=2,
    )


index = parse_wiki_index(url)
print(index.columns)
symbols = index["Ticker"].tolist()

# Parallel download
with ThreadPoolExecutor(max_workers=20) as executor:
    results = dict(executor.map(fetch_market_cap, symbols))

index["marketCap"] = index["Ticker"].map(
    lambda s: results.get(s)
    # lambda s: results.get(s)
)


total = index["marketCap"].dropna().sum()
index["weight"] = index["marketCap"] / total

index = index.rename(
    columns={
        "Ticker": "symbol",
        "Company": "name",
        "Prime Standard Sector": "sector",
    }
)

cols = [
    "symbol",
    "name",
    "sector",
    "marketCap",
    "weight",
]

index = index[cols].sort_values("marketCap", ascending=False)


index_to_json(index, "dax40")

