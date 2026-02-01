import pandas as pd
import os
from cleaning.types import type_coersion
from cleaning.missing_values import removing_rows_with_missing_values
from cleaning.timestamp_enforcement import sort_df_by_timestamp
from cleaning.duplicate_timestamps import duplicate_timestamps_check
from csv_saver import CSVsaver

'''
Order of cleaning:
1) Type enforcement
2) removing rows with Missing values
3) Sorting by timestamp
4) Removing duplicate timestamps
'''


def cleaning(df, folder_name, symbol, start, end):

    type_checked = type_coersion(df)
    missing_values_removed = removing_rows_with_missing_values(type_checked)
    sorted_by_timestamp = sort_df_by_timestamp(missing_values_removed)
    removing_duplicates = duplicate_timestamps_check(sorted_by_timestamp)
    saver = CSVsaver(folder_name, symbol, start, end)
    saver.save_as_csv(removing_duplicates)

    return removing_duplicates


