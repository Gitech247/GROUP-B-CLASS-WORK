# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Load CSV (or create a dummy DataFrame) ---
# If you have a CSV, uncomment and modify the line below:
# df = pd.read_csv('your_data.csv')

# Creating a dummy DataFrame for demonstration purposes
print("1. Creating a dummy dataset...")
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
data = {
    'Date': dates,
    'Asset_A_Price': np.random.normal(100, 10, 100).cumsum() + 100,
    'Asset_B_Price': np.random.normal(50, 5, 100).cumsum() + 50,
    'Asset_C_Price': np.random.normal(200, 20, 100).cumsum() + 200,
    'Asset_D_Volume': np.random.randint(1000, 10000, 100),
    'Market_Sentiment': np.random.normal(0, 1, 100)
}
df = pd.DataFrame(data)
print("Dummy DataFrame created:")
print(df.head())
print("\n")

# --- 2. Create 'asset objects' (interpreting as structuring and adding features to asset data) ---
# For simplicity, we'll consider each asset as a column in the DataFrame.
# Let's create some derived features for these assets.
print("2. Creating 'asset objects' (derived features)...")
df['Asset_A_Daily_Return'] = df['Asset_A_Price'].pct_change() * 100
df['Asset_B_Daily_Return'] = df['Asset_B_Price'].pct_change() * 100
df['Asset_C_Daily_Return'] = df['Asset_C_Price'].pct_change() * 100

# Adding a simple moving average for one asset as an example
df['Asset_A_SMA_10'] = df['Asset_A_Price'].rolling(window=10).mean()

print("DataFrame with derived features:")
print(df.head())
print("\n")

# --- 3. Perform calculations ---
print("3. Performing calculations...")
# Calculate daily returns statistics
asset_returns_df = df[['Asset_A_Daily_Return', 'Asset_B_Daily_Return', 'Asset_C_Daily_Return']]
print("Daily Returns Statistics:")
print(asset_returns_df.describe())

# Calculate correlations between asset prices
asset_prices_df = df[['Asset_A_Price', 'Asset_B_Price', 'Asset_C_Price']]
print("\nAsset Price Correlations:")
print(asset_prices_df.corr())

# Calculate average daily volume
avg_volume = df['Asset_D_Volume'].mean()
print(f"\nAverage Daily Volume for Asset D: {avg_volume:.2f}")
print("\n")

# --- 4. Produce a 4-panel visualization ---
print("4. Producing a 4-panel visualization...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Asset Analysis Dashboard', fontsize=16)

# Panel 1: Asset A Price Over Time
axes[0, 0].plot(df['Date'], df['Asset_A_Price'], label='Asset A Price')
axes[0, 0].plot(df['Date'], df['Asset_A_SMA_10'], label='Asset A 10-Day SMA', linestyle='--')
axes[0, 0].set_title('Asset A Price with SMA')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Price')
axes[0, 0].legend()
axes[0, 0].grid(True)

# Panel 2: Distribution of Asset B Daily Returns
sns.histplot(df['Asset_B_Daily_Return'].dropna(), kde=True, ax=axes[0, 1], color='skyblue')
axes[0, 1].set_title('Distribution of Asset B Daily Returns')
axes[0, 1].set_xlabel('Daily Return (%)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].grid(True)

# Panel 3: Asset D Volume Over Time
axes[1, 0].fill_between(df['Date'], df['Asset_D_Volume'], color='lightcoral', alpha=0.7)
axes[1, 0].set_title('Asset D Trading Volume')
axes[1, 0].set_xlabel('Date')
axes[1, 0].set_ylabel('Volume')
axes[1, 0].grid(True)

# Panel 4: Scatter plot of Asset A vs Asset C Prices
sns.scatterplot(x=df['Asset_A_Price'], y=df['Asset_C_Price'], hue=df['Market_Sentiment'], size=df['Asset_D_Volume'], sizes=(20, 400), ax=axes[1, 1], palette='viridis')
axes[1, 1].set_title('Asset A vs Asset C Prices (Market Sentiment & Volume)')
axes[1, 1].set_xlabel('Asset A Price')
axes[1, 1].set_ylabel('Asset C Price')
axes[1, 1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust layout to prevent title overlap
plt.show()

print("\nDemonstration complete!")
