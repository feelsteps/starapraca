# coding: utf-8
import numpy as np
import pandas as pd
import json
from fuzzywuzzy import process, fuzz
import time
import pdb
import math
import plotly.offline as offline
import plotly.graph_objs as go
offline.init_notebook_mode()

#fm1 = pd.read_csv('fmMapPpl.csv')

fm11 = pd.read_csv('C:/Users/filip.stepniak/Projects/1_Project_Leviathan/map_csv/fmMapPpl_19-06-2018.csv')
print(len(fm11))
fm1 = fm11[fm11['suma']>2]
print(len(fm1))

#gp2 = pd.read_csv('gpProjects.csv')

gp22 = pd.read_csv('C:/Users/filip.stepniak/Projects/1_Project_Leviathan/map_csv/gpMapProjects_19-06-2018.csv')
print(len(gp22))
gp2 = gp22[gp22['suma']>2]
print(len(gp2))

#fm2 = pd.read_csv('fmMapProjects.csv')

fm22 = pd.read_csv('C:/Users/filip.stepniak/Projects/1_Project_Leviathan/map_csv/fmMapProjects_19-06-2018.csv')
print(len(fm22))
fm2 = fm22[fm22['suma']>2]
print(len(fm2))

fm1_hover_text = []
fm1_bubble_size = []
fm2_hover_text = []
fm2_bubble_size = []
gp2_hover_text = []
gp2_bubble_size = []

#fmMapPpl
for index, row in fm1.iterrows():
    fm1_hover_text.append(('City: {city}<br>'+
                      'Nr of Freelancers: {suma}<br>').
                      format(city=row['city'],
                             suma=row['suma']))
    fm1_bubble_size.append((row['suma']))

fm1['text'] = fm1_hover_text
fm1['size'] = fm1_bubble_size

trace0 = go.Scattergeo(
    name = 'FreeMap People',
    lon=fm1['longitude'],
    lat=fm1['latitude'],
    text=fm1['text'],
    hoverlabel=dict(
        font=dict(family='roboto',color='rgb(255, 255, 255)'),
        
        ),
    marker=dict(
        size=fm1['size']/5, 
        color ='rgb(168, 192, 70)',
        line=dict(color='rgb(168, 192, 70)', width=2),
        )
)
#fmMapProjects
for index, row in fm2.iterrows():
    fm2_hover_text.append(('City: {city}<br>'+
                      'Nr of Projects: {suma}<br>').
                      format(city=row['city'],
                             suma=row['suma']))
    fm2_bubble_size.append((row['suma']))

fm2['text'] = fm2_hover_text
fm2['size'] = fm2_bubble_size

trace1 = go.Scattergeo(
    name='FreeMap Projects',
    lon=fm2['longitude'],
    lat=fm2['latitude'],
    text=fm2['text'],
    hoverlabel=dict(
        font=dict(family='roboto',color='rgb(255, 255, 255)'),
        
        ),
    marker=dict(
        size=fm2['size']/5, 
        color ='rgb(72,86,27)',
        line=dict(color='rgb(72,86,27)', width=2), #darkgreen
        )
)
#gpMapProjects
for index, row in gp2.iterrows():
    gp2_hover_text.append(('City: {city}<br>'+
                      'Nr of Projects: {suma}<br>').
                      format(city=row['city'],
                             suma=row['suma']))
    gp2_bubble_size.append((row['suma']))

gp2['text'] = gp2_hover_text
gp2['size'] = gp2_bubble_size

trace2 = go.Scattergeo(
    name='Gulp Projects',
    lon=gp2['longitude'],
    lat=gp2['latitude'],
    text=gp2['text'],
    hoverlabel=dict(
        font=dict(family='roboto',color='rgb(255, 255, 255)'),
        
        ),
    marker=dict(
        size=gp2['size']/5, 
        color ='rgb(0,0,0)',
        line=dict(color='rgb(0,0,0)', width=2), #black
        )
)
#LAYOUT
data = [trace0,trace1,trace2]
layout = go.Layout(
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#E2E2E2',
        bordercolor='#FFFFFF',
        borderwidth=2
    ),
    autosize=False,
    width=1500,
    height=1200,
    title='Projects by city',
    geo = dict(
        resolution = 50,
        scope = 'europe',
        showframe = False,
        showcoastlines = True,
        showland = True,
        showcountries = True,
        landcolor = "rgb(87, 87, 86)",
        countrycolor = "rgb(255, 255, 255)" ,
        coastlinecolor = "rgb(255, 255, 255)",
        projection = dict(
            type = 'conic conformal'
        ),
        lonaxis = dict( range= [ 5.5, 15.3 ] ),
        lataxis = dict( range= [ 46.7, 55.0 ] ),
       
    )
)

fig = go.Figure(data=data, layout=layout)

offline.iplot(fig, filename='projectsByCity.html')

