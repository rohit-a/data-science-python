# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:43:05 2020

@author: rohit

A comprehensive analysis of the Android app market by comparing over ten thousand apps in Google Play across different categories. 
We'll look for insights in the data to devise strategies to drive growth and retention.

"""

import pandas as pd
import matplotlib.pyplot as plt

# Reading apps data csv
apps_with_duplicates = pd.read_csv('datasets/apps.csv')

##
# View sample data
##
# Drop duplicates
apps = apps_with_duplicates.drop_duplicates(subset='App')
# Print the total number of apps
print('Total number of apps in the dataset = ', apps['App'].count())
# Have a look at a random sample of 5 rows
n = 5
apps.sample(n)


##
# Look at three columns we are working with - Installs, Size, Price
# Clean up on these columns to convert to numeric type
##

# Look at values in the column
print("Installs:\n", apps['Installs'].value_counts().index.values)
print("Size:\n",apps['Size'].value_counts().index.values)
print("Price:\n",apps['Price'].value_counts().index.values)

#Clean up non numeric characters
# List of characters to remove
chars_to_remove = ['+', 'M', '$', ',']

# List of column names to clean
cols_to_clean = ['Installs', 'Size', 'Price']

# Loop for each column
for col in cols_to_clean:
    # Replace each character with an empty string
    for char in chars_to_remove:
        apps[col] = apps[col].str.replace(char, '')
    # Convert col to numeric
    apps[col] = pd.to_numeric(apps[col]) 

##
# Which category has the highest share of (active) apps in the market?
# Is any specific category dominating the market?
# Which categories have the fewest number of apps?
##

# Print the total number of unique categories
num_categories = len(apps['Category'].unique())
print('\nNumber of categories = ', num_categories)

# Count the number of apps in each 'Category' and sort them in descending order
num_apps_in_category = apps['Category'].value_counts().sort_values(ascending = False)

num_apps_in_category.plot(kind="bar")
plt.show()
# There are 33 unique app categories present in our dataset. 
# Family and Game apps have the highest market prevalence. Interestingly, Tools, Business and Medical apps are also at the top.

##
# Distribution of App Ratings
##

# Average rating of apps
avg_app_rating = apps['Rating'].mean()
print('Average app rating = ', avg_app_rating)

#Histogram of app ratings
apps['Rating'].plot(kind="hist", bins=50)
plt.show()
# The average volume of ratings across all app categories is 4.17. 
# The histogram plot is skewed to the right indicating that the majority of the apps are highly rated 
# with only a few exceptions in the low-rated apps.

##
# Size and price of apps
# Does the size of an app affect its rating?
# Do users really care about system-heavy apps or do they prefer light-weighted apps?
# Does the price of an app affect its rating?
# Do users always prefer free apps over paid apps?
##

#%matplotlib inline
import seaborn as sns
sns.set_style("darkgrid")
import warnings
warnings.filterwarnings("ignore")

# Subset for categories with at least 250 apps
large_categories = apps.groupby(apps['Category']).filter(lambda x: len(x) >= 250).reset_index()

# Plot size vs. rating
plt1 = sns.jointplot(x = large_categories['Rating'], y = large_categories['Size'], kind = 'hex')

# Subset out apps whose type is 'Paid'
paid_apps = apps[apps['Type'] == 'Paid']

# Plot price vs. rating
plt2 = sns.jointplot(x = paid_apps['Rating'], y = paid_apps['Price'])

# The majority of top rated apps (rating over 4) range from 2 MB to 20 MB. 
# The vast majority of apps price themselves under $10.

##
# Relation between app category and app price
##

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# Select a few popular app categories
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                            'MEDICAL', 'TOOLS', 'FINANCE',
                                            'LIFESTYLE','BUSINESS'])]

# Examine the price trend by plotting Price vs Category
ax = sns.stripplot(x = popular_app_cats['Price'], y = popular_app_cats['Category'], jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories')

# Apps whose Price is greater than 200
apps_above_200 = popular_app_cats[['Category', 'App', 'Price']][popular_app_cats['Price'] > 200]
apps_above_200

# Medical and Family apps are the most expensive. Some medical apps extend even up to $80! All game apps are reasonably priced below $20.

##
# Filter out Junk Apps
# It looks like a bunch of the really expensive apps are "junk" apps. 
# That is, apps that don't really have a purpose. Some app developer may create an app called I Am Rich Premium or most expensive app (H)
# just for a joke or to test their app development skills. Some developers even do this with malicious intent and try to make money by hoping 
# people accidentally click purchase on their app in the store.
##

# Select apps priced below $100
apps_under_100 = apps[apps['Price'] < 100]

fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# Examine price vs category with the authentic apps
ax = sns.stripplot(x=apps_under_100['Price'], y=apps_under_100['Category'], data=apps_under_100,
                   jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories after filtering for junk apps')

# The distribution of apps under $20 becomes clearer.


##
# Sentiment Analysis of user reviews
##

# Load user_reviews.csv
reviews_df = pd.read_csv("datasets/user_reviews.csv")

# Join and merge the two dataframe
merged_df = pd.merge(apps, reviews_df, on = 'App', how = "inner")

# Drop NA values from Sentiment and Translated_Review columns
merged_df = merged_df.dropna(subset=['Sentiment', 'Translated_Review'])

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11, 8)

# User review sentiment polarity for paid vs. free apps
ax = sns.boxplot(x = merged_df['Type'], y = merged_df['Sentiment_Polarity'] , data = merged_df)
ax.set_title('Sentiment Polarity Distribution')


