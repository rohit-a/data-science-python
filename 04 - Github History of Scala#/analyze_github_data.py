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

##
# Is project actively maintained.
##
# Create a column that will store the month and the year, as a string
data['month_year'] = data['date'].dt.strftime("%m-%Y")

# Group by month_year and count the pull requests
counts = data.groupby('month_year')['pid'].count()

# Plot the results
counts.plot()

##
# Plot counts by contributors
##
# Group by the submitter
by_user = data.groupby('user')['pid'].count()

# Plot the histogram
by_user.plot(kind='hist')

##
# What files were changed in the last ten pull requests
##
# Identify the last 10 pull requests
last_10 = pulls.nlargest(10, 'date')

# Join the two data sets
joined_pr = pd.merge(last_10, pull_files)

# Identify the unique files
files = set(joined_pr['file'].unique())

# Print the results
files

##
# Who made the most pull requests to a given file
##
# This is the file we are interested in:
file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

# Identify the commits that changed the file
file_pr = data[data['file'] == 'src/compiler/scala/reflect/reify/phases/Calculate.scala']

# Count the number of changes made by each developer
author_counts = file_pr.groupby('user')['pid'].count()

# Print the top 3 developers
print(author_counts.nlargest(3))

##
# Who made the last ten pull requests on a given file
##
file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

# Select the pull requests that changed the target file
file_pr = pull_files[pull_files['file']=='src/compiler/scala/reflect/reify/phases/Calculate.scala']

# Merge the obtained results with the pulls DataFrame
joined_pr = pd.merge(file_pr, pulls)

# Find the users of the last 10 most recent pull requests
users_last_10 = set(joined_pr.nlargest(10, 'date')['user'])

# Printing the results
users_last_10

##
# The pull requests of two special developers
##
# The developers we are interested in
authors = ['xeno-by', 'soc']

# Get all the developers' pull requests
by_author = pulls[pulls['user'].isin(authors)]

# Count the number of pull requests submitted each year
counts = by_author.groupby(['user',by_author['date'].dt.year]).agg({'pid': 'count'}).reset_index()

# Convert the table to a wide format
counts_wide = counts.pivot_table(index='year', columns='user', values='pid', fill_value=0)

# Plot the results
counts_wide.plot(kind="bar")


##
# Visualizing the contributions of each developer
##

authors = ['xeno-by', 'soc']
file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

# Select the pull requests submitted by the authors, from the `data` DataFrame
by_author = data[data['user'].isin(authors)]

# Select the pull requests that affect the file
by_file = by_author[by_author['file'] == file]

# Group and count the number of PRs done by each user each year
grouped = by_file.groupby(['user', by_file['date'].dt.year]).count()['pid'].reset_index()

# Transform the data into a wide format
by_file_wide = grouped.pivot_table(index='date', columns='user', values='pid', fill_value=0)

# Plot the results
by_file_wide.plot(kind='bar')

