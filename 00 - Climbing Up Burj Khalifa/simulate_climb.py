# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:16:56 2020

@author: rohit

Pyhton script to simulate walks and show distribution and probabilty of reaching a floor.
Rules: 
    1. Player starts at floor 0 and throws a dice on each turn.
    2. If he gets 1,2 - player has to come down 1 floor.
    3. If he gets 3,4,5 - player climbs 1 floor.
    4. IF he gets 6, he gets to throw 1 more time and climbs as many floors as the number in the throw.
    5. Clumsiness: 0.1% of time player trips and falls to FLoor 0 (Without damage :D)
    6. By default, player gets to take 100 steps (throws dice 100 times)
    
Q1 - What is the distribution of floor reached over 5000 walks.
Q2 - What is the probability distribution of reaching a floor over 100 turns.

"""

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(2020)
all_walks = []                                      # Stores all walks.
sample_walks = 5000                                 # Number of sample walks
num_steps    = 100                                  # Number of Steps in each walk

# Simulate random walk 5000 times
for i in range(sample_walks) :                      # Simulate 5000 walks.
    random_walk = [0]                               # We start a walks from 0.
    for x in range(num_steps) :                     # 100 steps for each walk
        floor = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:                               # Dice conditions. 
            floor = max(0, floor - 1)
        elif dice <= 5:
            floor = floor + 1
        else:
            floor = floor + np.random.randint(1,7)  
        if np.random.rand() <= 0.001 :              # 0.1 % of times, reset to 0 due to clumsiness
            floor = 0
        random_walk.append(floor)                   # Append next step to a walk
    all_walks.append(random_walk)                   # Append a walk to all walks

# Create and plot all walks
np_aw_t = np.transpose(np.array(all_walks))         # Transpose for plotting
plt.plot(np_aw_t)
plt.xlabel('Sequence')
plt.ylabel('Floor')
plt.title('Floor for each turn over {} walks'.format(sample_walks))
plt.show()

# Select Floor reached in each walk - last row from np_aw_t
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.xlabel('Floor Reached')
plt.ylabel('No of Walks')
plt.title('Distribution of Floor reached over {} walks'.format(sample_walks))
plt.show()

# Plot probability of reaching a floor over 100 steps
plt.hist(ends, density=True, histtype='step', cumulative=-1, label='Reversed emp.')
plt.xlabel('Floor Reached')
plt.ylabel('Probability')
plt.title('Probability of Floor Reached over {} steps'.format(num_steps))
plt.show()
