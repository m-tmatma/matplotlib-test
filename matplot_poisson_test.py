'''
This is a test for plotting a poisson distribution graph using matplotlib
'''
# https://stackoverflow.com/questions/51242748/plot-a-poisson-distribution-graph-in-python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

LAMBDA = 5
t = np.arange(0, 20, 0.1)
d = np.exp(-LAMBDA)*np.power(LAMBDA, t)/factorial(t)

plt.plot(t, d, 'bs')
plt.grid()
plt.show()
