from dash import Dash, dcc, html, callback, Output, Input, State
from dash.exceptions import PreventUpdate

"""
Reference: https://dash.plotly.com/dash-core-components/dropdown
"""

app = Dash()

dd_basic_list = ['India', 'Singapore', 'US', 'Malaysia']

dd_options_values = {'BLR': 'Bangalore', 'NYC': 'New York City', 'SNG': 'Singapore'}

dd_labels_values = [{'label': 'BLR', 'value': 'Bangalore'},
                    {'label': 'MUM', 'value': 'Mumbai'},
                    {'label': 'NDH', 'value': 'New Delhi'},
]

cities = [
    {"label": "New York City", "value": "NYC"},
    {"label": "Montreal", "value": "MTL"},
    {"label": "San Francisco", "value": "SF"},
    {"label": "Bangalore", "value": "BLR"},
    {"label": "Mumbai", "value": "MUM"},
    {"label": "New Delhi", "value": "NDL"},
    {"label": "New Jersey", "value": "NJR"},
    {"label": "Singapore", "value": "SNG"},
    {"label": "London", "value": "LND"},
    {"label": "Paris", "value": "PRS"}
]

app.layout = html.Div([
    html.H1('Drop down demo', style = {'textAlign': 'center', 'color': '#ABCDEF'}),
    html.Label("Basic drop down with default value", style = {'font-weight': 'bold'}),
    dcc.Dropdown(dd_basic_list, 'US', id = 'dd-basic'),
    html.Div(id = 'dd-basic-output-container'),
    html.Hr(),
    html.Label('Drop down with different values', style = {'font-weight': 'bold'}),
    dcc.Dropdown(options = dd_options_values, value = 'NYC', id = 'dd-options-values'),
    html.Div(id = 'dd-options-values-output-container'),
    html.Hr(),
    html.Label('Drop down with labels and values', style = {'font-weight': 'bold'}),
    dcc.Dropdown(options = dd_labels_values, value = 'Bangalore', id = 'dd-labels-values'),
    html.Div(id = 'dd-labels-values-output-container'),
    html.Hr(),
    html.Label('Drop down multi select', style = {'font-weight': 'bold'}),
    dcc.Dropdown(dd_basic_list, ['India', 'Malaysia'], multi = True, id = 'dd-multi-select'),
    html.Div(id = 'dd-multi-select-output-container'),
    html.Hr(),
    html.Label('Drop down with placeholder', style = {'font-weight': 'bold'}),
    dcc.Dropdown(dd_basic_list, placeholder = 'All Countries', id = 'dd-placeholder'),
    html.Div(id = 'dd-placeholder-output-container'),
    html.Hr(),
    html.Label('Adjusted height', style = {'font-weight': 'bold'}),
    dcc.Dropdown(dd_basic_list, 'Malaysia', id = 'dd-height', maxHeight = 50, optionHeight = 20),
    html.Div(id = 'dd-height-output-container'),
    html.Hr(),
    html.Label('Dropdown with search', style = {'font-weight': 'bold'}),
    dcc.Dropdown(cities, id = 'dd-search', multi = True),
    html.Div(id = 'dd-search-output-container'),
    html.Hr(),
    html.Label('Dynamic search', style = {'font-weight': 'bold'}),
    dcc.Dropdown(id='dd-dynamic-search', multi = True, placeholder = 'All values (placeholder)'),
    html.Div(id = 'dd-dynamic-search-output-container'),
    ]
)

@callback(Output('dd-basic-output-container', 'children'), Input('dd-basic', 'value'))
def basic_dropdown_selection(value):
    return f'selected value is {value}'

@callback(Output('dd-options-values-output-container', 'children'), Input('dd-options-values', 'value'))
def options_values_dropdown_selection(value):
    return f'selected value is {value}'

@callback(Output('dd-labels-values-output-container', 'children'), Input('dd-labels-values', 'value'))
def labels_values_dropdown_selection(value):
    return f'selected value is {value}'

@callback(Output('dd-multi-select-output-container', 'children'), Input('dd-multi-select', 'value'))
def multi_select_dropdown_selection(value):
    return f'selected value(s): {value}'

@callback(Output('dd-placeholder-output-container', 'children'), Input('dd-placeholder', 'value'))
def placeholder_dropdown_selection(value):
    if value == None:
        return f'selected value(s): All Countries'
    else:
        return f'selected value(s): {value}'

@callback(Output('dd-height-output-container', 'children'), 
          Input('dd-height', 'value'))
def basic_dropdown_selection(value):
    return f'selected value(s): {value}'

@callback(
    Output('dd-dynamic-search', 'options'),
    Input('dd-dynamic-search', 'search_value'),
    State('dd-dynamic-search', 'value')
)
def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    return [
        o for o in cities if search_value in o["label"] or o["value"] in (value or [])
    ]

@callback(Output('dd-dynamic-search-output-container', 'children'), Input('dd-dynamic-search', 'value'))
def showSelectedItems(value):
    return f'Selected value(s) are {value}'

if __name__ == '__main__':
    app.run_server()
