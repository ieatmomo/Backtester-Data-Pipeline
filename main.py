from dotenv import load_dotenv
import os
from fetcher import Fetcher
import argparse
from batching.batching import batches
from normaliser import Normaliser


#IMPLEMENTING CLI
parser = argparse.ArgumentParser()
parser.add_argument("symbol")
parser.add_argument("timeframe")
parser.add_argument("start")
parser.add_argument("end")
parser.add_argument("limit")
parser.add_argument("adjustment")
parser.add_argument("feed")
parser.add_argument("sort")

args = parser.parse_args()

symbol = args.symbol
timeframe = args.timeframe
start = args.start
end = args.end
limit = args.limit
adjustment = args.adjustment
feed = args.feed
sort = args.sort

# LOGIC

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

data_dir = "data/raw"
os.makedirs(data_dir, exist_ok=True)

file_name = f"{symbol}_{start}_{end}.csv"
file_path = os.path.join(data_dir, file_name)
file_exists_raw = os.path.exists(file_path)

if not file_exists_raw:
    fetcher_object = Fetcher(API_KEY, API_SECRET_KEY, symbol, timeframe, start, end, limit, adjustment, feed, sort)
    fetcher_object.fetch()
    print("HAS BEEN CREATED")

#Only happens if file doesnt exist in cleaned and formatted and storage (shouldnt matter tbf, if it exists in storage, should exist everywhere else)
normaliser = Normaliser(symbol, start, end)
for batch in batches(file_path):
    #normalise
    normaliser.normalise(batch) # DONE
    #clean
    
    #format
    #store
    print("hi")

#python main.py "AAPL" "5Min" "2024-01-03T00%3A00%3A00Z" "2024-01-04T00%3A00%3A00Z" "100" "raw" "sip" "asc"
#If file exists in raw/cleaned/formatted/normalised...