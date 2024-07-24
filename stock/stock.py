import numpy as np
import pandas as pd
import tensorflow as tf
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
from ta import add_all_ta_features

# Load the model
model = load_model('C:\\Users\\harsh\\stock\\Stock Predictions Model.keras')

# Define custom CSS for styling
st.markdown("""
<style>
.main {
    background-color: #F5F5F5;
    padding-bottom: 50px; /* Adjust padding to accommodate the footer */
}
.header {
    font-size: 50px;
    color: #2E4053;
    text-align: center;
    padding: 10px;
}
.subheader {
    font-size: 30px;
    color: #2E4053;
    text-align: center;
    padding: 10px;
}
.textbox {
    width: 300px;
    height: 40px;
    font-size: 20px;
    margin: 20px auto;
    display: block;
}
.dataframe {
    margin: 20px auto;
    width: 90%;
}
.plot {
    margin: 20px auto;
    width: 90%;
}
.logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 120px;
    height: auto;
    margin-bottom: 20px;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #2E4053;
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 12px; /* Adjust font size */
}
</style>
""", unsafe_allow_html=True)

# Display the logo
st.markdown('<img src="https://i.pinimg.com/564x/7a/72/35/7a7235fc3e410289333a3da91118111e.jpg" class="logo">', unsafe_allow_html=True)

# Define the header
st.markdown('<p class="header">Stock Market Analysis</p>', unsafe_allow_html=True)

# Input field for stock symbol and date range
stock = st.text_input('Enter Stock Symbol', 'GOOG', key='textbox')
start_date = st.date_input('Start Date', datetime(2012, 1, 1))
end_date = st.date_input('End Date', datetime.today())

# Download the stock data
data = yf.download(stock, start=start_date, end=end_date)

# Display the stock data
st.markdown('<p class="subheader">Stock Data</p>', unsafe_allow_html=True)
st.write(data)

# Calculate technical indicators
data_ta = add_all_ta_features(data, open="Open", high="High", low="Low", close="Close", volume="Volume")

# Prepare training and testing data
data_train = pd.DataFrame(data_ta.Close[0: int(len(data_ta)*0.80)])
data_test = pd.DataFrame(data_ta.Close[int(len(data_ta)*0.80):])

scaler = MinMaxScaler(feature_range=(0, 1))

pas_100_days = data_train.tail(100)
data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
data_test_scale = scaler.fit_transform(data_test)

# Plot MA50
st.markdown('<p class="subheader">Price vs MA50</p>', unsafe_allow_html=True)
ma_50_days = data_ta.Close.rolling(50).mean()
fig1 = plt.figure(figsize=(8, 6))
plt.plot(ma_50_days, 'r', label='MA50')
plt.plot(data_ta.Close, 'g', label='Close Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig1)

# Plot MA50 and MA100
st.markdown('<p class="subheader">Price vs MA50 vs MA100</p>', unsafe_allow_html=True)
ma_100_days = data_ta.Close.rolling(100).mean()
fig2 = plt.figure(figsize=(8, 6))
plt.plot(ma_50_days, 'r', label='MA50')
plt.plot(ma_100_days, 'b', label='MA100')
plt.plot(data_ta.Close, 'g', label='Close Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)

# Plot MA100 and MA200
st.markdown('<p class="subheader">Price vs MA100 vs MA200</p>', unsafe_allow_html=True)
ma_200_days = data_ta.Close.rolling(200).mean()
fig3 = plt.figure(figsize=(8, 6))
plt.plot(ma_100_days, 'r', label='MA100')
plt.plot(ma_200_days, 'b', label='MA200')
plt.plot(data_ta.Close, 'g', label='Close Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig3)

# Prepare data for prediction
x = []
y = []

for i in range(100, data_test_scale.shape[0]):
    x.append(data_test_scale[i-100:i])
    y.append(data_test_scale[i, 0])

x, y = np.array(x), np.array(y)

# Make predictions
predict = model.predict(x)

scale = 1 / scaler.scale_

predict = predict * scale
y = y * scale

# Plot original vs predicted prices
st.markdown('<p class="subheader">Original Price vs Predicted Price</p>', unsafe_allow_html=True)
fig4 = plt.figure(figsize=(8, 6))
plt.plot(predict, 'r', label='Predicted Price')
plt.plot(y, 'g', label='Original Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig4)

# Add a footer for copyright
st.markdown('<div class="footer">© 2024 Created by Harshad, Yugant, and Shravani — All rights reserved.</div>', unsafe_allow_html=True)
