import logging
import yfinance as yf
import os
import pickle
import time
from datetime import datetime, timedelta

class StockDataFetcher:
    '''
    Attributes:
        cache_dir (str): The directory path where the cached data will be stored.

    Methods:
        __init__(): Initializes the StockDataFetcher object and sets up logging and cache directory.
        _get_cache_file_path(ticker: str, data_type: str) -> str: Returns the file path for the cache file corresponding to the given ticker and data type.
        _is_cache_valid(file_path: str) -> bool: Checks if the cache file at the given path is valid and not expired.
        _load_from_cache(file_path: str): Loads data from the cache file at the given path.
        _save_to_cache(file_path: str, data): Saves data to the cache file at the given path.
        fetch_historical_data(ticker: str, start_date: str, end_date: str): Fetches historical data for the given ticker and date range from Yahoo Finance. Returns the data as a list of dictionaries.
        fetch_financial_data(ticker: str): Fetches financial data for the given ticker from Yahoo Finance. Returns the data as a dictionary containing information, balance sheet, financials, and cashflow.
    '''
        
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.cache_dir = "cache" 
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir) 

    def _get_cache_file_path(self, ticker: str, data_type: str) -> str:
        return os.path.join(self.cache_dir, f"{ticker}_{data_type}.pkl")

    def _is_cache_valid(self, file_path: str) -> bool:
        if not os.path.exists(file_path):
            return False
        last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
        return (datetime.now() - last_modified) < timedelta(days=1)

    def _load_from_cache(self, file_path: str):
        with open(file_path, 'rb') as file:
            return pickle.load(file)

    def _save_to_cache(self, file_path: str, data):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)

    def fetch_historical_data(self, ticker: str, start_date: str, end_date: str) -> dict:
        """
        Returns:
            list: A list of dictionaries representing the historical data. Each dictionary contains the data for a single day.
        """
        cache_file_path = self._get_cache_file_path(ticker, "historical_data")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading historical data for {ticker} from cache")
            return self._load_from_cache(cache_file_path)

        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            logging.warning(f"No historical data found for {ticker}")
            return {}
        data.reset_index(inplace=True)
        data_dict = data.to_dict(orient='records')

        self._save_to_cache(cache_file_path, data_dict)
        return data_dict

    def fetch_financial_data(self, ticker: str) -> dict:
        """
        Returns:
            dict: A dictionary containing the financial data. The dictionary has the following keys:
                - 'info': Information about the stock.
                - 'balance_sheet': Balance sheet data.
                - 'financials': Financial statement data.
                - 'cashflow': Cash flow statement data.

        """
        cache_file_path = self._get_cache_file_path(ticker, "financial_data")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading financial data for {ticker} from cache")
            return self._load_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker)
        data = {
            "info": ticker_obj.info,
            "balance_sheet": ticker_obj.balance_sheet.to_dict(),
            "financials": ticker_obj.financials.to_dict(),
            "cashflow": ticker_obj.cashflow.to_dict()
        }

        self._save_to_cache(cache_file_path, data)
        return data