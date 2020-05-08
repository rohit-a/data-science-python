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


def get_data(file_path):
    # Reading file from file path and storing in data frame
    file_df = pd.read_csv(file_path)

    # Renaming and removing columns
    file_df = file_df.rename(columns={"Country/Region":"Country"}).drop(["Lat","Long"], axis="columns")

    # Aggregating data at Country Level (dropping "Province/State" column)
    file_df = file_df.groupby("Country").sum()

    # Pivoting down data
    file_df = file_df.reset_index().melt(id_vars='Country', var_name="Date")

    # Changing Date from String to Date type
    file_df['Date'] = pd.to_datetime(file_df['Date'])

    return file_df

# Creating a blank data frame
covid19_data = pd.DataFrame()

# Looping through files to create combined data frame
for name, path in files_url.items():
    df = get_data(path)
    df['Type'] = name
    covid19_data = covid19_data.append(df)

# Pivoting up on type to get single row for each Country, Date
covid19_data = covid19_data.pivot_table(index=['Country','Date'], columns = 'Type', values = 'value', aggfunc=sum, fill_value=0).reset_index()




# # Read Global data files for confirmed, recovered and deaths data.
# confirmed_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
# recovered_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
# deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# df_confirmed = pd.read_csv(confirmed_url)
# df_recovered = pd.read_csv(recovered_url)
# df_deaths = pd.read_csv(deaths_url)

# # Removing and renaming columns.
# df_confirmed = df_confirmed.rename(columns={"Country/Region":"Country"}).drop(["Lat","Long"], axis="columns")
# df_recovered = df_recovered.rename(columns={"Country/Region":"Country"}).drop(["Lat","Long"], axis="columns")
# df_deaths = df_deaths.rename(columns={"Country/Region":"Country"}).drop(["Lat","Long"], axis="columns")

# # Aggregating data at Country Level and dropping "Province/State" column
# df_confirmed = df_confirmed.groupby("Country").sum()
# df_recovered = df_recovered.groupby("Country").sum()
# df_deaths = df_deaths.groupby("Country").sum()

# # Pivoting down data
# df_confirmed = df_confirmed.reset_index().melt(id_vars='Country', var_name="Date", value_name="Confirmed")
# df_recovered = df_recovered.reset_index().melt(id_vars='Country', var_name="Date", value_name="Recovered")
# df_deaths = df_deaths.reset_index().melt(id_vars='Country', var_name="Date", value_name="Deaths")

# df_confirmed['Date'] = pd.to_datetime(df_confirmed['Date'])
# df_recovered['Date'] = pd.to_datetime(df_recovered['Date'])
# df_deaths['Date'] = pd.to_datetime(df_deaths['Date'])


