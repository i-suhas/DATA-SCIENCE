import requests
from datetime import datetime
import matplotlib.pyplot as plt

# Make a request to the CoinGecko API for Bitcoin prediction prices
response = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Retrieve the prediction prices from the response JSON
    data = response.json()
    prediction_prices = data['prices']

    # Separate the timestamps and prices into separate lists
    timestamps = [price[0] for price in prediction_prices]
    prices = [price[1] for price in prediction_prices]

    # Convert timestamps to dates
    dates = [datetime.fromtimestamp(timestamp / 1000).date() for timestamp in timestamps]

    # Plot the data in a bar graph
    plt.bar(dates, prices)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Bitcoin Prediction Prices')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print('Error occurred while retrieving data from the API.')
