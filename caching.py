import csv
import os

class Caching:
    def __init__(self, symbol, start, end):
        self.symbol = symbol
        self.start = start
        self.end = end

    def _cache_data_as_csv(self, data):
        data_dir = "data/raw"
        os.makedirs(data_dir, exist_ok=True)
        
        file_name = f"{self.symbol}_{self.start}_{self.end}.csv"
        file_path = os.path.join(data_dir, file_name)
        file_exists = os.path.exists(file_name)

        with open(file_path, 'a', newline='') as csvfile:
            field_names = ['c', 'h', 'l', 'n', 'o', 't', 'v', 'vw']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            if not file_exists:
                writer.writeheader()

            writer.writerows(data)

    def cache(self, data):
        self._cache_data_as_csv(data)