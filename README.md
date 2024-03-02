# FinTelligence: Adaptive Investment Toolkit

## Overview

FinTelligence is an adaptive investment toolkit designed to fetch a wide range of data for stocks from Yahoo Finance, enhancing investment decision-making processes with advanced data handling and analysis capabilities.

## Features

- **Enhanced Data Fetcher Module**: The `StockDataFetcher` class now supports fetching a broader spectrum of data including stock information, balance sheets, financials, cash flows, calendar events, income statements, and recommendations. Utilizes pickle files for efficient data storage and caching.
- **Data Analysis Ready**: Shifts data handling to `pandas` DataFrames, facilitating more complex data analysis and manipulation.
- **Optimized Request Handling**: Introduces a customized session object that combines caching, rate limiting, and a custom user-agent for optimized data requests.

## Changelog

For a detailed list of changes, improvements, and additions across different versions of FinTelligence, please see the [CHANGELOG.md](CHANGELOG.md).


## Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/KoscheiiB/fintelligence.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fintelligence
   ```

3. Install the required dependencies specified in the YAML file:

   ```bash
   conda env create -f environment.yaml
   ```

4. Activate the Conda environment:

   ```bash
   conda activate fintelligence_env
   ```

5. Available functions:

```python
from data_fetcher import StockDataFetcher

data_fetcher = StockDataFetcher()

tickers = "AAPL"
start_date = "2023-01-01"
end_date = "2023-12-31"

data_fetcher.fetch_historical_data(ticker, start_date, end_date)
data_fetcher.fetch_info(ticker)
data_fetcher.fetch_balance_sheet(ticker)
data_fetcher.fetch_financials(ticker)
data_fetcher.fetch_cashflow(ticker)
data_fetcher.fetch_calendar(ticker)
data_fetcher.fetch_income_statement(ticker)
data_fetcher.fetch_recommendations(ticker)
data_fetcher.fetch_recommendations_summary(ticker)
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
