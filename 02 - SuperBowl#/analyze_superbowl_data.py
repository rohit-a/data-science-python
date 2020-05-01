# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:20:58 2020

@author: rohit
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Load the CSV data into DataFrames
super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

##
# View loaded datasets
##
# Display the first five rows of each DataFrame
print(super_bowls.head())
print(tv.head())
print(halftime_musicians.head())


##
# Lokking at dataset issue
##
#Summary of Superbowls data
print('\nSuperbowls info')
halftime_musicians.info()
# Summary of the TV data to inspect
print("\nTV Info")
tv.info()
# Summary of the halftime musician data to inspect
print('\nMusicians Info')
halftime_musicians.info()
#Superbowls combined point column info
print('\n Combined Points Info')
print(super_bowls['combined_pts'].describe())


##
# Look at distirbution of number of point scored
# Plotting histogram of points vs number of games
# Looking at games with highest and lowest total scores
##
plt.style.use('seaborn')
# Plot a histogram of combined points
plt.hist(super_bowls['combined_pts'])
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()
# Display the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls['combined_pts'] > 70])
print(super_bowls[super_bowls['combined_pts'] < 25])


##
# Look at distribution of games by point differene between winning and losing teams
# Show closest games and games with most difference in points
##
# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()
# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls['difference_pts'] == 1])
print(super_bowls[super_bowls['difference_pts'] > 40])


##
# Does point differnce affect viewership.
# Are closer games watched by more people vs games with more differences
##
# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')
# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=games_tv)
# We can see that share declines when difference in points is huge.


##
# How has viewership, ad cost and house hold ratings changed over time 
##
# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot( tv['super_bowl'],tv['avg_us_viewers'],color='blue')
plt.title('Average Number of US Viewers')
# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot( tv['super_bowl'],tv['rating_household'],color='magenta')
plt.title('Household Rating')
# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv['super_bowl'],tv['ad_cost'], color='yellow')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')
# Improve the spacing between subplots
plt.tight_layout()
#We can see viewers increased before ad costs did. Maybe the networks weren't very data savvy and were slow to react?

##
# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII.
# Before NFL started signing big names, XXVII was when NFL signed up MJ
##
# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
halftime_musicians[halftime_musicians['super_bowl']<=27]
#The halftime shows before MJ indeed weren't that impressive

##
# Who has most half time appearances
##
# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)
# Display musicians with more than one halftime show appearance
print(halftime_appearances[halftime_appearances['super_bowl']>1])
#Beyoncé, Justin Timberlake, Nelly, and Bruno Mars are the only post-Y2K musicians with multiple appearances (two each).

##
# Who performed most songs ? 
##
# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]
# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].to_numpy()))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()
# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
print(no_bands.head(15))

