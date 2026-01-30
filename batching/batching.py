import pandas as pd

def batches(file_path):
    chunk_size = 25
    
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        yield chunk