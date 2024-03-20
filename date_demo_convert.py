'''
This script demonstrates how to plot dates on the x-axis using Matplotlib.
'''

# https://matplotlib.org/2.0.2/examples/pylab_examples/date_demo_convert.html
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange, date2num
from numpy import arange
import numpy as np

date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)

Y = arange(len(dates)*1.0)

# https://qiita.com/nkay/items/d1eb91e33b9d6469ef51
fig, ax = plt.subplots(constrained_layout=True)
ax.plot(dates, Y*Y)

# this is superfluous, since the autoscaler should get it right, but
# use date2num and num2date to convert between dates and floats if
# you want; both date2num and num2date convert an instance or sequence
ax.set_xlim(dates[0], dates[-1])

# The hour locator takes the hour or sequence of hours you want to
# tick, not the base multiple

# ax.xaxis.set_major_locator(DayLocator())
# ax.xaxis.set_minor_locator(HourLocator(arange(0, 25, 1)))
ax.xaxis.set_major_locator(HourLocator(interval=6))
ax.xaxis.set_minor_locator(HourLocator(interval=3))
ax.xaxis.set_major_formatter(DateFormatter('%Y/%m/%d %H:%M:%S'))

# https://github.com/Randle9000/pythonCheatSheet/blob/5308a430f0c405a979a8ba17b409bf6b1256ec36/pythonCourseEu/3_NumericalPython/matplotlib_examples/subplots_axes_and_figures/secondary_axis.py#L114-L133
# https://sabopy.com/py/matplotlib-33/
# https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2timedelta
def date2yday(x):
    """Convert matplotlib datenum to days since date1."""
    y = x - date2num(date1)
    return y

def yday2date(x):
    """Return a matplotlib datenum for x days after date1."""
    y = x + date2num(date1)
    return y

sec_ax = ax.secondary_xaxis('top', functions=(date2yday, yday2date))
sec_ax.set_xlabel('time elapsed')

ax.fmt_xdata = DateFormatter('%Y/%m/%d %H:%M:%S')
ax.tick_params(axis='x', rotation=90)
#fig.autofmt_xdate()
ax.grid()
#fig.subplots_adjust()
#fig.tight_layout()
plt.show()
