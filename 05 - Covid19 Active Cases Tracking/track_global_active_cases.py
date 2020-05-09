# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:07:44 2020

@author: rohit

Track Active Coronovirus cases
Global Data from COVID-19 Data Repository by CSSE at Johns Hopkins University  https://github.com/CSSEGISandData/COVID-19
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dictionary to store file links
files_url = {
                "Confirmed":"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
                "Recovered":"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv",
                "Deaths":"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
            }


def get_data(case_type, file_path):
    # Reading file from file path and storing in data frame
    file_df = pd.read_csv(file_path)
    
    # Renaming and removing columns
    file_df = file_df.rename(columns={"Country/Region":"Country"}).drop(["Lat","Long"], axis="columns")

    # Aggregating data at Country Level (dropping "Province/State" column)
    file_df = file_df.groupby("Country").sum()

    # Pivoting down data
    file_df = file_df.reset_index().melt(id_vars='Country', var_name="Date", value_name=case_type)

    # Changing Date from String to Date type
    file_df['Date'] = pd.to_datetime(file_df['Date'])
    
    return file_df

def plot_data(df, columns, x='Date', row='Country', title=""):
    df = df[columns].reset_index().melt(id_vars=[row, x], var_name='Metric', value_name='Metric Value')
    g=sns.relplot(x=x, y='Metric Value', col='Metric', data=df, hue=row, kind='line', facet_kws={'sharey':'col'})  
    g.set_xticklabels(rotation=45)
    g.fig.suptitle(title, y=1.01)

# Creating data frame with appended Confirmed, Recovered and Deaths data
covid19_data = pd.concat([get_data(file_type, path) for file_type, path in files_url.items()])

# Creating signle row for Country, Date by aggregating data.
covid19_data = covid19_data.groupby(['Country','Date']).sum()

# Calculating Active cases and % Cases Active
covid19_data['Active'] = covid19_data['Confirmed'] - (covid19_data['Deaths'] + covid19_data['Recovered'])
covid19_data['% Cases Active'] = covid19_data['Active']/covid19_data['Confirmed']*100

# Dividing in countries in groups based on Confirmed cases
bin_values = [0, 15000, 30000, 100000, 500000, float('Inf')]
bin_labels = ["< 15,000", "15,000 - 30,000", "30,000 - 100,000", "100,000 - 500,000", "500,000+"]
cases_by_country = covid19_data.groupby('Country')[['Confirmed']].max().sort_values('Confirmed', ascending=False)
cases_by_country['group'] = pd.cut(cases_by_country['Confirmed'], bins=bin_values , labels=bin_labels)

# Plotting #Active Cases and % Active Cases

#Plotting for single country: US
countries = ['US']
data = covid19_data.loc[countries]
plot_data(data, ['Active', '% Cases Active'], 'Date', 'Country', 'Active Cases in '+str(countries))

#Plotting for Bins "30,000 - 100,000", "100,000 - 500,000"
for  val in ["30,000 - 100,000", "100,000 - 500,000"]:
    countries = cases_by_country[cases_by_country['group'] == val].reset_index()['Country'].unique()
    data = covid19_data.loc[countries]
    plot_data(data, ['Active', '% Cases Active'], 'Date', 'Country', 'Active Cases in Countries with '+val+' Confirmed Cases')
