# -*- coding: utf-8 -*-
"""
The code in this python script will run on the backend of a data dashboard.

The script will wrangle the dataset from the CSV file and output a format that 
can be rendred as visuals by frontend library - in this case plotly.

The data being wrangled contains immigration data for 'Albania', 'Australia', 
'Austria', 'Belgium', 'Bulgaria','Bosnia and Herzegovina','Canada', 'Cyprus', 
and the 'Czech Republic' between 1999 and 2016.

"""

#Importing the relevant libraried
import pandas as pd
import plotly.graph_objs as go

#Reading the data from the CSV file into a dataframe 
df = pd.read_csv("asylum-seekers-global.csv")
df.rename(columns={'Country / territory of asylum/residence': 'Country'}, inplace = True)

#Clean the data 
#Drop missing data and null values
df.drop(df[df.Value == '*'].index, inplace=True)

#Cast entries in the Value column to integer (We're counting human beings)
df.Value = df.Value.astype('int64')
    
##########################Data for Visual 1##########################
    
#Select the required columns and groupby the Year column
df_v1 = df[['Year', 'Value']]
df_v1 = df_v1.groupby('Year').Value.sum()
df_v1 = df_v1.to_frame(name = 'count').reset_index()
    
#Create output dictionary for Plotly
df_v1.sort_values('Year', ascending=True, inplace=True)
visual_1 = []
visual_1.append(
        go.Scatter(
                x = df_v1['Year'].values.tolist(),
                y = df_v1['count'].values.tolist(),
                mode = 'lines',
                name = 'Year'
               )
        )
layout_v1 = dict(
        title = 'Changes in Total Number of Global Migrants',
        xaxis = dict(title = 'Year'),
        yaxis = dict(title = 'Number of Migrants'))
    
    
##########################Data for Visual 2##########################
#Filter dataset to get relevant data
df_v2 = df[['Country', 'Year', 'Value']]
df_v2 = df_v2[ df_v2.Year.isin(range(1999,2008))]
df_v2 = df_v2.drop(['Year'], axis = 1)

#Group df by country to find total numbers for each country
df_v2 = df_v2.groupby('Country').Value.sum()
df_v2 = df_v2.to_frame(name = 'count').reset_index()

#Select the top 10 Countries
df_v2.sort_values(by=['count'], ascending = False, inplace = True)
df_v2 = df_v2.iloc[:10,:]

#Create output dictionary for Plotly
visual_2 = []
visual_2.append(
        go.Bar(
                x = df_v2['Country'].values.tolist(),
                y = df_v2['count'].values.tolist(),
               )
        )
layout_v2 = dict(
        title = 'Top 10 Asylum Destinations From 1999 - 2008',
        xaxis = dict(title = 'Country'),
        yaxis = dict(title = 'Number of Migrants'))

##########################Data for Visual 3##########################
    
##########################Data for Visual 4##########################