import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from app import app

#function to create wellpath plot
def wellpath_plot(df):
    x=df['N/S (m)'].max()-df['N/S (m)'].min()
    y=df['E/W (m)'].max()-df['E/W (m)'].min()
    z=df['TVD (m RKB)'].max()-df['TVD (m RKB)'].min()
    trace0 = go.Scatter3d(
        x=df['N/S (m)'],
        y=df['E/W (m)'],
        z=df['TVD (m RKB)'],
        mode='lines',
        line=dict(
            color='rgb(211,211,211)',
            width=20
        ),
        hoverinfo='none',
        showlegend=False
    )

    trace1 = go.Scatter3d(
        x=df[df['DLS (deg/30m)']<2]['N/S (m)'],
        y=df[df['DLS (deg/30m)']<2]['E/W (m)'],
        z=df[df['DLS (deg/30m)']<2]['TVD (m RKB)'],
        mode='markers',
        marker=dict(
            color='rgb(128,196,196)',
            size=5
        ),
        name='DLS (°/30m): < 2',
        text = [
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                "<b>Inclination:</b> {} °<br>"
                "<b>Azimuth:</b> {} °<br>"
                "<b>DLS:</b> {} °/30m"
                .format(
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        df['Inc (deg)'].loc[i],
                        df['Azim (deg)'].loc[i],
                        df['DLS (deg/30m)'].loc[i]
                        )
                for i in df[df['DLS (deg/30m)']<2].index],
        hoverinfo='text'
    )

    trace2 = go.Scatter3d(
        x=df[(df['DLS (deg/30m)']>=2)&(df['DLS (deg/30m)']<4)]['N/S (m)'],
        y=df[(df['DLS (deg/30m)']>=2)&(df['DLS (deg/30m)']<4)]['E/W (m)'],
        z=df[(df['DLS (deg/30m)']>=2)&(df['DLS (deg/30m)']<4)]['TVD (m RKB)'],
        mode='markers',
        marker=dict(
            color='rgb(0,115,172)',
            size=5
        ),
        name='DLS (°/30m): 2-4',
        text = [
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                "<b>Inclination:</b> {} °<br>"
                "<b>Azimuth:</b> {} °<br>"
                "<b>DLS:</b> {} °/30m"
                .format(
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        df['Inc (deg)'].loc[i],
                        df['Azim (deg)'].loc[i],
                        df['DLS (deg/30m)'].loc[i]
                        )
                for i in df[(df['DLS (deg/30m)']>=2)&(df['DLS (deg/30m)']<4)].index],
        hoverinfo='text'
    )

    trace3 = go.Scatter3d(
        x=df[(df['DLS (deg/30m)']>=4)&(df['DLS (deg/30m)']<6)]['N/S (m)'],
        y=df[(df['DLS (deg/30m)']>=4)&(df['DLS (deg/30m)']<6)]['E/W (m)'],
        z=df[(df['DLS (deg/30m)']>=4)&(df['DLS (deg/30m)']<6)]['TVD (m RKB)'],
        mode='markers',
        marker=dict(
            color='rgb(120,123,194)',
            size=5
        ),
        name='DLS (°/30m): 4-6',
        text = [
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                "<b>Inclination:</b> {} °<br>"
                "<b>Azimuth:</b> {} °<br>"
                "<b>DLS:</b> {} °/30m"
                .format(
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        df['Inc (deg)'].loc[i],
                        df['Azim (deg)'].loc[i],
                        df['DLS (deg/30m)'].loc[i]
                        )
                for i in df[(df['DLS (deg/30m)']>=4)&(df['DLS (deg/30m)']<6)].index],
        hoverinfo='text'
    )

    trace4 = go.Scatter3d(
        x=df[(df['DLS (deg/30m)']>=6)&(df['DLS (deg/30m)']<8)]['N/S (m)'],
        y=df[(df['DLS (deg/30m)']>=6)&(df['DLS (deg/30m)']<8)]['E/W (m)'],
        z=df[(df['DLS (deg/30m)']>=6)&(df['DLS (deg/30m)']<8)]['TVD (m RKB)'],
        mode='markers',
        marker=dict(
            color='rgb(183,18,124)',
            size=5
        ),
        name='DLS (°/30m): 6-8',
        text = [
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                "<b>Inclination:</b> {} °<br>"
                "<b>Azimuth:</b> {} °<br>"
                "<b>DLS:</b> {} °/30m"
                .format(
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        df['Inc (deg)'].loc[i],
                        df['Azim (deg)'].loc[i],
                        df['DLS (deg/30m)'].loc[i]
                        )
                for i in df[(df['DLS (deg/30m)']>=6)&(df['DLS (deg/30m)']<8)].index],
        hoverinfo='text'
    )

    trace5 = go.Scatter3d(
        x=df[df['DLS (deg/30m)']>8]['N/S (m)'],
        y=df[df['DLS (deg/30m)']>8]['E/W (m)'],
        z=df[df['DLS (deg/30m)']>8]['TVD (m RKB)'],
        mode='markers',
        marker=dict(
            color='rgb(204,19,51)',
            size=5
        ),
        name='DLS (°/30m): > 8',
        text = [
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                "<b>Inclination:</b> {} °<br>"
                "<b>Azimuth:</b> {} °<br>"
                "<b>DLS:</b> {} °/30m"
                .format(
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        df['Inc (deg)'].loc[i],
                        df['Azim (deg)'].loc[i],
                        df['DLS (deg/30m)'].loc[i]
                        )
                for i in df[df['DLS (deg/30m)']>8].index],
        hoverinfo='text'
    )

    data = [trace0,trace1,trace2,trace3,trace4,trace5]

    layout = dict(
        width=900,
        height=800,
        margin=dict(t=0,b=0, pad=0),
        autosize=False,
        legend=dict(x=1,y=0.85),
        hoverlabel=dict(
                        bgcolor='rgb(255,255,255)',
                        bordercolor='rgb(0,0,0)'
                        ),
        hovermode='closest',
        scene=dict(
            xaxis=dict(
                title='<b>Northing (m)</b>',
                gridcolor='rgb(169,169,169)',
                zerolinecolor='rgb(169,169,169)',
                showbackground=True,
                backgroundcolor='rgb(255,255,255)',
                showspikes=False
            ),
            yaxis=dict(
                title='<b>Easting (m)</b>',
                gridcolor='rgb(169,169,169)',
                zerolinecolor='rgb(169,169,169)',
                showbackground=True,
                backgroundcolor='rgb(255,255,255)',
                showspikes=False
            ),
            zaxis=dict(
                title='<b>Depth (m)</b>',
                gridcolor='rgb(169,169,169)',
                zerolinecolor='rgb(169,169,169)',
                showbackground=True,
                backgroundcolor='rgb(255,255,255)',
                showspikes=False,
                autorange='reversed'
            ),
            camera=dict(
                up=dict(
                    x=0,
                    y=0,
                    z=1
                ),
                eye=dict(
                    x=-1.25,
                    y=1.25,
                    z=0.5,
                )
            ),
            aspectratio = dict(x=x/z, y=y/z, z=1),
            aspectmode = 'manual'
        )
    )
    fig = dict(data=data, layout=layout)
    return fig

#default wellbore
df_survey = pd.read_csv(f'Data/Wellpath/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

#define wellpath page layout and content
page_layout = html.Div([
    html.H3(['Wellpath']),
    html.Div(id='dropdown-output', style={'paddingBottom': '10px', 'border-bottom': '1px solid black', 'font-weight': 'bold'}),
    html.Br(),
    html.Div(
        id='wellpath',
        children=[
            html.Div(dcc.Graph(
                id='wellpath-graph',
                figure=wellpath_plot(df_survey),
                config=dict(displayModeBar=False)
                        ), style={'display': 'inline-block', 'float': 'left', 'paddingRight': '10px', 'border-right': '1px solid black'}),
            html.Div(children=[
                html.Br(),
                dash_table.DataTable(
                    id='wellpath-table',
                    columns=[
                        {"name": 'MD (m RKB)', "id": 'MD (m RKB)'},
                        {"name": 'Inc. (°)', "id": 'Inc (deg)'},
                        {"name": 'Azimuth (°)', "id": 'Azim (deg)'},
                        {"name": 'TVD (m RKB)', "id": 'TVD (m RKB)'},
                        {"name": 'DLS (°/30m)', "id": 'DLS (deg/30m)'}
                            ],
                    n_fixed_rows=1,
                    data=df_survey[['MD (m RKB)', 'Inc (deg)', 'Azim (deg)', 'TVD (m RKB)', 'DLS (deg/30m)']].to_dict("rows"),
                    style_header={'font-family': 'Calibri', 'font-weight': 'bold'},
                    style_cell={'padding':'10px', 'font-family': 'Calibri', 'font-size': '16px', 'width': '100px'}
                                            )], style={'display': 'inline-block', 'paddingTop': '100px', 'paddingLeft': '25px'})
                ]
            )
])

#callback to update table according to wellbore selection
@app.callback(
    Output('wellpath-table', 'data'),
    [Input('wells-dropdown', 'value')]
            )
def display_wellpath_table(val):
    df_survey = pd.read_csv(f'Data/Wellpath/Volve_{val}.csv', sep=';', float_precision='round_trip')
    data=df_survey[['MD (m RKB)', 'Inc (deg)', 'Azim (deg)', 'TVD (m RKB)', 'DLS (deg/30m)']].to_dict("rows")
    return data

#callback to update plot according to wellbore selection
@app.callback(
    Output('wellpath-graph', 'figure'),
    [Input('wells-dropdown', 'value')]
            )
def display_wellpath_graph(val):
    df_survey = pd.read_csv(f'Data/Wellpath/Volve_{val}.csv', sep=';', float_precision='round_trip')
    return wellpath_plot(df_survey)
