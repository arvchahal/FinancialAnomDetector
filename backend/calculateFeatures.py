import json
# import getDataReq
import pandas as pd
from featureFunctions import FeatureFunctions
# Symbol = getDataReq.symbol
#read the data from the file
def calcFeatures(Symbol,data):
# Load JSON data

# Access the time series data
    time_series = data.get("Time Series (Daily)", {})

# Ensure the DataFrame uses the dates as the index and sorts it
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.index = pd.to_datetime(df.index)

# Convert columns to numeric
    df = df.apply(pd.to_numeric, errors='coerce')

# Check if conversion was successful
    df.sort_index(inplace=True, ascending=True)
# Calculate moving averages
    ff = FeatureFunctions(df['4. close'])
    df['20-day AVG'] = ff.calculateSMA()

    df['50-day AVG'] = ff.calculateSMA(50)
    df['RSI'] = ff.calculate_rsi()
    df['MACD'] = ff.calculateMACD()
    df['50-day EMA'] = ff.calculateEMA(50)

#df["Bollinger-Bands_Upper"],df["Bollinger-Bands_Middle"],df["Bollinger-Bands_Lower"] = ff.calculateBollingerBands()
    df['Bollinger-Band_width'] = ff.calculateBollingerBands()
    df.drop(df.head(50).index,inplace = True)
    df.sort_index(inplace=True, ascending=False)
# Display the first few rows to verify
    return df



