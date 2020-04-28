# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:11:55 2020

@author: rohit
"""

import pandas as pd

##
# Importing data
##
# Loading in the data
pulls_one = pd.read_csv('datasets/pulls_2011-2013.csv')
pulls_two = pd.read_csv('datasets/pulls_2014-2018.csv')
pull_files = pd.read_csv('datasets/pull_files.csv')

##
# Preparing and cleaning data
##
# Append pulls_one to pulls_two
pulls = pulls_one.append(pulls_two, ignore_index=True)

# Convert the date for the pulls object
pulls['date'] = pd.to_datetime(pulls['date'], utc=True)

##
# Merging data
##

# Merge the two DataFrames
data = pd.merge(pulls, pull_files)