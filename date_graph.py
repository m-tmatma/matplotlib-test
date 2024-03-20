'''
sample code for secondary_xaxis
'''
# https://sabopy.com/py/matplotlib-33/
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from matplotlib.dates import DateFormatter

def date2yday(x):
    """
    x is in matplotlib datenums, so they are floats.
    """
    y = x - mdates.date2num(datetime.datetime(2018, 1, 1))
    return y * 24


def yday2date(x):
    """
    return a matplotlib datenum (x is days since start of year)
    """
    y = x / 24 + mdates.date2num(datetime.datetime(2018, 1, 1))
    return y

def convert_c_to_f(x):
    '''
    Convert Celsius to Fahrenheit
    '''
    return x * 1.8 + 32


def convert_f_to_c(x):
    '''
    Convert Fahrenheit to Celsius
    '''
    return (x - 32) / 1.8

dates = [datetime.datetime(2018, 1, 1) + datetime.timedelta(hours=k * 6)
            for k in range(240)]
temperature = 20 + np.random.randn(len(dates))
fig, ax = plt.subplots(constrained_layout=True)

ax.plot(dates, temperature)
ax.set_ylabel(r'$T\ [^oC]$')
plt.xticks(rotation=90)

ax.xaxis.set_major_formatter(DateFormatter('%Y/%m/%d %H:%M:%S'))

secaxx = ax.secondary_xaxis('bottom', functions=(date2yday, yday2date))
secaxx.set_xlabel('ellapsed time [hours]')
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_ticklabels(ax.get_xticks(), rotation=45)
ax.xaxis.set_major_formatter(DateFormatter('%Y/%m/%d %H:%M:%S'))

ticks = []
temp = ax.get_xticks()
for l in temp:
    diff = l - temp[0]
    print(l, diff)
    ticks.append(diff * 24)
secaxx.set_xticks(ticks)

secaxy = ax.secondary_yaxis('right', functions=(convert_c_to_f, convert_f_to_c))
secaxy.set_ylabel(r'$T\ [^oF]$')
#plt.savefig('datetime_do.jpg',dpi=100)
ax.grid()
fig.tight_layout()
plt.show()
