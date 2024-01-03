from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('gapminderDataFiveYear.csv')
year_values = []
for year in df['year'].unique():
    year_values.append({'label': str(year), 'value': year})

graphLayout = go.Layout(
    xaxis = {'type': 'log', 'title': 'GDP Per Capita'},
    yaxis = {'title': 'Life Expectance'},
    hovermode = 'closest'
)

app = Dash()

app.layout = html.Div([
            dcc.Graph(id = 'graph'),
            dcc.Dropdown(id = 'dd-year-picker', options = year_values, value = df['year'].max())
    ]
)

@callback(Output('graph', 'figure'), Input('dd-year-picker', 'value'))
def updateGraph(selector_year_value):
    df_filtered = df[df['year'] == selector_year_value]
    traces = []
    for cntnt in df_filtered['continent'].unique():
        df_continent = df_filtered[df_filtered['continent'] == cntnt]
        traces.append(go.Scatter(
            x = df_continent['gdpPercap'],
            y = df_continent['lifeExp'],
            text = df_continent['country'],
            mode = 'markers',
            opacity = 0.7,
            marker = {'size': 15},
            name = cntnt
        ))
    fig = {'data': traces, 'layout': graphLayout}
    return fig

if __name__ == '__main__':
    app.run_server()