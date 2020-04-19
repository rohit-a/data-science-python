# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:58:46 2020

@author: rohit

Python Script to simulate snakes and ladder game. Simulates 5000 games and each game can have maximun 1000 turns.

Q1 - What is the distribution of nuber of turns required to complete the game.
Q2 - What is the probability distribution of compelting the game in 'x' turns.
Q3 - What is the distribution of Snakes or Ladders encountered for completed games.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2020)
sample_games = 5000
max_turns = 1000

# To store stats for each game
all_games_stats_df = pd.DataFrame(columns = ['moves','snakes','ladders'])

# Reading board layput 
board_df = pd.read_csv("board_layout.csv", index_col=0)

# Simulating 5000 games
for i in range(sample_games):
    num_moves = 0
    num_snakes = 0
    num_ladders = 0
    current = 1
        
    # Simulating turns of a game
    for j in range(max_turns):
        current_type = 'NA'
        
        num_steps = np.random.randint(1,7)                                                  # Dice Roll
        num_steps = num_steps if num_steps != 6 else num_steps + np.random.randint(1,7)     # If player gets a 6 roll again
        
        if (current + num_steps) <= 100:
            current_type = board_df.loc[current + num_steps,'type']                         # Get position type
            current = board_df.loc[current + num_steps,'final_position']                    # Get next position from data frame
        
        num_moves = num_moves + 1
        num_snakes = num_snakes if current_type != 'S' else num_snakes + 1
        num_ladders = num_ladders if current_type != 'L' else num_ladders + 1
        
        if(current == 100):
            break
        
    all_games_stats_df.loc[i,['moves','snakes','ladders']] = [num_moves, num_snakes, num_ladders] 
    
plt.hist(all_games_stats_df['moves'], bins=20)
plt.title('Distribution of Moves required to complete {} games'.format(sample_games))
plt.xlabel('No of Moves')
plt.ylabel('No of Games')
plt.show()      