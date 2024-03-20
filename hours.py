'''
sample code to show how to use secondary_xaxis to plot data in hours
'''
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np

origin = datetime.datetime(2018, 1, 1)

def date2yday(x):
    """
    x is in matplotlib datenums, so they are floats.
    """
    y = x - mdates.date2num(origin)
    return y * 24

def yday2date(x):
    """
    return a matplotlib datenum (x is days since start of year)
    """
    y = x / 24 + mdates.date2num(origin)
    return y

X = np.arange(0, 24*7, 24)
Y = np.square(X)

fig, ax = plt.subplots(constrained_layout=True)
ax.grid()
ax.plot(X, Y)

# label
ax.xaxis.set_major_locator(ticker.MultipleLocator(24))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(6))

secaxx = ax.secondary_xaxis('top', functions=(yday2date, date2yday))
secaxx.set_xlabel('ellapsed time [hours]')
secaxx.xaxis.set_ticklabels(ax.get_xticks(), rotation=90)
secaxx.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d\n%H:%M:%S'))
fig.tight_layout()
plt.show()
