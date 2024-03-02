# Changelog

## [v0.0.2] - [Mar 2, 2024]

### Added
- Methods to fetch stock information, balance sheets, financials, cashflows, calendar events, income statements, and recommendations.
- Caching using pickle files for data storage, enhancing the efficiency of data retrieval and management.
- `pyrate_limiter` for rate limiting to comply with Yahoo Finance's API rate limits.
- Custom session object `CachedLimiterSession` that combines session caching, rate limiting, and a custom user-agent for optimized data requests.

### Changed
- Shifted data handling to `pandas` DataFrames for enhanced data analysis capabilities.
- Improved overall project folder organization, and cached files are now organized in ticker-specific directories.

## [v0.0.1] - [Feb 26, 2024]

### Added
- Basic caching mechanism to store fetched data locally, reducing redundant requests to Yahoo Finance.
- Functionality to fetch historical and financial data for stocks from Yahoo Finance using `yfinance`.
- Basic logging setup for application monitoring and debugging.
