📈 Stock Forecasting Project

Overview:
This project focuses on forecasting stock prices using historical data from Apple Inc. (AAPL). The goal is to predict future stock movements and visualize trends using ARIMA, Prophet, and Moving Averages. An interactive Streamlit dashboard allows users to explore historical and predicted stock prices.

Key objectives:

Perform exploratory data analysis (EDA) to understand stock trends and volatility.

Implement ARIMA and Prophet models for forecasting.

Compare forecasts and visualize results interactively with Plotly.

Build a Streamlit app for real-time stock visualization.

Tech Stack:

Python

Pandas & NumPy (Data Manipulation)

Matplotlib & Seaborn (Static Visualizations)

Plotly (Interactive Visualizations)

Statsmodels (ARIMA Modeling)

Prophet (Time Series Forecasting)

Streamlit (Interactive Dashboard)

Jupyter Notebook (Analysis & EDA)

Folder Structure:
```
stock-forecasting/
├─ data/ # Raw and processed datasets
│ ├─ AAPL_raw.csv
│ ├─ AAPL_cleaned.csv
│ ├─ AAPL_arima_forecasts.csv
│ └─ AAPL_prophet_forecasting.csv
├─ images/ # Saved plots
├─ notebooks/ # Jupyter notebooks
│ ├─ 01_data_collection.ipynb
│ ├─ 02_cleaning_feature_engineering.ipynb
│ ├─ 03_eda_visualization.ipynb
│ └─ 04_forecasting_models.ipynb
├─ src/ # Python scripts (optional)
├─ streamlit_app.py # Streamlit interactive app
├─ requirements.txt # Dependencies
└─ README.md
```

Project Workflow:

Data Collection

Fetch historical stock data using yfinance.

Store raw data in data/AAPL_raw.csv.

Data Cleaning & Feature Engineering

Handle missing values and duplicate entries.

Compute features like Moving Averages (7-day, 30-day) and Volatility.

Save cleaned data to data/AAPL_cleaned.csv.

Exploratory Data Analysis (EDA)

Plot historical closing prices, moving averages, and volatility.

Generate interactive visualizations with Plotly.

Forecasting

ARIMA Model: Forecast next 30 days of stock prices.

Prophet Model: Forecast 1-year future prices with trend and seasonality.

Compare ARIMA vs Prophet forecasts.

Save forecasted datasets: AAPL_arima_forecasts.csv and AAPL_prophet_forecasting.csv.

Streamlit Dashboard

Interactive plots for historical data, forecasts, and moving averages.

Users can select date ranges and visualize predictions dynamically.

Key Insights:

Moving averages highlight short-term and long-term trends.

ARIMA provides short-term forecast; Prophet captures yearly seasonality.

Visualizations reveal periods of high volatility and consistent trends.

Streamlit app enables easy exploration and interactive analysis.

Visualizations:

Stock Closing Price: images/closing_price.png

Moving Averages: images/moving_averages.png

Volatility: images/volatility.png

ARIMA vs Prophet Forecast: images/arima_prophet_forecast.png

Run Project Locally:

Clone the repository:
git clone https://github.com/yourusername/stock-forecasting.git
cd stock-forecasting

Create virtual environment:
python -m venv .venv
Activate it:

Windows: .venv\Scripts\activate

Mac/Linux: source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run Jupyter Notebooks (optional):
jupyter notebook

Run Streamlit App:
streamlit run streamlit_app.py

Future Improvements:

Add other stocks and multi-stock comparison.

Deploy Streamlit app online (Heroku or Streamlit Cloud).

Include sentiment analysis from news and social media for enhanced forecasting.

Author:

Bala Manikanta Kumar – Data Analytics & Python Enthusiast

GitHub: https://github.com/BalaManikanta-Dondapati
