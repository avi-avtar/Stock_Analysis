import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for Apple
data = yf.download('AAPL', start='2023-01-01', end='2024-01-01')
data['Daily Change'] = data['Close'].pct_change()

# Calculate mean and standard deviation of daily changes
mean_change = data['Daily Change'].mean()
std_dev_change = data['Daily Change'].std()

# Calculate the 95% prediction interval
lower_bound = mean_change - 1.99 * std_dev_change
upper_bound = mean_change + 1.99 * std_dev_change

print(lower_bound,upper_bound)

# Plot the stock prices and prediction interval
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='AAPL Stock Price')
plt.axhline(y=data['Close'].iloc[-1] * (1 + lower_bound), color='r', linestyle='--', label='Lower Bound (95% Interval)')
plt.axhline(y=data['Close'].iloc[-1] * (1 + upper_bound), color='g', linestyle='--', label='Upper Bound (95% Interval)')
plt.title('AAPL Stock Price with 95% Prediction Interval')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
