import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from app import app


def pressure_plot(df):
    trace0 = go.Scatter(
        x=df['Pore pressure (s.g.)'],
        y=[0 for num in df.index],
        mode='markers',
        marker = dict(
            color = 'rgb(0,0,0)',
            size = 0.01,
                    ),
        name='dummy_data',
        hoverinfo='none',
        showlegend=False,
    )

    trace1 = go.Scatter(
        x=df['Pore pressure (s.g.)'],
        y=df['TVD (m)'],
        mode='lines',
        line = dict(
            color = ('rgb(183,18,124)'),
            width = 2
                    ),
        name='Pore pressure',
        text=[
            "<b>TVD:</b> {} m<br>"
            "<b>Pore pressure:</b> {} s.g.<br>"
            "<b>Fracture pressure:</b> {} s.g.<br>"
            "<b>Pressure window:</b> {} s.g.<br>"
            .format(
                    df['TVD (m)'].loc[num],
                    df['Pore pressure (s.g.)'].loc[num],
                    df['Fracture pressure (s.g.)'].loc[num],
                    round(df['Fracture pressure (s.g.)'].loc[num]-df['Pore pressure (s.g.)'].loc[num], 3)
                    )
            for num in df.index
            ],
        hoverinfo="text",
        hoverlabel=dict(
                        bgcolor='rgb(255,255,255)',
                        bordercolor='rgb(0,0,0)'
                        ),
        showlegend=True,
    )

    trace2 = go.Scatter(
        x=df['Fracture pressure (s.g.)'],
        y=df['TVD (m)'],
        mode='lines',
        line = dict(
            color = ('rgb(0,115,172)'),
            width = 2
                    ),
        name='Fracture pressure',
        text=[
            "<b>TVD:</b> {} m<br>"
            "<b>Pore pressure:</b> {} s.g.<br>"
            "<b>Fracture pressure:</b> {} s.g.<br>"
            "<b>Pressure window:</b> {} s.g.<br>"
            .format(
                    df['TVD (m)'].loc[num],
                    df['Pore pressure (s.g.)'].loc[num],
                    df['Fracture pressure (s.g.)'].loc[num],
                    round(df['Fracture pressure (s.g.)'].loc[num]-df['Pore pressure (s.g.)'].loc[num], 3)
                    )
            for num in df.index
            ],
        hoverinfo="text",
        hoverlabel=dict(
                        bgcolor='rgb(255,255,255)',
                        bordercolor='rgb(0,0,0)'
                        ),
        showlegend=True,
    )
    data = [trace0,trace1,trace2]
    layout = go.Layout(
                    title=None,
                    height = 550,
                    width = 800,
                    margin=dict(t=25, pad=0),
                    autosize = False,
                    xaxis=dict(
                        title='<b>Pressure<br>(s.g.)</b>',
                        range=[0.8, 2.0]
                            ),
                    yaxis=dict(
                        title='<b>TVD<br>(m)</b>',
                        autorange='reversed'),
                    legend=dict(x=0, y=-0.3),
                    hovermode='closest'
                        )
    fig = go.Figure(data=data,layout=layout)
    return fig

df_geopressures = pd.read_csv(f'Data/Geopressures/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

page_layout = html.Div([
    html.H3(['Geopressures']),
    html.Div(id='dropdown-output', style={'paddingBottom': '10px', 'border-bottom': '1px solid black', 'font-weight': 'bold'}),
    html.Br(),
    html.Div(
        id='geopressures',
        children=[
            html.Div(children=[
                html.Div(dcc.Graph(
                    id='geopressures-graph',
                    figure=pressure_plot(df_geopressures),
                    config=dict(displayModeBar=False)
                            ), style={'display': 'inline-block', 'float': 'left', 'border-right': '1px solid black'}),
                html.Div(children=[
                    dash_table.DataTable(
                        id='geopressures-table',
                        columns=[
                            {"name": 'TVD (m)', "id": 'TVD (m)'},
                            {"name": 'Pore pressure (s.g.)', "id": 'Pore pressure (s.g.)'},
                            {"name": 'Fracture pressure (s.g.)', "id": 'Fracture pressure (s.g.)'}
                                ],
                        n_fixed_rows=1,
                        data=df_geopressures.to_dict("rows"),
                        style_header={'font-family': 'Calibri', 'font-weight': 'bold'},
                        style_cell={'padding':'10px', 'font-family': 'Calibri', 'font-size': '16px'},
                        style_cell_conditional=[
                            {'if': {'column_id': 'TVD (m)'},
                             'width': '100px'},
                            {'if': {'column_id': 'Pore pressure (s.g.)'},
                             'width': '175px'},
                            {'if': {'column_id': 'Fracture pressure (s.g.)'},
                             'width': '175px'},
])], style={'display': 'inline-block', 'paddingTop': '50px', 'paddingLeft': '150px'})
])])])


@app.callback(
    Output('geopressures-table', 'data'),
    [Input('wells-dropdown', 'value')]
            )
def display_geopressures_table(val):
    df_geopressures = pd.read_csv(f'Data/Geopressures/Volve_{val}.csv', sep=';', float_precision='round_trip')
    data=df_geopressures.to_dict("rows")
    return data


@app.callback(
    Output('geopressures-graph', 'figure'),
    [Input('wells-dropdown', 'value')]
            )
def display_geopressures_graph(val):
    df_geopressures = pd.read_csv(f'Data/Geopressures/Volve_{val}.csv', sep=';', float_precision='round_trip')
    return pressure_plot(df_geopressures)
