from dotenv import load_dotenv
import os
from fetcher import Fetcher

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

fetcher_object = Fetcher(API_KEY, API_SECRET_KEY)

fetcher_object.fetch()

