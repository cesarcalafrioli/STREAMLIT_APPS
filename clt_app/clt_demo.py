"""
This app simulates 1,000 coin flips and stores those values in a list
we call binom_dist. We then sample (with replacement) 100 from that list, take the mean, and
store that mean in the cleverly named variable list_of_means. We do that 1,000 times (which is
overkill – we could do this even with dozens of samples), and then plot the histogram. After we
do this, the result of the following code should show a bell-shaped distribution.

We first created an empty figure and empty axes for that figure by calling
plt.subplots(), and then assigned the histogram we created to the ax variable.
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

binom_dist = np.random.binomial(1, .5, 100)
list_of_means = []

for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)

"""
Let’s let the user decide what the percentage chance of heads is, assign that
to a variable, and use that as an input in our binomial distribution.

The code below uses the st.number_input() function to collect our percentage,
assigns the user input to a variable (perc_heads), then uses that variable to
change the inputs to the binomial distribution function that we used before.
It also sets our histogram’s x axis to always be between 0 and 1, so we can
better notice changes as our input changes.
"""
perc_heads = st.number_input(label = 'Chance of Coins Landing on Heads',
min_value = 0.0, max_value = 1.0, value = .5)
binom_dist2 = np.random.binomial(1, perc_heads, 1000)
list_of_means2 = []
for i in range(0, 1000):
    list_of_means2.append(np.random.choice(binom_dist2, 100, replace=True). mean())

fig2, ax2 = plt.subplots()
ax2 = plt.hist(list_of_means2, range=[0,1])
st.pyplot(fig2)

"""
Accept text input in Streamlit using the st.text_ input() function, just as we did with the numeric input.
The next bit of code takes a text input and assigns it to the title of our graph.
"""
perc_heads3 = st.number_input(label='Chance of Coins Landing on Heads', min_value = 0.0, max_value=1.0, value=.5)
graph_title3 = st.text_input(label='Graph Title')
binom_dist3 = np.random.binomial(1, perc_heads3, 1000)
list_of_means3 = []
for i in range(0, 1000):
    list_of_means3.append(np.random.choice(binom_dist3, 100, replace=True).
mean())
fig3, ax3 = plt.subplots()
plt.hist(list_of_means2, range=[0,1])
plt.title(graph_title3)
st.pyplot(fig3)