from flask import Flask,jsonify,json
import getDataReq
import calculateFeatures
import anomalyFinder
import pandas as pd

app = Flask(__name__)
@app.route('/api/getData/stock-ticker/<symbol>', methods=['GET'])
def getData(symbol):
  data = json.dumps(getDataReq.stockInf(symbol))
  return data



@app.route('/api/trainModel/stock-ticker/<symbol>', methods=['GET'])
def trainModel(symbol):
    data = getDataReq.stockInf(symbol)
    features = calculateFeatures.calcFeatures(symbol, data)
    anomalies = anomalyFinder.runModel(features).copy()
    
    # Ensure the anomalies DataFrame index is in datetime format
    anomalies.index = pd.to_datetime(anomalies.index)
    
    # Convert the index to a string format (YYYY-MM-DD) and then reset the index to turn it into a column
    anomalies.reset_index(inplace=True)
    anomalies['index'] = anomalies['index'].dt.strftime('%Y-%m-%d')
    
    # Optionally, if 'index' is not automatically named to something meaningful, rename it
    anomalies.rename(columns={'index': 'Date'}, inplace=True)
    
    # Convert to JSON; dates are already in string format so no need for date_format
    x= anomalies['Date'].to_json(orient='records')
    return x


if __name__ =="__main__":
  app.run(debug=True)