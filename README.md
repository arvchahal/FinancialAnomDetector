This is a fullstack app that incorporates the Alphavantage API gets the most recent information of a stock including the 
date, open, close, volume.  Then from these values my code calculates features based off of this in the form of RSI,MACD,
EMA, 20 day average, 50 day average, and so on.  These features are then put into an Isolation Forest Machine Learning Algorithm
which finds and detects anomalies in the data.  It then forwards this data to the frontend and graphs these points as red
"splotches".


Please have fun and play around by modifying the features that are used in the model and the contamination rate and what not.

Please email me at arnav.chahal@vanderbilt.edu if there are any errors in the code or problems or suggested features

In the future I am looking to implement a news sentiment analysis section about the dates that are listed as anomalies for more
information about these events.  

At the moment I am using the adjusted data otherwise the anomalies in stock data would be problematic as the unadjusted data does not
account for splits in stocks and dividends and so on.


Thanks and have fun

The website is no longer deployed 


To run this code locally clone the git hub repo and cd into frontend and run npm start
