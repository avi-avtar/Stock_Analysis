import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load stock data (for example, from a CSV file)
# data = pd.read_csv('apple_stock_data.csv')
# For demonstration, let's create some synthetic data
np.random.seed(42)
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Close': np.random.normal(loc=150, scale=5, size=100)  # Synthetic closing prices
})

# Calculate daily returns
data['Return'] = data['Close'].pct_change()

# Calculate mean and standard deviation of daily returns
mean_return = data['Return'].mean()
std_dev = data['Return'].std()

# Define the range for the probability calculation
lower_bound = mean_return - 2 * std_dev
upper_bound = mean_return + 2 * std_dev

# Calculate the probability of staying within the range
probability = norm.cdf(upper_bound, mean_return, std_dev) - norm.cdf(lower_bound, mean_return, std_dev)

# Plotting the probability distribution
x = np.linspace(mean_return - 3*std_dev, mean_return + 3*std_dev, 100)
y = norm.pdf(x, mean_return, std_dev)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Probability Density Function')
plt.axvline(lower_bound, color='r', linestyle='--', label='Lower Bound')
plt.axvline(upper_bound, color='g', linestyle='--', label='Upper Bound')
plt.title('Probability Distribution of Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Probability Density')
plt.yticks(np.arange(0, max(y), 2))  # Change y-axis interval from 10 to 2
plt.legend()
plt.show()

print(f"Probability of staying within the range: {probability * 100:.2f}%")
