import pandas as pd
import os
from csv_saver import CSVsaver

'''
1) Convert dict to DF -> Batching already converts into a DF
2) Rename columns
3) Reorder columns (if needed)
4) END
'''

class Normaliser:
    def __init__(self, symbol, start, end):
        self.symbol = symbol
        self.start = start
        self.end = end
    
    def _rename_columns(self, df):
        columns = ["close", "high", "low", "number_of_trades", "open", "timestamp", "volume", "volume_weighted_average_price"]
        df.columns = columns
        
        return df
    
    def _reorder(self, df):
        return df.iloc[:, [5, 4, 1, 2, 0, 6, 7, 3]]

    def normalise(self, batch):
        saver = CSVsaver("normalised", self.symbol, self.start, self.end)
        renamed = self._rename_columns(batch)
        reordered = self._reorder(renamed)

        saver.save_as_csv(reordered)

        return reordered
        

