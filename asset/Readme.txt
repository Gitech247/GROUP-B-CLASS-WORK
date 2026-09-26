OARD
========================
PROJECT PURPOSE
---------------
This Python project demonstrates basic asset analysis using a sample
financial dataset. It creates or loads price, trading-volume, and market-
sentiment data; calculates useful features; and produces a visual dashboard.
The analysis includes:
- Daily percentage returns for Assets A, B, and C
- A 10-day simple moving average for Asset A
- Summary statistics for daily returns
- Correlations between asset prices
- Average daily volume for Asset D
- A four-panel visual dashboard
REQUIREMENTS
------------
Install Python 3 and these libraries:
pip install pandas numpy matplotlib seaborn
HOW TO RUN
----------
1. Save the analysis code in a file called asset_analysis.py, or open it in
   Google Colab.
2. If running on your computer, open a terminal in the project folder.
3. Run this command:
python asset_analysis.py
In Google Colab, paste the code into a code cell and run the cell.
USING YOUR OWN CSV DATA
-----------------------
The supplied code creates a dummy dataset for demonstration. To use your own
data, replace the dummy-data section with:
df = pd.read_csv("your_data.csv")
Your CSV should contain these columns:
Date
Asset_A_Price
Asset_B_Price
Asset_C_Price
Asset_D_Volume
Market_Sentiment
OUTPUT
------
The script prints a data preview, daily-return statistics, asset-price
correlations, and the average daily volume for Asset D. It also displays four
charts:
1. Asset A price with its 10-day moving average
2. Distribution of Asset B daily returns
3. Asset D trading volume over time
4. Asset A versus Asset C prices, showing market sentiment and volume
NOTE
----
The sample values are randomly generated for learning and demonstration. They
