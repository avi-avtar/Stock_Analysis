# Heatmaps display data intensity through colour variations, useful for visualising correlations between different stocks or metrics.
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# Download historical stock data for Apple (AAPL)
stock_data = yf.download('AAPL', start='2020-01-01', end='2024-08-01')

# Calculate the correlation matrix
correlation_matrix = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()