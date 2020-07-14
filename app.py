#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:04:19 2020

@author: ving2000
"""

import pandas as pd
import numpy as np

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table 
import plotly.graph_objects as go
import os

import base64


from sklearn.tree import DecisionTreeClassifier

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css?__cf_chl_jschl_tk__=8c34fbabd7a9065a2b15ccb7c0f4a8e1f7095423-1594745469-0-ATyghI11j64_82dCIfkBR6U9lEAJQ2JIp6hIV-3pywwLe01_vRFfF7UV4nmYpuYUgr3ZdPsAULX-fg0ASgb38W9nc5Nm0bcjx2uQrtCAsebPe3BeP0paFRFQHpQRitUZ-J1KnH17SOLAMrctw2p6taQFqiTTbW8VXkO9ed68sCRpQzBce1U9mNTcl0CFLaVULXEGAz_ryWHgVjoXDionOpxFJv_Uy6aOS4pwbgwrFBlKyWTDnLewwwT3P2uLVCdbsfg4w4pBONc9SDylGz_uDxEVNJ_3rEpmLMcdi9RREkXrHnlegjqgZ-pRcPsHrvAS08JJz6_cVPu3rEdm1oKWjl1y3AMq5KvhlgbYSMPuwzJ8']

# external_stylesheets=[dbc.themes.BOOTSTRAP]) 

app = dash.Dash(__name__,  external_stylesheets=external_stylesheets)
server = app.server

df = pd.read_excel('job_quiz.xlsx')
mix_df = pd.read_csv('Random_df.csv', index_col = 0)
des_df = pd.read_excel('job_field_desc.xlsx')

y = df['Label']
x = df.drop(['Label'], axis = 1)

num_dict = []

for col in x.columns:
    
    local_dict = {}
    for answer in x[col].unique():
        
        ind = x[col].unique().tolist().index(answer)
        local_dict[ind] = answer

    num_dict.append(local_dict)

num_dict


new_x = pd.concat((x, mix_df.drop(['Label'], axis = 1)), axis = 0)
new_x['Education'].replace('no', 'None', inplace=True)
new_x['Interest'].replace(['travel', 'entrepreneur'], ['traveling', 'entrepreneurship'], inplace=True)
new_y = pd.concat((y, mix_df['Label']))

# ---------------------------------------------    

def Encode (df, key_dict):

    columns = df.columns

    for col in range(len(columns)):
        temp = [code for entry in df[columns[col]] for code, name in key_dict[col].items()  if name == entry]
        df[columns[col]] = temp

def Format_Dash (key_dict, ind):
    options = []
    for code, name in key_dict[ind].items():
        options.append(dict(label=name, value = code))
    return options

# ----------------------------------------------

Encode(new_x, num_dict)


tree_clf = DecisionTreeClassifier()
tree_clf.fit(new_x, new_y)

image_filename = os.path.join(os.getcwd(), 'cropped-tco-logo-gigkoala_2-4-1.png')
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


# ---------------------------------------------------------------------------
 
app.layout = html.Div(
    [
        html.Div([
         html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style = {'height': '15%',
                'width': '15%'})
         ], style = {'textAlign': 'center'}),
         
         html.H1("WHAT CAREER FIELD IS RIGHT FOR YOU?", style={'text-align': 'center', 
                                            'font-family': 'Times New Roman, serif',
                                            'fontWeight': 'bold', 'color': 'crimson'}),
         
         html.H6('Answer these 9 questions to find out where your skills are most needed!',
                 style = {'text-align': 'center'}),
         
       html.H6('-------', style = {'text-align': 'center'}),
         
        html.Div([
         
         html.Br(), 
         html.Label("1. What interest would you like to see applied on the job?", 
                    style = {'fontWeight': 'bold'}),
         dcc.RadioItems(
            options=Format_Dash(num_dict, 0),
            value=None,
            id="ans1"
        ),
        
        html.Br(),
        html.Label("2. Do you have clean driving record?",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 1),
            value=None,
            id="ans2"
        ),
        
        html.Br(),
        html.Label("3. Which of the following best describes your education level.",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 2),
            value=None,
            id="ans3",
        ),
        
        html.Br(),
        html.Label("4. What is one of your skills that you think would make you a valuable asset to future employers?",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 3),
            value=None,
            id="ans4",
        ),
        
        html.Br(),
        html.Label("5. What would you tell employers as your most marketable trait?",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 4),
            value=None,
            id="ans5",
        ),
        
        html.Br(),
        html.Label("6. Do you consider yourself as someone who can go through phases of trial-and-error?",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 5),
            value=None,
            id="ans6",
        ),
        
        html.Br(),
        html.Label("7. What is your usual role in a group setting?",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 6),
            value=None,
            id="ans7",
        ),
        
        html.Br(),
        html.Label("8. Do you enjoy working outdoors?",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 7),
            value=None,
            id="ans8",
        ),
        
        html.Br(),
        html.Label("9. Do you see yourself as someone who serves others?",
                   style = {'fontWeight': 'bold'}),
        dcc.RadioItems(
            options=Format_Dash(num_dict, 8),
            value=None,
            id="ans9",
        ),
        
        html.Br(),
        
        html.Button('Submit', id='button', style = {'backgroundColor': 'black', 'color': 'white'}),
        html.Label('Hit Submit and Scroll Down to View Results')
        
        ], style={'width':'100%', 'margin':70, 'text-align': 'left'}),
        
        html.Br(),
        html.Div(id = 'results')
        
    ]
)



@app.callback(
    Output(component_id='results', component_property='children'),

    [Input(component_id='button', component_property='n_clicks'),
     Input(component_id='ans1', component_property='value'),
     Input(component_id='ans2', component_property='value'),
     Input(component_id='ans3', component_property='value'),
     Input(component_id='ans4', component_property='value'),
     Input(component_id='ans5', component_property='value'),
     Input(component_id='ans6', component_property='value'),
     Input(component_id='ans7', component_property='value'),
     Input(component_id='ans8', component_property='value'),
     Input(component_id='ans9', component_property='value')
     
   ]
)

def return_field (n_clicks, ques1, ques2, ques3, ques4, ques5, ques6, ques7, ques8, ques9):
    
   if n_clicks!=None:
    
       df = pd.DataFrame([[ques1, ques2, ques3, ques4, ques5, ques6, ques7, ques8, ques9]], 
                             columns = new_x.columns.to_list())
       res = tree_clf.predict(df)
       
       field = des_df[des_df['Field'] == res[0]]
       ind = field.index[0]
       resq = field['Requirements'][ind].split('. ')
       resp = field['Responsibilities'][ind].split('. ')
       
       
       return html.Div([
           html.H3('RESULTS', style = {'text-align': 'center',
                                       'backgroundColor' : 'wheat',
                                       'border': '4px black solid'}), 
           html.Br(),
           html.Label('Your most fitted gig field is ', style = {'text-align': 'center'}),
           html.H4(res[0].upper(), style = {'color': 'crimson', 'fontWeight': 'bold', 'text-align': 'center'}),
           
           html.Div([
           
           html.Div([
               html.Label('Basic Requirements', style = {'fontWeight': 'bold', 'font-size': '30px',
                                                     }),
               html.Ul([html.Li(x) for x in resq])
               ], style = {'width':'100%', 'margin':20, 'text-align': 'left'}),
                           
           html.Div([     
                       
           
           html.Label('General Responsibilities', style = {'fontWeight': 'bold', 'font-size': '30px',
                                                    }),
           html.Ul([html.Li(x) for x in resp])
           
          ] , style = {'width':'100%', 'margin':20, 'text-align': 'left'
                       })
                       
            ], style = {'backgroundColor': '#C9FBE5'}),
                       
           html.Label('Source: {}'.format(field['Source'][ind]), style = {'text-align': 'right', 'font-style': 'italic'}),
           
           html.Div([
           
           html.Label(['Check out hiring employers in ', 
                       html.A(res[0], href=field['Link'][ind])], style = {'font-size': '25px', 
                                                                          'text-align': 'center'}),
           
           html.Label(['Subscribe to ',
                       html.A('GigKoala', href='https://gigkoala.com'),
                       ' to receive our ',
                       html.A('Weekly Newsletters', href = 'https://gigkoala.com/2020/06/22/newsletter-attachment/'),
                       ' sent to your email!'], style = {'font-size': '25px',
                                                         'text-align': 'center'})
           ], style = {'margin':30})
                                                         
           ])
                                
                     





if __name__ == '__main__':
    app.run_server(debug=True)

