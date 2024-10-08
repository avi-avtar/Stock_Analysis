#Scatter plots visualise the relationship between two variables, such as stock price and trading volume, helping to identify correlations.


import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock data for Apple (AAPL)
stock_data = yf.download('AAPL', start='2020-01-01', end='2024-08-01')

# Scatter plot of Volume vs. Close Price
plt.scatter(stock_data['Volume'], stock_data['Close'], alpha=0.5)
plt.title('Volume vs. Close Price')
plt.xlabel('Volume')
plt.ylabel('Close Price')
plt.grid(True)
plt.show()