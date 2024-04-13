# Fullstack Stock Anomaly Detection App

## Overview
This fullstack application utilizes the Alphavantage API to fetch the most recent stock information, including date, open, close, and volume. The data is then used to compute various technical indicators such as RSI, MACD, EMA, and moving averages (20-day and 50-day). These features are input into an Isolation Forest Machine Learning Algorithm to detect anomalies, which are then visualized on the frontend as red splotches.

The website is no longer hosted and can only be run locally

## Features
- **Anomaly Detection**: Detects anomalies in stock data using machine learning.
- **Data Visualization**: Displays anomalies on the frontend with distinctive markings.
- **Customization**: Users can modify the model's features and contamination rate to explore different outcomes.

## Future Enhancements
- **News Sentiment Analysis**: Planned implementation to analyze news sentiment on dates identified as anomalies for more contextual information.

## Setup and Running Locally

### Prerequisites
- Node.js
- Python 3
- Flask
- Git

### Clone the Repository
To get started, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```
```bash
cd backend
python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
```bash
pip install -r requirements.txt

```
```bash
export FLASK_APP=<flask_api_filename>.py  # On Windows use `set FLASK_APP=<flask_api_filename>.py`

flask run
```

Run the Frontend
```bash
cd frontend
npm install

```

```bash
npm start

```
The application should now be running locally and accessible via a web browser at http://localhost:3000.

## Note
The application uses adjusted stock data to account for splits, dividends, and other adjustments. The website is currently not deployed and can only be run locally.

---

Make sure to replace `<repository-url>`, `<repository-directory>`, and `<flask_api_filename>` with the actual values relevant to your project. This will make it straightforward for users to follow the setup instructions and get the application running.
