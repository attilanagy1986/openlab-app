import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from app import app


def temp_plot(df):
    trace1 = go.Scatter(
        x=df['Temperature (degC)'],
        y=df['TVD (m)'],
        mode='lines',
        line = dict(
            color = ('rgb(0,115,172)'),
            width = 2
                    ),
        name='Temperature gradient',
        text=[
            "<b>TVD:</b> {} m<br>"
            "<b>Temperature:</b> {} °C<br>"
            "<b>Medium:</b> {}<br>"
            .format(
                    df['TVD (m)'].loc[num],
                    df['Temperature (degC)'].loc[num],
                    df['Medium'].loc[num]
                    )
            for num in df.index
            ],
        hoverinfo="text",
        hoverlabel=dict(
                        bgcolor='rgb(255,255,255)',
                        bordercolor='rgb(0,0,0)'
                        ),
        showlegend=False
    )
    data = [trace1]
    layout = go.Layout(
                    title=None,
                    height = 550,
                    width = 800,
                    margin=dict(t=25, pad=0),
                    autosize = False,
                    xaxis=dict(
                        title='<b>Temperature<br>(°C)</b>',
                        range=[0, 130]
                            ),
                    yaxis=dict(
                        title='<b>TVD<br>(m)</b>',
                        autorange='reversed'),
                    hovermode='closest'
                        )

    fig = go.Figure(data=data,layout=layout)
    return fig

df_geothermal = pd.read_csv(f'Data/Geothermal/Plot/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')
df_geothermal_table = pd.read_csv(f'Data/Geothermal/Table/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

page_layout = html.Div([
    html.H3(['Geothermal']),
    html.Div(id='dropdown-output', style={'paddingBottom': '10px', 'border-bottom': '1px solid black', 'font-weight': 'bold'}),
    html.Br(),
    html.Div(
        id='geothermal',
        children=[
            html.Div(children=[
                html.Div(dcc.Graph(
                    id='geothermal-graph',
                    figure=temp_plot(df_geothermal),
                    config=dict(displayModeBar=False)
                            ), style={'display': 'inline-block', 'float': 'left', 'border-right': '1px solid black'}),
                html.Div(dash_table.DataTable(
                    id='geothermal-table',
                    columns=[
                        {"name": 'Medium', "id": 'Medium'},
                        {"name": 'From TVD (m)', "id": 'From TVD (m)'},
                        {"name": 'Temp. gradient (°C/100m)', "id": 'Temp. gradient (°C/100m)'}
                            ],
                    data=df_geothermal_table.to_dict("rows"),
                    style_header={'font-family': 'Calibri', 'font-weight': 'bold'},
                    style_cell={'padding':'10px', 'font-family': 'Calibri', 'font-size': '16px'}
                                            ), style={'display': 'inline-block', 'paddingTop': '50px', 'paddingLeft': '150px'})])
                ]
            )
])


@app.callback(
    Output('geothermal-table', 'data'),
    [Input('wells-dropdown', 'value')]
            )
def display_geothermal_table(val):
    df_geothermal_table = pd.read_csv(f'Data/Geothermal/Table/Volve_{val}.csv', sep=';', float_precision='round_trip')
    data=df_geothermal_table.to_dict("rows")
    return data


@app.callback(
    Output('geothermal-graph', 'figure'),
    [Input('wells-dropdown', 'value')]
            )
def display_geothermal_graph(val):
    df_geothermal = pd.read_csv(f'Data/Geothermal/Plot/Volve_{val}.csv', sep=';', float_precision='round_trip')
    return temp_plot(df_geothermal)
