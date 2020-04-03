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
df = pd.read_csv("asylum-seekers-monthly.csv")
df.rename(columns={'Country / territory of asylum/residence': 'Country'}, inplace = True)
    
    
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
                mode = 'lines'
               )
        )
layout_v1 = dict(
        title = 'Changes in Total Number of Global Migrants',
        xaxis = dict(title = 'Year'),
        yaxis = dict(title = 'Number of Migrants'))
    
    
##########################Data for Visual 2##########################



##########################Data for Visual 3##########################
    
##########################Data for Visual 4##########################