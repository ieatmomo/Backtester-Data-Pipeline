import pandas as pd

def removing_rows_with_missing_values(df):
    df.dropna(inplace=True)