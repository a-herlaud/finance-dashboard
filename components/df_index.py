import pandas as pd
from datetime import datetime
from utils.market_metrics import get_period_prices, get_period_returns, cumulative_return, annualized_return

periods = {
    "1M": 21,
    "YTD": (datetime.now().date() - datetime(datetime.now().year,1,1).date()).days,
    "1Y": 252,
    "5Y": 252*5
}

def df_index(df: pd.DataFrame):
    metrics = {}

    for name, days in periods.items():
        prices = get_period_prices(df['Close'], days)
        r = get_period_returns(prices)

        metrics[name] = {       
            "Cumulative return": cumulative_return(r),
            "Open": prices.iloc[0],
            "Close": prices.iloc[-1],
        }

    df_metrics = pd.DataFrame(metrics)
    return df_metrics