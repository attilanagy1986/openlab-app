#single bundle of all the scripts
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go
import pandas as pd
import json
import openlab


external_stylesheets = ['https://cdn.jsdelivr.net/gh/attilanagy1986/Dash-css@master/undo.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Openlab app'
server = app.server
app.config.suppress_callback_exceptions = True


wells_dict = {
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

app.layout = html.Div([
    dcc.Location(id='url'),
    dcc.Link(
            'Wells',
            href='/wells',
            style={
                'color': 'rgb(0,0,0)',
                'font-size': '17px',
                'font-weight': 'bold'
                }),
    dcc.Link(
            'Hole section',
            href='/hole_section',
            style={
                'color': 'rgb(0,0,0)',
                'font-size': '17px',
                'font-weight': 'bold',
                'paddingLeft':'25px'
                }),
    dcc.Link(
            'Wellpath',
            href='/wellpath',
            style={
                'color': 'rgb(0,0,0)',
                'font-size': '17px',
                'font-weight': 'bold',
                'paddingLeft':'25px'
                }),
    dcc.Link(
            'Fluid',
            href='/fluid',
            style={
                'color': 'rgb(0,0,0)',
                'font-size': '17px',
                'font-weight': 'bold',
                'paddingLeft':'25px'
                }),
    dcc.Link(
            'Drillstring',
            href='/drillstring',
            style={
                'color': 'rgb(0,0,0)',
                'font-size': '17px',
                'font-weight': 'bold',
                'paddingLeft':'25px'
                }),
    dcc.Link(
            'Geopressures',
            href='/geopressures',
            style={
                'color': 'rgb(0,0,0)',
                'font-size': '17px',
                'font-weight': 'bold',
                'paddingLeft':'25px'
                }),
    dcc.Link(
            'Geothermal',
            href='/geothermal',
            style={
                'color': 'rgb(0,0,0)',
                'font-size': '17px',
                'font-weight': 'bold',
                'paddingLeft':'25px'
                }),
    dcc.Link(
            'OpenLab',
            href='/openlab',
            style={
                'color': 'rgb(43,151,155)',
                'font-size': '17px',
                'font-weight': 'bold',
                'paddingLeft':'25px'
                }),
    html.Div([
        html.H3(['Select a wellbore'], style={'paddingBottom': '10px', 'font-weight': 'bold', 'border-bottom': '1px solid black'}),
        dcc.Dropdown(
            options=[{'label':value, 'value':key} for key, value in wells_dict.items()],
            value='15_9_19_A',
            placeholder='Select a wellbore',
            id='wells-dropdown',
            style={'width':'50%'}
        ),
        html.Br(),
    ], id='external-page-wells', style={'paddingLeft':'25px'}),
    html.Div(id='page-content')
], style={'font-family': 'Calibri', 'paddingLeft':'25px', 'paddingRight':'25px'})


df_wells = pd.read_csv('Data/volve_wells.csv', sep=';')

wells_layout = html.Div([
                        dash_table.DataTable(
                                    id='wells-table',
                                    columns=[{"name": i, "id": i} for i in df_wells.columns],
                                    data=df_wells.to_dict("rows"),
                                    style_header={'font-family': 'Calibri', 'font-weight': 'bold'},
                                    style_cell={'padding':'10px', 'font-family': 'Calibri', 'font-size': '16px', 'width': '100px'}
                        )], style={'width':'70%'})

def section_plot(df):
    x=df['N/S (m)'].max()-df['N/S (m)'].min()
    y=df['E/W (m)'].max()-df['E/W (m)'].min()
    z=df['TVD (m RKB)'].max()-df['TVD (m RKB)'].min()
    trace1 = go.Scatter3d(
        x=df[df['Section (in)']==30]['N/S (m)'],
        y=df[df['Section (in)']==30]['E/W (m)'],
        z=df[df['Section (in)']==30]['TVD (m RKB)'],
        mode='lines',
        name='Cased hole',
        line=dict(
            color='rgb(5,133,133)',
            width=2*30
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==30].index],
        hoverinfo='text',
        showlegend=True
    )

    trace2 = go.Scatter3d(
        x=df[df['Section (in)']==20]['N/S (m)'],
        y=df[df['Section (in)']==20]['E/W (m)'],
        z=df[df['Section (in)']==20]['TVD (m RKB)'],
        mode='lines',
        name='Cased hole',
        line=dict(
            color='rgb(5,133,133)',
            width=2*20
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==20].index],
        hoverinfo='text',
        showlegend=False
    )

    trace3 = go.Scatter3d(
        x=df[df['Section (in)']==14]['N/S (m)'],
        y=df[df['Section (in)']==14]['E/W (m)'],
        z=df[df['Section (in)']==14]['TVD (m RKB)'],
        mode='lines',
        name='Cased hole',
        line=dict(
            color='rgb(5,133,133)',
            width=2*14
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==14].index],
        hoverinfo='text',
        showlegend=False
    )

    trace4 = go.Scatter3d(
        x=df[df['Section (in)']==13.375]['N/S (m)'],
        y=df[df['Section (in)']==13.375]['E/W (m)'],
        z=df[df['Section (in)']==13.375]['TVD (m RKB)'],
        mode='lines',
        name='Cased hole',
        line=dict(
            color='rgb(5,133,133)',
            width=2*13.375
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==13.375].index],
        hoverinfo='text',
        showlegend=False
    )

    trace5 = go.Scatter3d(
        x=df[df['Section (in)']==12.25]['N/S (m)'],
        y=df[df['Section (in)']==12.25]['E/W (m)'],
        z=df[df['Section (in)']==12.25]['TVD (m RKB)'],
        mode='lines',
        name='Open hole',
        line=dict(
            color='rgb(198,137,75)',
            width=2*12.25
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==12.25].index],
        hoverinfo='text',
        showlegend=True
    )

    trace6 = go.Scatter3d(
        x=df[df['Section (in)']==9.625]['N/S (m)'],
        y=df[df['Section (in)']==9.625]['E/W (m)'],
        z=df[df['Section (in)']==9.625]['TVD (m RKB)'],
        mode='lines',
        name='Cased hole',
        line=dict(
            color='rgb(5,133,133)',
            width=2*9.625
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==9.625].index],
        hoverinfo='text',
        showlegend=False
    )

    trace7 = go.Scatter3d(
        x=df[df['Section (in)']==8.5]['N/S (m)'],
        y=df[df['Section (in)']==8.5]['E/W (m)'],
        z=df[df['Section (in)']==8.5]['TVD (m RKB)'],
        mode='lines',
        name='Open hole',
        line=dict(
            color='rgb(198,137,75)',
            width=2*8.5
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==8.5].index],
        hoverinfo='text',
        showlegend=True
    )

    trace8 = go.Scatter3d(
        x=df[df['Section (in)']==7]['N/S (m)'],
        y=df[df['Section (in)']==7]['E/W (m)'],
        z=df[df['Section (in)']==7]['TVD (m RKB)'],
        mode='lines',
        name='Cased hole',
        line=dict(
            color='rgb(5,133,133)',
            width=2*7
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==7].index],
        hoverinfo='text',
        showlegend=False
    )

    trace9 = go.Scatter3d(
        x=df[df['Section (in)']==6.625]['N/S (m)'],
        y=df[df['Section (in)']==6.625]['E/W (m)'],
        z=df[df['Section (in)']==6.625]['TVD (m RKB)'],
        mode='lines',
        name='Cased hole',
        line=dict(
            color='rgb(5,133,133)',
            width=2*6.625
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==6.625].index],
        hoverinfo='text',
        showlegend=False
    )

    trace10 = go.Scatter3d(
        x=df[df['Section (in)']==6]['N/S (m)'],
        y=df[df['Section (in)']==6]['E/W (m)'],
        z=df[df['Section (in)']==6]['TVD (m RKB)'],
        mode='lines',
        name='Open hole',
        line=dict(
            color='rgb(198,137,75)',
            width=2*6
        ),
        text = [
                "<b>Section:</b> {} in<br>"
                "<b>TVD:</b> {} m<br>"
                "<b>MD:</b> {} m<br>"
                .format(
                        df['Section (in)'].loc[i],
                        df['TVD (m RKB)'].loc[i],
                        df['MD (m RKB)'].loc[i],
                        )
                for i in df[df['Section (in)']==6].index],
        hoverinfo='text',
        showlegend=True
    )

    data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9,trace10]

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
        aspectmode = 'manual',
        aspectratio=dict(x=x/z, y=y/z, z=1)
        )
    )

    fig = dict(data=data, layout=layout)
    return fig

df_survey = pd.read_csv(f'Data/Hole_section/Plot/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')
df_hsection = pd.read_csv(f'Data/Hole_section/Table/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

hole_section_layout = html.Div([
    html.H3(['Hole section']),
    html.Div(id='dropdown-output', style={'paddingBottom': '10px', 'border-bottom': '1px solid black', 'font-weight': 'bold'}),
    html.Br(),
    html.Div(
        id='hole-section',
        children=[
            html.Div(dcc.Graph(
                id='hsection-graph',
                figure=section_plot(df_survey),
                config=dict(displayModeBar=False)
                            ), style={'display': 'inline-block', 'float': 'left', 'border-right': '1px solid black'}),
            html.Div(children=[
                html.Br(),
                dash_table.DataTable(
                    id='hsection-table',
                    columns=[
                        {"name": 'Type', "id": 'Type'},
                        {"name": 'From depth (m)', "id": 'From depth (m)'},
                        {"name": 'To depth (m)', "id": 'To depth (m)'},
                        {"name": 'OD (in)', "id": 'OD (in)'},
                        {"name": 'ID (in)', "id": 'ID (in)'}
                            ],
                    data=df_hsection.to_dict("rows"),
                    style_header={'font-family': 'Calibri', 'font-weight': 'bold'},
                    style_cell={'padding':'10px', 'font-family': 'Calibri', 'font-size': '16px'}
                                            )], style={'display': 'inline-block', 'paddingTop': '100px', 'paddingLeft': '75px'})
                ]
            )
])

@app.callback(
    Output('hsection-table', 'data'),
    [Input('wells-dropdown', 'value')]
            )
def display_hsection_table(val):
    df_hsection = pd.read_csv(f'Data/Hole_section/Table/Volve_{val}.csv', sep=';', float_precision='round_trip')
    data=df_hsection.to_dict("rows")
    return data

@app.callback(
    Output('hsection-graph', 'figure'),
    [Input('wells-dropdown', 'value')]
            )
def display_hsection_graph(val):
    df_survey = pd.read_csv(f'Data/Hole_section/Plot/Volve_{val}.csv', sep=';', float_precision='round_trip')
    return section_plot(df_survey)



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

df_survey = pd.read_csv(f'Data/Wellpath/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

wellpath_layout = html.Div([
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


@app.callback(
    Output('wellpath-table', 'data'),
    [Input('wells-dropdown', 'value')]
            )
def display_wellpath_table(val):
    df_survey = pd.read_csv(f'Data/Wellpath/Volve_{val}.csv', sep=';', float_precision='round_trip')
    data=df_survey[['MD (m RKB)', 'Inc (deg)', 'Azim (deg)', 'TVD (m RKB)', 'DLS (deg/30m)']].to_dict("rows")
    return data


@app.callback(
    Output('wellpath-graph', 'figure'),
    [Input('wells-dropdown', 'value')]
            )
def display_wellpath_graph(val):
    df_survey = pd.read_csv(f'Data/Wellpath/Volve_{val}.csv', sep=';', float_precision='round_trip')
    return wellpath_plot(df_survey)


df_fluid = pd.read_csv('Data/Fluid/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

fluid_layout = html.Div([
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


df_drillstring = pd.read_csv('Data/Drillstring/Volve_15_9_19_A_8_5.csv', sep=';', float_precision='round_trip')

drillstring_layout = html.Div([
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

geopressures_layout = html.Div([
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

geothermal_layout = html.Div([
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


open_lab_layout = html.Div([
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



@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def populate_content(url):
    if url == '/wells':
        return wells_layout
    elif url == '/hole_section':
        return hole_section_layout
    elif url == '/wellpath':
        return wellpath_layout
    elif url == '/fluid':
        return fluid_layout
    elif url == '/drillstring':
        return drillstring_layout
    elif url == '/geopressures':
        return geopressures_layout
    elif url == '/geothermal':
        return geothermal_layout
    elif url == '/openlab':
        return open_lab_layout


@app.callback(
    Output('external-page-wells', 'style'),
    [Input('url', 'pathname')]
)
def hide_external(url):
    if url == '/wells':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@app.callback(
    Output('dropdown-output', 'children'),
    [Input('wells-dropdown', 'value')]
)
def display_dropdown_contents(val):
    if val:
        return f'Wellbore selected: {wells_dict[val]}'


if __name__ == '__main__':
    app.run_server()
