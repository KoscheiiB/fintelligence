from datetime import datetime, timedelta
import logging
import yfinance as yf
import os
import pickle
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
import pandas as pd

class CachedLimiterSession(CacheMixin, LimiterMixin, Session): 
    pass
 
session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*3)),  # max 2 requests per 3 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
    expire_after=None,
)

session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
class StockDataFetcher:        
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.cache_dir = "../cache/" 
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir) 
        self.session = session   

    def _get_cache_file_path(self, ticker: str, data_type: str) -> str:
        ticker_cache_dir = os.path.join(self.cache_dir, ticker)
        if not os.path.exists(ticker_cache_dir):
            os.makedirs(ticker_cache_dir)
        return os.path.join(ticker_cache_dir, f"{data_type}.pkl") 

    def _is_cache_valid(self, file_path: str) -> bool:
        if not os.path.exists(file_path):
            return False
        last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
        return (datetime.now() - last_modified) < timedelta(days=1)

    def _save_df_to_cache(self, file_path: str, data: pd.DataFrame):
        data.to_pickle(file_path)

    def _load_df_from_cache(self, file_path: str) -> pd.DataFrame:
        return pd.read_pickle(file_path)
    
    def _save_dict_to_cache(self, file_path: str, data: dict):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)

    def _load_dict_from_cache(self, file_path: str) -> dict:
        with open(file_path, 'rb') as file:
            return pickle.load(file)

    def fetch_historical_data(self, ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        cache_file_path = self._get_cache_file_path(ticker, "historical_data")
        try:
            if self._is_cache_valid(cache_file_path):
                logging.info(f"Loading historical data for {ticker} from cache")
                return self._load_df_from_cache(cache_file_path)

            data = yf.download(ticker, start=start_date, end=end_date, session=self.session)
            if data.empty:
                logging.warning(f"No historical data found for {ticker}")
                return pd.DataFrame()

            self._save_df_to_cache(cache_file_path, data)
            return data
        except Exception as e:
            logging.error(f"Error fetching historical data for {ticker}: {e}")
            return pd.DataFrame()

    def fetch_info(self, ticker: str) -> dict:
        cache_file_path = self._get_cache_file_path(ticker, "info")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading info for {ticker} from cache")
            return self._load_dict_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        info = ticker_obj.info

        self._save_dict_to_cache(cache_file_path, info)
        return info

    def fetch_balance_sheet(self, ticker: str) -> pd.DataFrame:
        cache_file_path = self._get_cache_file_path(ticker, "balance_sheet")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading balance sheet for {ticker} from cache")
            return self._load_df_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        balance_sheet = ticker_obj.balance_sheet

        self._save_df_to_cache(cache_file_path, balance_sheet)
        return balance_sheet
    
    def fetch_financials(self, ticker: str) -> pd.DataFrame:
        cache_file_path = self._get_cache_file_path(ticker, "financials")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading financials for {ticker} from cache")
            return self._load_df_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        financials = ticker_obj.financials

        self._save_df_to_cache(cache_file_path, financials)
        return financials
    
    def fetch_cashflow(self, ticker: str) -> pd.DataFrame:
        cache_file_path = self._get_cache_file_path(ticker, "cashflow")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading cashflow for {ticker} from cache")
            return self._load_df_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        cashflow = ticker_obj.cashflow

        self._save_df_to_cache(cache_file_path, cashflow)
        return cashflow
    
    def fetch_calendar(self, ticker: str) -> dict:
        cache_file_path = self._get_cache_file_path(ticker, "calendar")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading calendar for {ticker} from cache")
            return self._load_dict_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        calendar = ticker_obj.calendar

        self._save_dict_to_cache(cache_file_path, calendar)
        return calendar 
    
    def fetch_income_statement(self, ticker: str) -> pd.DataFrame:
        cache_file_path = self._get_cache_file_path(ticker, "income_statement")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading income statement for {ticker} from cache")
            return self._load_df_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        income_statement = ticker_obj.income_stmt

        self._save_df_to_cache(cache_file_path, income_statement)
        return income_statement
    
    def fetch_recommendations(self, ticker: str) -> pd.DataFrame:
        cache_file_path = self._get_cache_file_path(ticker, "recommendations")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading recommendations for {ticker} from cache")
            return self._load_df_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        recommendations = ticker_obj.recommendations

        self._save_df_to_cache(cache_file_path, recommendations)
        return recommendations
    
    def fetch_recommendations_summary(self, ticker: str) -> pd.DataFrame:
        cache_file_path = self._get_cache_file_path(ticker, "recommendations_summary")
        if self._is_cache_valid(cache_file_path):
            logging.info(f"Loading recommendations summary for {ticker} from cache")
            return self._load_df_from_cache(cache_file_path)

        ticker_obj = yf.Ticker(ticker, session=self.session)
        recommendations_summary = ticker_obj.recommendations_summary

        self._save_df_to_cache(cache_file_path, recommendations_summary)
        return recommendations_summary