#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:59:18 2020

@author: marshall132
"""

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import plotly
# import plotly.plotly as py
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)

### READ IN ALL NECCESSARY DATAFRAME FILES

shots = pd.read_csv('shots.csv')
shots['GAME_ID'] = shots['GAME_ID'].astype(str)

merged_2 = pd.read_csv('merged_2.csv')

cluster_17_merged = pd.read_csv('cluster_17_merged.csv')
cluster_18_merged = pd.read_csv('cluster_18_merged.csv')
cluster_19_merged = pd.read_csv('cluster_19_merged.csv')

def ellipse_arc(x_center=0, y_center=0, a=1, b =1, start_angle=0, end_angle=2*np.pi, N=100, closed= False):
    t = np.linspace(start_angle, end_angle, N)
    x = x_center + a*np.cos(t)
    y = y_center + b*np.sin(t)
    path = f'M {x[0]}, {y[0]}'
    for k in range(1, len(t)):
        path += f'L{x[k]}, {y[k]}'
    if closed:
        path += ' Z'
    return path  

court_shapes =[go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            x0=-7.5,
            y0=-7.5,
            x1=7.5,
            y1=7.5,
            line_color="Black",
        ),
            go.layout.Shape(
            type="rect",
            x0=-30,
            y0=-7.5,
            x1=30,
            y1=-7.5,
            line_color="Black"),
            
            go.layout.Shape(
            type="rect",
            x0=-80,
            y0=-47.5,
            x1=80,
            y1=142.5,
            line_color="Black"),
             
            go.layout.Shape(
            type="rect",
            x0=-60,
            y0=-47.5,
            x1=60,
            y1=142.5,
            line_color="Black"),
               
            dict(type="path",
            path= ellipse_arc(y_center= 140, a=60, b=60, start_angle=0, end_angle=3*np.pi/3, N=100),
            line_color="Black"),
               
            dict(type="path",
            path= ellipse_arc(y_center= 140, a=60, b=60, start_angle=0, end_angle=-3*np.pi/3, N=100),
            line_color="Black"),
               
            go.layout.Shape(
            type="rect",
            x0=-220,
            y0=-47.5,
            x1=-220,
            y1=92.5,
            line_color="Black"),  
            
            go.layout.Shape(
            type="rect",
            x0=220,
            y0=-47.5,
            x1=220,
            y1=92.5,
            line_color="Black"),
                
            
            dict(type="path",
            path= ellipse_arc(y_center= 92.5, a=220, b=146.5, start_angle=0, end_angle=3*np.pi/3, N=100),
            line_color="Black"),
                
            go.layout.Shape(
            type="rect",
            x0=-250,
            y0=-47.5,
            x1=250,
            y1=422.5,
            line_color="Black"),
             
            dict(type="path",
            path= ellipse_arc(a=40, b=40, start_angle=0, end_angle=3*np.pi/3, N=100),
            line_color="Black"),
                
            dict(type="path",
            path= ellipse_arc(y_center= 422.5, a=60, b=60, start_angle=0, end_angle=-3*np.pi/3, N=100),
            line_color="Black"),
            
            dict(type="path",
            path= ellipse_arc(y_center= 422.5, a=20, b=20, start_angle=0, end_angle=-3*np.pi/3, N=100),
            line_color="Black"),   
               ]  


def shot_chart(name, year=''):    
    if year:
        year_clean = '00' + year[0] + year[2:]
        player = shots[(shots.PLAYER_NAME == name) & (shots['GAME_ID'].str.contains(year_clean))]
    else:
        player= shots[shots.PLAYER_NAME == name]

    missed_shot_trace = go.Scattergl(
            x = player[player.SHOT_MADE_FLAG == 0]['LOC_X'],
            y = player[player.SHOT_MADE_FLAG == 0]['LOC_Y'],
            mode = 'markers',
            name = 'Miss',
            marker= dict(color='blue', symbol='x', size=8, line={'width':1}, opacity=0.7),
            text = [str(sd) for sd in player[player.SHOT_MADE_FLAG == 0]['ACTION_TYPE']],
            hoverinfo = 'text'
        )
    made_shot_trace = go.Scattergl(
        x = player[player.SHOT_MADE_FLAG == 1]['LOC_X'],
        y = player[player.SHOT_MADE_FLAG == 1]['LOC_Y'],
        mode = 'markers',
        name='Make',
        marker= dict(color='red', symbol='circle', size=8, line={'width':1}, opacity=0.7),
        text = [str(sd) for sd in player[player.SHOT_MADE_FLAG == 1]['ACTION_TYPE']],
        hoverinfo = 'text'
    )

    
   
    data = [missed_shot_trace, made_shot_trace]
    layout = go.Layout(
        title= name + ' Shot Chart ' + year,
        showlegend =True,
        xaxis={'showgrid':False, 'range':[-250,250]},
        yaxis={'showgrid':False, 'range':[422.5,-47.5]},
        height = 600,
        width = 650,
        shapes=court_shapes)

    fig = go.Figure(data=data, layout=layout)
    return fig


st.title('NBA Shot Breakdown')

st.plotly_chart(shot_chart('Ben Simmons', year='2017'))



