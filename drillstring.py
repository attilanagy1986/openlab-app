import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from app import app


df_drillstring = pd.read_csv('Data/Drillstring/Volve_15_9_19_A_8_5.csv', sep=';', float_precision='round_trip')

page_layout = html.Div([
    html.H3(['Drillstring']),
    html.Div(id='dropdown-output', style={'paddingBottom': '10px', 'font-weight': 'bold', 'border-bottom': '1px solid black'}),
    html.Br(),
    dcc.Dropdown(
        options=[{'label':'8.5 in section', 'value':'8_5'}],
        placeholder = 'Select a hole section',
        id='drillstring-dropdown',
        style={'width':'50%'}
    ),
    html.Div(),
    html.Br(),
    html.Div(id='table-container', children=[
        dash_table.DataTable(
            id='drillstring-table',
            columns=[{'name': i, 'id': i} for i in df_drillstring.columns],
            data=df_drillstring.to_dict("rows"),
            style_header={'font-family': 'Calibri', 'font-weight': 'bold'},
            style_cell={'padding':'10px', 'font-family': 'Calibri', 'font-size': '16px'}
    )], style={'width':'50%', 'paddingTop':'25px'})
])


@app.callback(
    Output('drillstring-dropdown', 'options'),
    [Input('wells-dropdown', 'value')]
            )
def change_drillstring_dropdown(val):
    drillstring_dict = {
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
        drillstring_options = drillstring_dict[val]
        drillstring_options = list(reversed(drillstring_options))
        options=[{'label':str(drillstring_options[i])+' in section', 'value':str(drillstring_options[i]).replace('.', '_')} for i in range(len(drillstring_options))]
        return options


@app.callback(
    Output('drillstring-table', 'data'),
    [Input('wells-dropdown', 'value'), Input('drillstring-dropdown', 'value')]
)
def display_drillstring_table(val1, val2):
    df_drillstring = pd.read_csv(f'Data/Drillstring/Volve_{val1}_{val2}.csv', sep=';', float_precision='round_trip')
    data=df_drillstring.to_dict("rows")
    return data


@app.callback(
            Output('table-container', 'style'),
            [Input('drillstring-dropdown', 'value')]
            )
def hide_table(input):
    if input:
        return {'width':'50%'}
    else:
        return {'display':'none'}
