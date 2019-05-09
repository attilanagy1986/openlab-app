import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from app import app

#function to create hole section plot
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

#default wellbore
df_survey = pd.read_csv(f'Data/Hole_section/Plot/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')
df_hsection = pd.read_csv(f'Data/Hole_section/Table/Volve_15_9_19_A.csv', sep=';', float_precision='round_trip')

#define hole section page layout and content
page_layout = html.Div([
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

#callback to update table according to wellbore selection
@app.callback(
    Output('hsection-table', 'data'),
    [Input('wells-dropdown', 'value')]
            )
def display_hsection_table(val):
    df_hsection = pd.read_csv(f'Data/Hole_section/Table/Volve_{val}.csv', sep=';', float_precision='round_trip')
    data=df_hsection.to_dict("rows")
    return data

#callback to update plot according to wellbore selection
@app.callback(
    Output('hsection-graph', 'figure'),
    [Input('wells-dropdown', 'value')]
            )
def display_hsection_graph(val):
    df_survey = pd.read_csv(f'Data/Hole_section/Plot/Volve_{val}.csv', sep=';', float_precision='round_trip')
    return section_plot(df_survey)
