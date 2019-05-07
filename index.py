import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import wells
import hole_section
import wellpath
import fluid
import drillstring
import geopressures
import geothermal
import open_lab


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


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def populate_content(url):
    if url == '/wells':
        return wells.page_layout
    elif url == '/hole_section':
        return hole_section.page_layout
    elif url == '/wellpath':
        return wellpath.page_layout
    elif url == '/fluid':
        return fluid.page_layout
    elif url == '/drillstring':
        return drillstring.page_layout
    elif url == '/geopressures':
        return geopressures.page_layout
    elif url == '/geothermal':
        return geothermal.page_layout
    elif url == '/openlab':
        return open_lab.page_layout


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
