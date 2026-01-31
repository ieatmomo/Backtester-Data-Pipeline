import pandas as pd

def sort_df_by_timestamp(df):
    return df.sort_values(by='timestamp')