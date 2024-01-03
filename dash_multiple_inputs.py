from dash import Dash, html, dcc, callback, Input, Output
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("mpg.csv")
features = df.columns

dashboard_layout = [html.Div([dcc.Dropdown(id='xaxis', 
                                           options=[{'label': i, 'value': i} for i in features],
                                           value = 'displacement')],
                        style = {'width': '48%', 'display': 'inline-block'}),
                    html.Div([dcc.Dropdown(id='yaxis', 
                                           options=[{'label': i, 'value': i} for i in features],
                                           value = 'mpg')],
                        style = {'width': '48%', 'display': 'inline-block'}),
                    dcc.Graph(id = 'target-graph')
]

app = Dash()

app.layout = html.Div(dashboard_layout, style = {'padding': 10})

@callback(
        Output('target-graph', 'figure'),
        [Input('xaxis', 'value'), Input('yaxis', 'value')]
)
def update_graph(x, y):
    x_col = df[x]
    y_col = df[y]
    graph_data = go.Scatter(x = x_col, 
                       y = y_col, 
                       text = df['name'],
                       mode = 'markers',
                       marker = {'size': 15, 'opacity': 0.5, 'line': {'width': 0.5, 'color': 'white'}}
    )

    graph_layout = go.Layout(title = 'Dashboard with multiple inputs',
                             xaxis = {'title': x},
                             yaxis = {'title': y},
                             hovermode = 'closest'

    )

    return {"data": [graph_data], "layout": graph_layout}



if __name__ == '__main__':
    app.run_server()