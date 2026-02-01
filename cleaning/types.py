import pandas as pd


def type_coersion(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")

    PRICE_COLS = ["open", "high", "low", "close", "volume_weighted_average_price"]
    COUNT_COLS = ["volume", "number_of_trades"]

    for col in PRICE_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in COUNT_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce", downcast="integer")

    return df
