import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import json
import openlab

from app import app

#wellbores for dropdown selection
well_dict = {
            '15_9_19_A': '15/9-19 A',
            '15_9_19_B': '15/9-19 B',
            '15_9_19_BT2': '15/9-19 BT2',
            '15_9_19_S': '15/9-19 S',
            '15_9_19_SR': '15/9-19 SR',
            '15_9_F_1': '15/9-F-1',
            '15_9_F_1_A': '15/9-F-1 A',
            '15_9_F_1_B': '15/9-F-1 B',
            '15_9_F_1_C': '15/9-F-1 C',
            '15_9_F_4': '15/9-F-4',
            '15_9_F_5': '15/9-F-5',
            '15_9_F_7': '15/9-F-7',
            '15_9_F_9': '15/9-F-9',
            '15_9_F_9_A': '15/9-F-9 A',
            '15_9_F_10': '15/9-F-10',
            '15_9_F_11': '15/9-F-11',
            '15_9_F_11_A': '15/9-F11 A',
            '15_9_F_11_B': '15/9-F-11 B',
            '15_9_F_12': '15/9-F-12',
            '15_9_F_14': '15/9-F-14',
            '15_9_F_15': '15/9-F-15',
            '15_9_F_15_A': '15/9-F-15 A',
            '15_9_F_15_B': '15/9-F-15 B',
            '15_9_F_15_C': '15/9-F-15 C',
            '15_9_F_15_D': '15/9-F-15 D'
            }

#define openlab page layout
page_layout = html.Div([
    html.H3(['Create a well configuration in OpenLab Drilling Simulator']),
    html.Div(['Choose a wellbore and a hole section'], style={'paddingBottom':'10px'}),
    dcc.Dropdown(
        options=[{'label':value, 'value':key} for key, value in well_dict.items()],
        placeholder = 'Select a wellbore',
        id='wellbore-dropdown',
        style={'width':'50%'}
    ),
    html.Br(),
    dcc.Dropdown(
        placeholder = 'Select a hole section',
        id='section-dropdown',
        style={'width':'50%'}),
    html.Br(),
    html.Div(["Generate Python login script in OpenLab Web Client\Account\Settings"], style={'paddingBottom':'10px'}),
    dcc.Textarea(
        id='text-input',
        placeholder='Paste here the Python login script\nusername="string"\napikey="string"\nlicenseguid="string"',
        rows=4,
        style={'width': '55%'}),
    html.Br(),
    html.Div(
        html.Button(
            children='Create configuration',
            id='create-button',
            n_clicks=0,
            style={
                'font-size': '14px',
                'border-radius':'2px',
                'padding':'5px',
                'cursor': 'pointer'}
    ), style={'paddingTop':'10px'}),
    html.Div(id='text-output')
])

#update hole section dropdown according to wellbore selection
@app.callback(
    Output('section-dropdown', 'options'),
    [Input('wellbore-dropdown', 'value')]
            )
def change_section_dropdown(val):
    section_dict = {
        '15_9_19_A': [8.5],
        '15_9_19_B': [8.5],
        '15_9_19_BT2': [6, 8.5],
        '15_9_19_S': [12.25, 17.5],
        '15_9_19_SR': [8.5, 12.25],
        '15_9_F_1': [8.5, 17.5],
        '15_9_F_1_A': [8.5],
        '15_9_F_1_B': [8.5, 12.25],
        '15_9_F_1_C': [8.5, 12.25, 17.5],
        '15_9_F_4': [8.5, 12.25],
        '15_9_F_5': [8.5, 12.25],
        '15_9_F_7': [12.25],
        '15_9_F_9': [12.25],
        '15_9_F_9_A': [8.5, 12.25],
        '15_9_F_10': [8.5, 12.25, 17.5],
        '15_9_F_11': [8.5, 17.5],
        '15_9_F_11_A': [8.5],
        '15_9_F_11_B': [8.5, 12.25],
        '15_9_F_12': [8.5, 12.25, 17.5],
        '15_9_F_14': [8.5, 12.25, 17.5],
        '15_9_F_15': [8.5, 12.25],
        '15_9_F_15_A': [8.5, 17.5],
        '15_9_F_15_B': [8.5],
        '15_9_F_15_C': [8.5, 12.25],
        '15_9_F_15_D': [8.5, 12.25, 17.5]
    }
    if val:
        section_options = section_dict[val]
        section_options = list(reversed(section_options))
        options=[{'label':str(section_options[i])+' in section', 'value':str(section_options[i]).replace('.', '_')} for i in range(len(section_options))]
        return options

#create configuration in OpenLab
@app.callback(
    Output('text-output', 'children'),
    [Input('create-button', 'n_clicks')],
    [
    State('text-input', 'value'),
    State('wellbore-dropdown', 'value'),
    State('section-dropdown', 'value')]
)
def create_config(n_clicks, val, wellbore, section):
    if (val and wellbore and section):
        input_text = val
        input_text.strip()
        text = input_text.split()
        username = text[0][text[0].find('=')+2:-1]
        apikey = text[1][text[1].find('=')+2:-1]
        licenseguid = text[2][text[2].find('=')+2:-1]

        session = openlab.http_client(username=username,apikey=apikey,licenseguid=licenseguid)
        with open(f'Configurations/{wellbore}_section_{section}.json', 'r') as f:
            data = json.load(f)

        new_config = session.create_configuration(f'{wellbore}_section_{section}', data['Data'])
