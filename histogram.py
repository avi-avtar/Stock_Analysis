# Histograms show the distribution of stock returns or other numerical data. They help understand the frequency distribution of returns.

import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock data for Apple (AAPL)
stock_data = yf.download('AAPL', start='2020-01-01', end='2024-08-01')

# Calculate daily returns
stock_data['Return'] = stock_data['Close'].pct_change()

# Drop NaN values that result from the percentage change calculation
stock_data = stock_data.dropna()

# Plotting the histogram of stock returns
plt.hist(stock_data['Return'], bins=30, edgecolor='black')
plt.title('Histogram of AAPL Stock Returns')
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.show()