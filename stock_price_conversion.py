# -*- coding: utf-8 -*-
"""

2
_
_
.

# Stock Price Conversion Tool

## Description

The **Stock Price Conversion Tool** allows users to retrieve the latest stock price of a given company and convert that price to a specified currency. This feature combines data from the Alpha Vantage API for stock prices and the Exchange Rate API for currency conversion. It provides a convenient way to see how stock prices translate across different currencies.
"""

import requests
import time

# Define Alpha Vantage API key and endpoint
ALPHA_VANTAGE_API_KEY = 'ARIQK315OYB8OG4Z'
stock_symbol = 'AAPL'  # Example: Apple Inc.
alpha_vantage_url = 'https://www.alphavantage.co/query'

# Define parameters for the Alpha Vantage API request
params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': stock_symbol,
    'interval': '1min',
    'apikey': ALPHA_VANTAGE_API_KEY
}

def fetch_stock_data():
    """
    Fetch the latest stock price from Alpha Vantage API.

    Returns:
        float: The latest stock price if successful, None otherwise.
    """
    try:
        stock_response = requests.get(alpha_vantage_url, params=params)
        stock_response.raise_for_status()  # Raise HTTPError for bad responses

        # Check if the API response indicates a rate limit issue
        if 'Note' in stock_response.json():
            print(f"API rate limit exceeded. Waiting to retry...")
            time.sleep(60)  # Wait 60 seconds before retrying
            return fetch_stock_data()  # Retry fetching data

        stock_data = stock_response.json()

        # Extract the latest price
        latest_time = next(iter(stock_data['Time Series (1min)']))
        latest_price = float(stock_data['Time Series (1min)'][latest_time]['1. open'])
        return latest_price

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"KeyError: {e} - Check if the JSON structure has changed")
    except ValueError as e:
        print(f"ValueError: {e} - Check if the price conversion is valid")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

# Define Currency Conversion API key and endpoint
CURRENCY_API_KEY = 'd4c2ace32b7ef05816254950'
currency_url = f'https://v6.exchangerate-api.com/v6/{CURRENCY_API_KEY}/latest/USD'

def fetch_conversion_rate(target_currency):
    """
    Fetch the conversion rate from USD to the target currency from the Exchange Rate API.

    Args:
        target_currency (str): The currency code to convert to.

    Returns:
        float: The conversion rate if successful, None otherwise.
    """
    try:
        currency_response = requests.get(currency_url)
        currency_response.raise_for_status()  # Raise HTTPError for bad responses

        # Check if the API response indicates a rate limit issue
        if 'error-type' in currency_response.json():
            print(f"API rate limit exceeded or other error. Waiting to retry...")
            time.sleep(60)  # Wait 60 seconds before retrying
            return fetch_conversion_rate(target_currency)  # Retry fetching data

        conversion_data = currency_response.json()
        conversion_rates = conversion_data['conversion_rates']

        if target_currency in conversion_rates:
            return conversion_rates[target_currency]
        else:
            print(f"Conversion rate for {target_currency} not found.")
            return None

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"KeyError: {e} - Check if the JSON structure has changed")
    except ValueError as e:
        print(f"ValueError: {e} - Check if the conversion rate is valid")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

latest_price = fetch_stock_data()
if latest_price is not None:
    target_currency = 'INR'
    conversion_rate = fetch_conversion_rate(target_currency)
    if conversion_rate is not None:
        price_in_home_currency = latest_price * conversion_rate
        print(f"Price of {stock_symbol} in {target_currency}: {price_in_home_currency:.2f}")
    else:
        print(f"Unable to fetch conversion rate.")
else:
    print(f"Unable to fetch stock price.")
