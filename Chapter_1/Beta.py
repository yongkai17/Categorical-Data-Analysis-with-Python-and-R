"""
Python adaption of  Analysis of Categorical Data with R: Chapter 1
@author Yong Kai Wong
@description To explore beta distributions.

"""

from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

# Let's create an array of 0 to 1
v = np.linspace(0, 1, num=100)

# Experiment with Beta(a, b) = Beta(5, 5)
a, b = 5, 5
plt.plot(v, beta.pdf(v, a, b))
plt.ylabel('$\mathbb{P}(v)$')
plt.xlabel('$v$')
plt.title('Beta ({}, {})'.format(a, b))
plt.show()

# Let's visualise 4 beta density functions for
# Beta(1, 1), Beta(1, 5), Beta(5, 1) and Beta(5, 5)
# in 4 subplots
param = [(a, b) for a in [1, 5] for b in [1, 5]]
k = 0
for i in param:
	k = k + 1
	a, b = i
	plt.subplot(220+k)
	plt.plot(v, beta.pdf(v, a, b))
	plt.ylabel('$\mathbb{P}(v)$')
	plt.title('Beta ({}, {})'.format(a, b), fontsize=10)
	plt.ylim(0, 5)

plt.subplots_adjust(top=0.9, bottom=0.10,
					left=0.10, right=0.95,
					hspace=0.35, wspace = 0.25)
plt.show()

