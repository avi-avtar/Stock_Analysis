import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for Apple
ticker = '^NSEI'
data = yf.download(ticker, start='2023-01-01', end='2024-01-01')
data['Daily Return'] = data['Adj Close'].pct_change()

# Calculate mean and standard deviation of daily returns
mean_return = data['Daily Return'].mean()
std_return = data['Daily Return'].std()

# Calculate the 95% prediction interval
confidence_level = 0.98
z_score = 1.99  # for 95% confidence
interval = z_score * std_return

# Calculate the upper and lower bounds
data['Upper Bound'] = data['Adj Close'] * (1 + interval)
data['Lower Bound'] = data['Adj Close'] * (1 - interval)

# Plot the stock prices and prediction interval
plt.figure(figsize=(14, 7))
plt.plot(data['Adj Close'], label='Adjusted Close Price')
plt.plot(data['Upper Bound'], label='Upper Bound (95% CI)', linestyle='--')
plt.plot(data['Lower Bound'], label='Lower Bound (95% CI)', linestyle='--')
plt.fill_between(data.index, data['Lower Bound'], data['Upper Bound'], color='gray', alpha=0.2)

# Customize y-axis interval
plt.yticks(np.arange(min(data['Adj Close']), max(data['Adj Close']), 100))

plt.title(f'{ticker} Stock Price with 95% Prediction Interval')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()