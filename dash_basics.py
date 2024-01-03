from dash import Dash, dcc, html

app = Dash()

data = [
    {'x': [2020, 2021, 2022], 'y': [4, 5, 6], 'type': 'bar', 'name': 'India'},
    {'x': [2020, 2021, 2022], 'y': [6, 5, 4], 'type': 'bar', 'name': 'Singapore'}
]

colours = {'background': '#111111', 'text': '#7FDBFF', 'paper_bg': '#222222'}

# Styling using CSS
graph_style = {'textAlign': 'center', 'color': colours['text']}

layout = {
    'tite': 'Sample bar graph', 
    'plot_bgcolor': colours['background'],
    'paper_bgcolor': colours['paper_bg'],
    'font': colours['text']
}

app.layout = html.Div(children = [
    html.H1("Hello Dash!", style=graph_style),
    html.Div('Dash: Web Dashboards with Python.'),
    dcc.Graph(id='graph example', figure={'data': data, 'layout': layout})
    ],
    style = {'backgroundColor': colours['background']}
)

if __name__ == '__main__':
    app.run_server()