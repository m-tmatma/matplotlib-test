# https://sabopy.com/py/matplotlib-33/
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

dates = [datetime.datetime(2018, 1, 1) + datetime.timedelta(hours=k * 6)
            for k in range(240)]
temperature = 20 + np.random.randn(len(dates))
fig, ax = plt.subplots(constrained_layout=True)

ax.plot(dates, temperature)
ax.set_ylabel(r'$T\ [^oC]$')
plt.xticks(rotation=70)

ax.xaxis.set_major_formatter(DateFormatter('%Y/%m/%d %H:%M:%S'))

def date2yday(x):
    """
    x is in matplotlib datenums, so they are floats.
    """
    y = x - mdates.date2num(datetime.datetime(2018, 1, 1))
    return y


def yday2date(x):
    """
    return a matplotlib datenum (x is days since start of year)
    """
    y = x + mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

secaxx = ax.secondary_xaxis('top', functions=(date2yday, yday2date))
secaxx.set_xlabel('yday [2018]')


def CtoF(x):
    return x * 1.8 + 32


def FtoC(x):
    return (x - 32) / 1.8

secaxy = ax.secondary_yaxis('right', functions=(CtoF, FtoC))
secaxy.set_ylabel(r'$T\ [^oF]$')
#plt.savefig('datetime_do.jpg',dpi=100)
ax.grid()
fig.tight_layout()
plt.show()