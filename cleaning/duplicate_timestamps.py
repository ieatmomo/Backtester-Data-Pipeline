'''
Docstring for cleaning.duplicate_timestamps
Module for checking for duplicate timestamps in normalised dataset

'''
import pandas as pd

def duplicate_timestamps_check(df):
    return df.drop_duplicates(subset=["timestamp"], keep="first")