#Box plots summarise the distribution of stock returns, showing median, quartiles, and outliers. They are useful for understanding volatility and return distribution
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# Download historical stock data for Apple (AAPL)
stock_data = yf.download('AAPL', start='2020-01-01', end='2024-08-01')

# Calculate daily returns
stock_data['Return'] = stock_data['Close'].pct_change()

# Drop NaN values resulting from the percentage change calculation
stock_data = stock_data.dropna()

# Plotting the box plot of stock returns
plt.figure(figsize=(8, 6))
sns.boxplot(x=stock_data['Return'])
plt.title('Box Plot of Stock Returns')
plt.xlabel('Return')
plt.show()