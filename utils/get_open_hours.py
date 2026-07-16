import pandas as pd


def get_open_hours(df: pd.DataFrame):
    df = df.copy()
    # print(df)
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df.set_index("Datetime").sort_index()

    # Trading days
    days = sorted(df.index.normalize().unique())

    if len(days) == 1:
        previous_day = days[-1]
    else:
        previous_day = days[-2]
    current_day = days[-1]

    # Previous full session
    session = df[df.index.normalize() == previous_day]
    previous_open = session.index.min()
    previous_close = session.index.max()

    # Combine previous session hours with current day's date
    market_open = pd.Timestamp.combine(
        current_day.date(),
        previous_open.time(),
    )

    market_close = pd.Timestamp.combine(
        current_day.date(),
        previous_close.time(),
    )

    return market_open, market_close