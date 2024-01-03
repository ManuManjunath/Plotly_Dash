from dash import Dash, dcc, html, callback, Input, Output, State

dashboard_layout = html.Div([
        dcc.Input(id = "input-number", value = 1, style = {"fontSize": 24}),
        html.Hr(),
        html.H1("Live update"),
        html.H3(id = "output-number"),
        html.Hr(),
        html.H1("Update with state"),
        html.Button(id = "submit-button", n_clicks = 0, children = "show vaue"),
        html.H3(id = "output-number-state")
    ]
)

app = Dash()

app.layout = dashboard_layout

@callback(
        Output("output-number", "children"),
        Input("input-number", "value")
)
def updateLiveOutput(value):
    return value

@callback(
        Output("output-number-state", "children"),
        Input("submit-button", "n_clicks"),
        [State("input-number", "value")]
)
def updateStateOutput(n_clicks, value):
    return value

if __name__ == "__main__":
    app.run_server()