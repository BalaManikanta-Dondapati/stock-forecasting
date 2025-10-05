# streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet
from prophet.plot import plot_plotly
from statsmodels.tsa.arima.model import ARIMA

# -------------------
# Load Data
# -------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data("data/AAPL_cleaned.csv")

# Limit to last 3 years to save memory
max_date = df['Date'].max()
min_date = max_date - pd.DateOffset(years=3)
df_recent = df[df['Date'] >= min_date].copy()

# -------------------
# Sidebar
# -------------------
st.sidebar.header("Stock Forecasting App")
selected_stock = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
forecast_days = st.sidebar.slider("Days to Forecast", 30, 90, 30)

st.title(f"{selected_stock} Stock Forecasting Dashboard")

# -------------------
# Moving Averages
# -------------------
df_recent['MA7'] = df_recent['Close'].rolling(7).mean()
df_recent['MA30'] = df_recent['Close'].rolling(30).mean()

# -------------------
# Historical Data
# -------------------
st.subheader("Historical Data with Moving Averages")
fig_hist = go.Figure()
fig_hist.add_trace(go.Scatter(x=df_recent['Date'], y=df_recent['Close'], 
                              mode='lines', name='Close'))
fig_hist.add_trace(go.Scatter(x=df_recent['Date'], y=df_recent['MA7'], 
                              mode='lines', name='7-day MA'))
fig_hist.add_trace(go.Scatter(x=df_recent['Date'], y=df_recent['MA30'], 
                              mode='lines', name='30-day MA'))
st.plotly_chart(fig_hist, use_container_width=True)

# -------------------
# Prophet Forecast
# -------------------
st.subheader(f"{forecast_days}-Day Forecast Using Prophet")

# Prepare data for Prophet
df_prophet = df_recent[['Date', 'Close']].rename(columns={'Date':'ds', 'Close':'y'})
df_prophet['y'] = pd.to_numeric(df_prophet['y'], errors='coerce')
df_prophet = df_prophet.dropna()

@st.cache_data
def fit_prophet(df_prophet):
    model = Prophet(daily_seasonality=False, changepoint_prior_scale=0.05)
    model.fit(df_prophet)
    return model

model_prophet = fit_prophet(df_prophet)

future = model_prophet.make_future_dataframe(periods=forecast_days)
forecast_prophet = model_prophet.predict(future)

# -------------------
# ARIMA Forecast
# -------------------
st.subheader(f"{forecast_days}-Day Forecast Using ARIMA")

# Fit ARIMA model
model_arima = ARIMA(df_recent['Close'], order=(5,1,0))
model_arima_fit = model_arima.fit()

# Forecast
forecast_arima = model_arima_fit.forecast(steps=forecast_days)
future_dates = pd.date_range(df_recent['Date'].iloc[-1] + pd.Timedelta(days=1), 
                             periods=forecast_days, freq='D')
# Convert to list of strings for caching
future_dates_list = future_dates.strftime('%Y-%m-%d').tolist()

# -------------------
# Plot Comparison
# -------------------
st.subheader("Forecast Comparison: Prophet vs ARIMA")
fig_forecast = go.Figure()

# Historical
fig_forecast.add_trace(go.Scatter(x=df_recent['Date'], y=df_recent['Close'], 
                                  mode='lines', name='Historical'))

# Prophet forecast
fig_forecast.add_trace(go.Scatter(x=forecast_prophet['ds'], y=forecast_prophet['yhat'], 
                                  mode='lines', name='Prophet Forecast'))

# ARIMA forecast
fig_forecast.add_trace(go.Scatter(x=future_dates, y=forecast_arima, 
                                  mode='lines', name='ARIMA Forecast'))

st.plotly_chart(fig_forecast, use_container_width=True)

# -------------------
# Download Forecasts
# -------------------
@st.cache_data
def save_forecasts(prophet, arima, arima_dates_list):
    path_prophet = "data/AAPL_prophet_forecast.csv"
    path_arima = "data/AAPL_arima_forecast.csv"
    prophet.to_csv(path_prophet, index=False)
    df_arima = pd.DataFrame({'Date': arima_dates_list, 'ARIMA_Prediction': arima})
    df_arima.to_csv(path_arima, index=False)
    return path_prophet, path_arima

path_prophet, path_arima = save_forecasts(forecast_prophet, forecast_arima, future_dates_list)

st.download_button("Download Prophet Forecast CSV", data=open(path_prophet,'rb'), 
                   file_name='AAPL_prophet_forecast.csv')
st.download_button("Download ARIMA Forecast CSV", data=open(path_arima,'rb'), 
                   file_name='AAPL_arima_forecast.csv')
