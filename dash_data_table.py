from dash import Dash, html, dcc, Input, Output, callback, dash_table
from dash.dash_table.Format import Format, Scheme
from dash.dash_table import FormatTemplate
import pandas as pd
from collections import OrderedDict

df_5 = pd.read_csv("mpg.csv").head(5)
df_10 = pd.read_csv("mpg.csv").head(10)

df_rand = pd.DataFrame(OrderedDict([[
    'Column {}'.format(i + 1), list(range(30))
    ] for i in range(15)
    ]
))

df_temp = pd.DataFrame(OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
))

"""
style_* property priority -0 in decreasing order
1. style_data_conditional
2. style_data
3. style_filter_conditional
4. style_filter
5. style_header_conditional
6. style_header
7. style_cell_conditional
8. style_cell
"""


layout_table_basic = html.Div([
    html.H1("Basic table"),
    dash_table.DataTable(data = df_5.to_dict("records"),
                         columns = [{"name": i, "id": i} for i in df_5.columns],
                         cell_selectable = False)
    ]
)

layout_table_with_callback = html.Div([
        html.H1("Click on a cell"),
        dash_table.DataTable(df_5.to_dict('records'), [{"name": i, "id": i} for i in df_5.columns], id = 'tbl'),
        html.H3(id = "cell-details")
    ]
)

layout_table_with_pagination_and_sort = html.Div([
        html.H1("Table with pagination"),
        dash_table.DataTable(data = df_10.to_dict('records'),
                             columns = [{"name": i, "id": i} for i in df_5.columns],
                             page_size = 4,
                             sort_action = 'native'
                             )
    ]
)

layout_fixed_headers_with_scroll = html.Div([
        html.H1("Table with fixed headers and scroll bar"),
        dash_table.DataTable(data = df_10.to_dict('records'),
                             columns = [{"name": i, "id": i} for i in df_5.columns],
                             fixed_rows = {"headers": True},
                             style_table = {"height": 200, "overflowY": "auto"}
                             )
    ]
)

layout_fixed_col_width = html.Div([
        html.H1("Fixed column width"),
        dash_table.DataTable(
            data = df_rand.to_dict("records"),
            columns = [{'id': c, 'name': c} for c in df_rand.columns],
            fixed_rows = {"headers": True},
            style_table = {"height": 200},
            style_cell={'minWidth': '150px', 'maxWidth': '150px', 'width': '150px'}
        )
    ]
)

layout_adjusted_col_width = html.Div([
        html.H1("Adjusted column width"),
        dash_table.DataTable(
            data = df_temp.to_dict("records"),
            columns = [{'id': c, 'name': c} for c in df_temp.columns],
            fixed_rows = {"headers": True},
            style_table = {"height": 200, "overflowX": "auto"},
            style_cell = {'minWidth': '10px', 'maxWidth': '250px', 'width': '100px'},
            style_cell_conditional = [{'if': {'column_id': 'Date'}, 'width': '250px'},]
        )
    ]
)

# Read more here - https://dash.plotly.com/datatable/conditional-formatting
layout_formatted_grid = html.Div([
        html.H1("* Some formatting"),
        html.P("* All data cells have a blue border"),
        html.P("* cylinders column is right aligned"),
        html.P("* displacement header has a different format"),
        html.P("* horespower header is center aligned"),
        html.P("* horsepower value highlighted if below 150"),
        dash_table.DataTable(
            data = df_5.to_dict("records"),
            columns = [{'id': c, 'name': c} for c in df_5.columns],
            style_header = {'border': '1px solid black', 'backgroundColor': 'rgb(240, 300, 120)'},
            style_cell = {'textAlign': 'left'},
            style_data = {'border': '1px solid blue'},
            style_cell_conditional = [
                {
                    'if': {'column_id': 'cylinders'}, 
                    'textAlign': 'right'
                },
                {
                    'if': {'column_id': 'horsepower', 'filter_query': '{horsepower} < 150'},
                    'color': 'red',
                    'backgroundColor': 'black'
                },
                {
                    'if': {'column_id': 'name'},
                    'filter_action': 'native',
                    'filter_options': {"placeholder_text": "Filter value..."},
                }
            ],
            style_header_conditional = [
                {'if': {'column_id': 'displacement'}, 'backgroundColor': 'rgb(100, 100, 100)'},
                {'if': {'column_id': 'horsepower'}, 'textAlign': 'center'},
            ]
        )
    ]
)

layout_list_view_with_banding = html.Div([
        html.H1("List view with banding"),
        dash_table.DataTable(
            data = df_5.to_dict("records"),
            columns = [{'id': c, 'name': c} for c in df_5.columns],
            style_as_list_view = True,
            style_data_conditional = [{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(220, 220, 220)'}]
        )
    ]
)

layout_number_formatting = html.Div([
        html.H1("Number formatting"),
        dash_table.DataTable(
            data = df_5.to_dict("records"),
            columns = [
                dict(id = 'mpg', name = 'MPG'),
                dict(id = 'cylinders', name = 'CYLINDERS'),
                dict(id = 'displacement', name = 'DISPLACEMENT', type = 'numeric', format = Format(precision=2, scheme=Scheme.fixed)),
                dict(id = 'horsepower', name = 'HORSEPOWER'),
                dict(id = 'weight', name = 'WEIGHT'),
                dict(id = 'acceleration', name = 'ACCELERATION'),
                dict(id = 'model_year', name = 'MODEL YEAR'),
                dict(id = 'origin', name = 'ORIGIN', type = 'numeric', format = FormatTemplate.percentage(2)),
            ]
        )
    ]
)

app = Dash()

app.layout = html.Div([
    layout_table_basic,
    html.Hr(),
    layout_table_with_callback,
    html.Hr(),
    layout_table_with_pagination_and_sort,
    html.Hr(),
    layout_fixed_headers_with_scroll,
    html.Hr(),
    layout_fixed_col_width,
    html.Hr(),
    layout_adjusted_col_width,
    html.Hr(),
    layout_formatted_grid,
    html.Hr(),
    layout_list_view_with_banding,
    html.Hr(),
    layout_number_formatting,
    html.Hr(),
    ]
)

@callback(
    Output("cell-details", "children"),
    Input("tbl", "active_cell")
)
def show_selected_cell_data(active_cell):
    print(active_cell)
    cell = active_cell
    cell_value = df_5.iat[cell["row"], cell["column"]]
    #return str(active_cell) if active_cell else "click on a cell"
    return cell_value

if __name__ == "__main__":
    app.run_server()