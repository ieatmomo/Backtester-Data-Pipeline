from dotenv import load_dotenv
import requests
import json


class Fetcher:
    def __init__(self, API_KEY, API_SECRET_KEY):
        self.API_KEY = API_KEY
        self.API_SECRET_KEY = API_SECRET_KEY
        self.symbols = "AAPL"
        self.timeframe = "5Min"
        self.start = "2024-01-03T00%3A00%3A00Z"
        self.end = "2024-01-04T00%3A00%3A00Z"
        self.limit = "100"
        self.adjustment = "raw"
        self.feed = "sip"
        self.sort = "asc"

    
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

    def _check_token_exists(self, response):
        if response['next_page_token'] == None:
            return False 

        else:
            return True

    def fetch(self):
        next_page_flag = False
        response = self._api_call()
        data = self._parse_response(response)
        #TODO: SAVE TO CSV

        token_check = self._check_token_exists(data)
        while token_check:
            page_token = data['next_page_token']
            next_page = self._next_page_api_call(page_token)
            #TODO: SAVE DATA TO CSV





