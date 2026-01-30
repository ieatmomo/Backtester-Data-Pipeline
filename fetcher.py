from dotenv import load_dotenv
import requests
import json
from caching import Caching


class Fetcher:
    def __init__(self, API_KEY, API_SECRET_KEY, symbols, timeframe, start, end, limit, adjustment, feed, sort):
        self.API_KEY = API_KEY
        self.API_SECRET_KEY = API_SECRET_KEY
        self.symbols = symbols
        self.timeframe = timeframe
        self.start = start
        self.end = end
        self.limit = limit
        self.adjustment = adjustment
        self.feed = feed
        self.sort = sort

    def _api_call(self):
        
        url = f"https://data.alpaca.markets/v2/stocks/bars?symbols={self.symbols}&timeframe={self.timeframe}&start={self.start}&end={self.end}&limit={self.limit}&adjustment={self.adjustment}&feed={self.feed}&sort={self.sort}"

        headers = {"accept": "application/json",
           "APCA-API-KEY-ID": self.API_KEY,
           "APCA-API-SECRET-KEY": self.API_SECRET_KEY
        }   

        response = requests.get(url, headers=headers)

        return response
    
    def _next_page_api_call(self, page_token):
        url = f"https://data.alpaca.markets/v2/stocks/bars?symbols={self.symbols}&timeframe={self.timeframe}&start={self.start}&end={self.end}&limit={self.limit}&adjustment={self.adjustment}&feed={self.feed}&page_token={page_token}&sort={self.sort}"

        headers = {"accept": "application/json",
           "APCA-API-KEY-ID": self.API_KEY,
           "APCA-API-SECRET-KEY": self.API_SECRET_KEY
        }   

        response = requests.get(url, headers=headers)

        return response
    
    def _parse_response(self, response):
        response = response.json()
        return response

    def fetch(self):
        response = self._api_call()
        data = self._parse_response(response)
        
        cacher = Caching(self.symbols, self.start, self.end)

        while True:
            bars = data["bars"][self.symbols]
            cacher.cache(bars)

            if data["next_page_token"] is None:
                break

            page_token = data['next_page_token']
            response = self._next_page_api_call(page_token)
            data = self._parse_response(response)

        return "Done"





