'''
sample code to demonstrate how to use secondary_xaxis to plot a time series with a secondary x-axis
'''
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

X = np.arange(datetime.datetime(2022, 1, 1), datetime.datetime(2023, 1, 1), datetime.timedelta(days=1))
Y = np.linspace(0, 100, X.size)

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(X, Y)
ax.set_ylabel(r'test')
ax.xaxis.set_label_position('top')
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_ticklabels(ax.get_xticks(), rotation=45)
ax.xaxis.set_label("date")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d\n%H:%M:%S'))

ticks = []
temp = ax.get_xticks()
for l in temp:
    diff = l - temp[0]
    print(l, diff)
    ticks.append(diff * 24)

def date2yday(x):
    """
    x is in matplotlib datenums, so they are floats.
    """
    y = x - mdates.date2num(datetime.datetime(2022, 1, 1))
    return y * 24

def yday2date(x):
    """
    return a matplotlib datenum (x is days since start of year)
    """
    y = x / 24 + mdates.date2num(datetime.datetime(2022, 1, 1))
    return y

secaxx = ax.secondary_xaxis('bottom', functions=(date2yday, yday2date))
secaxx.set_xlabel('ellapsed time [hours]')
secaxx.set_xticks(ticks)
ax.grid()
plt.show()
