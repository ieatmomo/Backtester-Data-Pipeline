import pandas as pd
import os

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

    def _save_as_csv(self, df):
        normalised_dir = "data/normalised"
        os.makedirs(normalised_dir, exist_ok=True)
        
        file_name = f"{self.symbol}_{self.start}_{self.end}.csv"
        file_path = os.path.join(normalised_dir, file_name)
        
        # Use pandas to_csv with append mode
        df.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)

    def normalise(self, batch):
        renamed = self._rename_columns(batch)
        reordered = self._reorder(renamed)

        self._save_as_csv(reordered)
        

