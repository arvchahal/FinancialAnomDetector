import React, { useState } from 'react';
import './App.css';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Line } from "react-chartjs-2";

// Register the chart components you wish to use
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [chartData, setChartData] = useState(null);
  const [chartKey, setChartKey] = useState(0);
  const [symbol, setSymbol] = useState('');
  const [showAnomaliesButton, setShowAnomaliesButton] = useState(false); // State to manage button visibility
  let submit1 = false;
  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Validate the symbol length
    if (symbol.length > 5 || symbol.length < 1) {
      alert("Invalid Symbol. Please input a valid Stock Symbol/Ticker.");
      return;
    }
    // Fetch data based on the symbol
    fetch(`${process.env.REACT_APP_API_URL}/api/getData/stock-ticker/${symbol.toUpperCase()}`)
      .then(res => res.json())
      .then(data => {
        if (!data) {
          alert("Data for the provided symbol is not available.");
          return;
        }

        const timeSeries = data["Time Series (Daily)"];
        if (!timeSeries) {
          alert("No time Series Data available");
          return;
        }

        const processedData = (() => {
          const labels = Object.keys(timeSeries).sort(); // Sort dates
          const closingPrices = labels.map(date => parseFloat(timeSeries[date]["5. adjusted close"]));
          return {
            labels,
            datasets: [
              {
                label: `${symbol.toUpperCase()} Adjusted Closing Prices`,
                data: closingPrices,
                borderColor: 'rgb(75, 192, 192)',
                backgroundColor: 'rgba(75, 192, 192, 0.5)',
              }
            ]
          };
        })();
        setChartData(processedData); // Set the processed data for the chart
        setShowAnomaliesButton(true); // Show the "Find Anomalies" button
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        alert("Failed to fetch data. Please try again.");
      });
      submit1=true;
  };

  const handleFindAnomalies = () => {
    fetch(`${process.env.REACT_APP_API_URL}/api/trainModel/stock-ticker/${symbol.toUpperCase()}`)
        .then(res => res.json())
        .then(anomalyData => {
            const anomalyDates = anomalyData; // Adjust based on actual API response

            const updatedChartData = {...chartData};
            updatedChartData.datasets = updatedChartData.datasets.map(dataset => ({
                ...dataset,
                borderColor: 'rgb(75, 192, 192)', // Default line color
                backgroundColor: 'rgba(75, 192, 192, 0.5)', // Default fill color
                pointBackgroundColor: dataset.data.map((_, index) => {
                    const label = updatedChartData.labels[index];
                    return anomalyDates.includes(label) ? 'red' : 'rgba(75, 192, 192, 0.5)';
                }),
                pointRadius: dataset.data.map((_, index) => {
                    const label = updatedChartData.labels[index];
                    return anomalyDates.includes(label) ? 7 : 3; // Larger radius for anomalies
                }),
                pointBorderColor: dataset.data.map((_, index) => {
                    const label = updatedChartData.labels[index];
                    return anomalyDates.includes(label) ? 'red' : 'rgb(75, 192, 192)';
                }),
                pointBorderWidth: dataset.data.map((_, index) => {
                    const label = updatedChartData.labels[index];
                    return anomalyDates.includes(label) ? 3 : 1; // Thicker border for anomalies
                })
            }));

            setChartData(updatedChartData);
        })
        .catch(error => console.error('Error fetching anomalies:', error));
      setChartKey(prevKey => prevKey + 1);

  };
  

  

  // Chart options
  const options = {
    scales: {
      y: {
        beginAtZero: false,
      }
    },
    responsive: true,
    plugins: {
      legend: {
        display: true,
        position: 'top',
      },
      title: {
        display: true,
        text: `Closing Prices for ${symbol.toUpperCase()}`,
      },
    },
  };

  return (
    <div className="App">
      <header className="stkTkr">
        <p>Please input a stock ticker to detect historical anomalies</p>
        <form onSubmit={handleSubmit}>
          <div className="userInput">
            <h3 className="symbText">Symbol/Ticker:</h3>
            <input
              type="text"
              value={symbol}
              onChange={e => setSymbol(e.target.value)}
              placeholder="Enter Symbol (e.g., TSLA)"
            />
          </div>
          <button type="submit" className="submitButton">Submit</button>
        </form>
      </header>
      {/* Render the line chart only if data is available */}
      {chartData && <Line data={chartData} options={options} />}
      {showAnomaliesButton && <button onClick={handleFindAnomalies} className="findAnomaliesButton">Find Anomalies</button>}
    </div>
  );
}

export default App;
