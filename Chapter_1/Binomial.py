"""
Python adaption of  Analysis of Categorical Data with R: Chapter 1
@author Yong Kai Wong
@description To explore binomial distributions.

"""

from scipy.stats import binom
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import random

# Note that Bilder and Loughin denote a binomial variable with W
# Here we shall use K such that K ~ Binomial(n, p)
n, p = 5, 0.6

# Approach 1: binom.pmf
print(binom.pmf(k=0, n=n, p=p))
print(binom.pmf(k=1, n=n, p=p))

# Approach 2: binom
rv = binom(n, p)
print(rv)  # rv_frozen object
print(rv.pmf(0))
print(rv.pmf(1))

# Calculate PMF for k = 0,1,2....n
k = np.array(range(0, n+1))
print(k)
print(rv.pmf(k))

# Check if the sum of all pmf = 1
print(sum(rv.pmf(k)))

# close but not quite. Then what should we do?
# We shall cover this later
# Draw a PMF for K ~ Binomial(n, p)

plt.vlines(k, 0, rv.pmf(k), colors='black', lw=15)
plt.ylabel('$\mathbb{P}(K=k)$')
plt.xlabel('$k$')
plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.title('Binomial probability mass function for $n =$ {} and $\pi = ${}'.format(n, p))
plt.show()

# Simulate 1,000 bservations from a Binomial
# distribution with n = 5, prob = 0.6
random.seed(1234)

n, p, N = 5, 0.5, 1000
x = np.random.binomial(n=n, p=p, size=N)

# print the sample mean and variances
print(x.mean())
print(x.var())


# Print the head of simulated binomial variable
print(x[1:10])


# Plot a histogram of simulated binomial observations
plt.hist(x)
plt.ylabel('Count')
plt.xlabel('$k$')
plt.title('Binomial with $n =$ {}, $\pi = ${}, and {} observations'.format(n, p, N))
plt.show()


# Plot a histogram of simulated binomial observations with relative frequency
y = stats.relfreq(x, numbins=6)

plt.bar(k, y.frequency)
plt.ylabel('Relative frequency')
plt.xlabel('$k$')
plt.title('Binomial with $n =$ {}, $\pi = ${}, and {} observations'.format(n, p, N))
plt.show()