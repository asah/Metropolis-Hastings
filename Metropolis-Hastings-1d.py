#
# Metropolis-Hastings algorithm, for study purposes (1-dimensional version)
#
import numpy as np
import matplotlib.pyplot as pl

def f(x):
    """
    define some function - could be anything, so let's pick something simple.

    intuition: given a location, what is the value at that location,
    e.g. for a restaurant, how busy is it by time of day?
    """
    return np.exp(-x**2)

# how many samples to take... I read that you need >>1000 to amortize
# startup searching, which seems suspicious and inefficient to me...
num_samples = 100_000
    
samples = np.arange(num_samples, dtype=np.float)
samples[0] = 0.2  # TODO(asah): WTF is this and why is it important?

# apparently, M-H has a concept of "accepting" a sample
# TODO: feels wasteful to me vs accepting everything... but I'm not a
# mathematician...
num_accepted = 0

# gather samples
for i in range(num_samples-1):
    # TODO: why use a normal distribution of random numbers?
    samples_next = np.random.normal(samples[i], 1.)
    # TODO: what is this magic?! what's the intuition?!
    if np.random.random_sample() < min(1, f(samples_next) / f(samples[i])):
        samples[i+1] = samples_next
        num_accepted = num_accepted + 1
    else:
        samples[i+1] = samples[i]
print(f"acceptance rate is {num_accepted / float(num_samples) * 100.0:.1f}%")

#
# create and display a histogram
#
pl.hist(samples, bins=50, color='blue')
pl.show()
