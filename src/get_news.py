"""getting information using news api"""

import os
from pathlib import Path
from datetime import date, timedelta
import requests
from dotenv import load_dotenv

# setting working directory
WORKING_DIR = Path(__file__).parent.parent
ENV_PATH = WORKING_DIR / ".env"

# getting all the information we need from .env
load_dotenv(ENV_PATH)
API_KEY = os.getenv("API_KEY")

class GetNewsData:
    """this class will be used in main.py for getting all the data"""

    def __init__(self, topic):
        self.today_date = date.today() #date right now
        self.yesterday_date = date.today() - timedelta(days=1) #date yesterday
        self.url = (f"https://newsapi.org/v2/everything?q={topic}&from={self.yesterday_date}"
                    f"&to={self.today_date}&sortBy=popularity&language=en&apiKey={API_KEY}")


    def _get_news_data(self):
        """function for getting the dictionary"""
        response = requests.get(self.url, timeout=10)
        return response.json()


    def valid_data(self):
        """getting all the usefully data"""

        news_list = self._get_news_data() #geting the dictionary from the first function
        news = {} #empty dictionary for the iteration bellow
        for idx, article in enumerate(news_list.get("articles", [])):
            news[f"News{idx + 1}"] = {
                "title": article.get("title", ""),
                "author": article.get("author", ""),
                "description": article.get("description", ""),
                "content": article.get("content", ""),
                "url": article.get("url", "")
            }
        return news


    def number_of_news(self):
        """function for getting the number of articles based on topic"""

        news_list = self._get_news_data() #geting the dictionary from the first function
        nr_news = f"{news_list["totalResults"]}"
        return nr_news
