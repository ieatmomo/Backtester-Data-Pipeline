import csv
import os

class Caching:
    def __init__(self, symbol, start, end):
        self.symbol = symbol
        self.start = start
        self.end = end

    def _cache_data_as_csv(self, data):
        
        file_name = f"{self.symbol}_{self.start}_{self.end}.csv"
        file_exists = os.path.exists(file_name)
        with open(file_name, 'a', newline='') as csvfile:
            field_names = ['c', 'h', 'l', 'n', 'o', 't', 'v', 'vw']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            if not file_exists:
                writer.writeheader()

            writer.writerows(data)

    def cache(self, data):
        self._cache_data_as_csv(data)