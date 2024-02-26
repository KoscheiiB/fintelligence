# FinTelligence: Adaptive Investment Toolkit

## Overview

FinTelligence is an adaptive investment toolkit designed to fetch historical and financial data for stocks from Yahoo Finance. This toolkit facilitates data retrieval and analysis to support investment decision-making processes.

## Features

- **Data Fetcher Module**: Includes a `StockDataFetcher` class responsible for fetching historical and financial data for stocks.
- **Caching Mechanism**: Utilizes caching to store fetched data locally, improving performance and reducing redundant requests to Yahoo Finance.

## Installation

1. Clone the repository:

   ```bash
   git clone git clone https://github.com/KoscheiiB/fintelligence.git

   ```

2. Navigate to the project directory:

   ```bash
   cd FinTelligence
   ```

3. Install the required dependencies specified in the YAML file:

   ```bash
   conda env create -f environment.yaml
   ```

## Usage

1. Activate the Conda environment:

   ```bash
   conda activate fintelligence_env
   ```

2. Import the `StockDataFetcher` class from the `data_fetcher` module:

   ```python
   from data_fetcher import StockDataFetcher
   ```

3. Create an instance of the `StockDataFetcher` class:

   ```python
   data_fetcher = StockDataFetcher()
   ```

4. Fetch historical data for a stock:

   ```python
   historical_data = data_fetcher.fetch_historical_data(ticker, start_date, end_date)
   ```

5. Fetch financial data for a stock:

   ```python
   financial_data = data_fetcher.fetch_financial_data(ticker)
   ```

## Example

```python
from data_fetcher import StockDataFetcher

data_fetcher = StockDataFetcher()

tickers = ["AAPL", "GOOGL", "MSFT"]
start_date = "2023-01-01"
end_date = "2023-12-31"

for ticker in tickers:
    # Fetch historical data
    print(f"Fetching historical data for {ticker}...")
    historical_data = data_fetcher.fetch_historical_data(ticker, start_date, end_date)
    print(f"Historical data for {ticker}:\n{historical_data[:5]}...\n")

    # Fetch financial data
    print(f"Fetching financial data for {ticker}...")
    financial_data = data_fetcher.fetch_financial_data(ticker)
    print(f"Financial data for {ticker}:\n{financial_data}\n")
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
