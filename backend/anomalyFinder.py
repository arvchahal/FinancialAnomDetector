from sklearn.ensemble import IsolationForest
import pandas as pd
import json
# Configure the Isolation Forest model
from sklearn.preprocessing import StandardScaler

def runModel(df):
  scaler = StandardScaler()
  features = ["2. high","3. low","6. volume","50-day AVG","RSI","MACD","Bollinger-Band_width"]
  

# Access the time series data
  df.index = pd.to_datetime(df.index)
  df_scaled = scaler.fit_transform(df[features])

  model = IsolationForest(n_estimators=10000, contamination=0.05, max_samples=.1,random_state=42)
  # contamination parameter is an estimate of the proportion of outliers in the data set

# Fit the model and predict anomalies
  df['anomaly'] = model.fit_predict(df_scaled)

# Mark anomalies with -1 (normal data points are marked with 1)
  df['anomaly'] = df['anomaly'].apply(lambda x: 'anomaly' if x == -1 else 'normal')
# Extract and examine anomalies
  anomalies = df[df['anomaly'] == 'anomaly']
  return anomalies

