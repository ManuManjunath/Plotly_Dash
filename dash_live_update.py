from dash import Dash, html, dcc, Input, Output, callback
import requests
import plotly.graph_objects as go

scrapeUrl = "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10"

dashLayout = html.Div([
    html.Div([
        html.Pre(id = 'counter', children = "Random Number"),
        dcc.Graph(id = 'graph-random-number', style={'width':1200}),
        dcc.Interval(id = 'interval-component', interval = 10000, n_intervals = 0)
    ])
])

counter_list = []

app = Dash()
app.layout = dashLayout

@callback(
        [Output('counter', 'children') ,Output('graph-random-number', 'figure')],
        [Input('interval-component', 'n_intervals')]
)
def update_data(n):
    num = requests.get(scrapeUrl).json()[0]
    counter_list.append(num)
    text = f"Random number between 1 and 10 is {num}"

    graphData = [go.Scatter(
        x = list(range(len(counter_list))),
        y = counter_list,
        mode = 'lines+markers'
    )]
    fig = go.Figure(data = graphData)

    return text, fig

if __name__ == '__main__':
    app.run_server()