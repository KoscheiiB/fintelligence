from data_fetcher import StockDataFetcher

def main():
    data_fetcher = StockDataFetcher()
    
    tickers = ["AAPL", "GOOGL", "MSFT"]
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    
    for ticker in tickers:
        historical_data = data_fetcher.fetch_historical_data(ticker, start_date, end_date)
        #print(f"Data for {ticker}: {historical_data[:2]}")
        
        financial_data = data_fetcher.fetch_financial_data(ticker)
        #print(f"Info for {ticker}: {list(financial_data['info'].keys())[:5]}")

if __name__ == "__main__":
    main()