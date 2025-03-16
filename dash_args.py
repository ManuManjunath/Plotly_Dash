from dash import Dash, dcc, html, callback, Output, Input, State

app = Dash()

arg1 = "123"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='output-container')
])

@app.callback(
    Output('output-container', 'children'),
    [Input('url', 'search')]
)
def update_output(search):
    if search:
        query = search.split('=')[1]  # Assuming simple key=value format
        return html.Div([
            html.H2(f'Query parameter value: {query}')
        ])
    else:
        return html.Div([
            html.H2('No query parameter provided')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
