import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from app import app


df_fluid = pd.read_csv('Data/Fluid/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

page_layout = html.Div([
    html.H3(['Fluid']),
    html.Div(id='dropdown-output', style={'paddingBottom': '10px', 'border-bottom': '1px solid black', 'font-weight': 'bold'}),
    html.Br(),
    html.Div([
            dash_table.DataTable(
                id='fluid-table',
                columns=[{"name": i, "id": i} for i in df_fluid.columns],
                data=df_fluid.to_dict("rows"),
                style_header={'font-family': 'Calibri', 'font-weight': 'bold'},
                style_cell={'padding':'10px', 'font-family': 'Calibri', 'font-size': '16px'}
    )], style={'paddingTop': '10px', 'width':'50%'})
])

@app.callback(
    Output('fluid-table', 'data'),
    [Input('wells-dropdown', 'value')]
            )
def display_fluid_table(val):
    df_fluid = pd.read_csv(f'Data/Fluid/Volve_{val}.csv', sep=';', float_precision='round_trip')
    data=df_fluid.to_dict("rows")
    return data
