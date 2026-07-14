def get_period_prices(prices, days):
    return prices.iloc[-days:].dropna()

def get_period_returns(prices):
    return prices.pct_change().dropna()

def cumulative_return(returns):
    return (1 + returns).prod() - 1

def annualized_return(returns):
    total_return = (1 + returns).prod()
    years = len(returns) / 252
    return total_return ** (1 / years) - 1

