import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical data for Apple
ticker = 'MSFT'
data = yf.download(ticker, start='2023-01-01', end='2023-12-31')
data['Daily Return'] = data['Adj Close'].pct_change()

# Calculate mean and standard deviation of daily returns
mean_return = data['Daily Return'].mean()
std_return = data['Daily Return'].std()

# Calculate the 95% prediction interval
confidence_level = 0.95
z_score = 1.96  # for 95% confidence
interval = z_score * std_return

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Adj Close'], label='Adjusted Close Price')
plt.fill_between(data.index, 
                 data['Adj Close'] * (1 - interval), 
                 data['Adj Close'] * (1 + interval), 
                 color='gray', alpha=0.3, label='95% Prediction Interval')

# Customize y-axis interval
plt.yticks(np.arange(min(data['Adj Close']), max(data['Adj Close']), 2))

plt.title(f'{ticker} Stock Price with 95% Prediction Interval')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.show()


