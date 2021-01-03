import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# define time frame
start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

# local data
ticker = 'FB'
data = web.DataReader(ticker, 'yahoo', start, end)

# print(data)
# print(data.columns)

# restructure data

data = data[['Open', 'High', 'Low', 'Close']]

data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)

# visualization

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title(f'{ticker} Share Price', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.5, colorup='#00ff00')
plt.show()
