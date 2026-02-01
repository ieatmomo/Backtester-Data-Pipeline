import pandas as pd
import os

class CSVsaver:
    def __init__(self, folder_name, symbol, start, end):
        self.folder_name = folder_name
        self.symbol = symbol
        self.start = start
        self.end = end

    def save_as_csv(self, data):
        dir = f"data/{self.folder_name}"

        os.makedirs(dir, exist_ok=True)
        
        file_name = f"{self.symbol}_{self.start}_{self.end}.csv"
        file_path = os.path.join(dir, file_name)

        data.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)