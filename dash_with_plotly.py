from dash import Dash, dcc, html
import plotly.graph_objects as go
import numpy as np

app = Dash()

# Creating data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x = random_x, 
                   y =  random_y, 
                   mode = 'markers',
                   marker = {'size': 12, 
                              'color': 'rgb(51, 204, 153)',
                              'symbol': 'pentagon',
                              'line': {'width': 2}
                              }
                   )
]

layout = go.Layout(title = 'Sample Scatter Plot',
                   xaxis = {'title': 'Some X title'},
                   yaxis = {'title': 'Some Y title'}
)

app.layout = html.Div(
    [
        dcc.Graph(id = 'scatterplot1', figure = {'data': data, 'layout': layout}),
        dcc.Graph(id = 'scatterplot2', figure = {'data': data, 'layout': layout})
    ]
)

if __name__ == '__main__':
    app.run_server()