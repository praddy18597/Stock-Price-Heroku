import yfinance as yf    #it will take take data from yahoo finance
import streamlit as st
import pandas as pd 

st.write("""
# Simple Stock Price App

Shown are the stcok **closing price** and **volume of google**!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period= 'id', start = '2010-5-31', end = '2020-5-31')

#open high    low close    volume dividends    stock splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
