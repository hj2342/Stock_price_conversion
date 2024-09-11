# Stock Price Conversion Tool

## Description

The **Stock Price Conversion Tool** allows users to retrieve the latest stock price of a given company and convert that price to a specified currency. This feature combines data from the Alpha Vantage API for stock prices and the Exchange Rate API for currency conversion. It provides a convenient way to see how stock prices translate across different currencies.

## APIs Used

### 1. Alpha Vantage API
- **Purpose**: Provides real-time stock price data.
- **Endpoint**: `https://www.alphavantage.co/query`
- **Function**: `TIME_SERIES_INTRADAY`
- **Reason for Choosing**: Alpha Vantage offers comprehensive stock data with an easy-to-use API for retrieving real-time intraday stock prices.

### 2. Exchange Rate API
- **Purpose**: Provides current exchange rates between different currencies.
- **Endpoint**: `https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD`
- **Reason for Choosing**: The Exchange Rate API offers reliable currency conversion rates with a straightforward API for retrieving rates against USD.

## Instructions

1. **Set Up Your Environment**
   - Install the necessary Python libraries if not already installed:
     ```bash
     pip install requests
     ```

2. **API Keys**
   - Obtain an API key for Alpha Vantage and Exchange Rate API.
   - Replace the placeholders in the code with your actual API keys.

3. **Running the Code**
   - Save the provided Python script to a file, for example, `stock_price_conversion.py`.
   - Run the script using Python:
     ```bash
     python stock_price_conversion.py
     ```

4. **Code Configuration**
   - Set the `stock_symbol` variable to the desired stock symbol (e.g., 'AAPL' for Apple Inc.).
   - Set the `target_currency` variable to the currency code you want to convert to (e.g., 'INR' for Indian Rupee).

## Prerequisites

- **Python 3.x**: Make sure Python 3 is installed on your system.
- **API Keys**: You will need API keys for both Alpha Vantage and Exchange Rate API. Insert these keys into the script where indicated.

## Example Output

- **Price of AAPL in INR: 18455.72**
## Error Handling

The script includes error handling for:
- Network issues and invalid API responses.
- Missing or incorrect keys in the JSON responses.
- API rate limits, with automatic retries after a delay.

  
## Contact

For questions or suggestions, please contact hj2342@nyu.edu
