from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("mpg.csv")

app = Dash()

app.layout = html.Div([
            dcc.Input(id = 'id-input', value = 'Initial text', type = 'text'),
            html.Div(id = 'id-container'),
    ]
)

@callback(Output(component_id='id-container', component_property='children'), 
          Input('id-input', 'value')
)
def updateText(value):
    return f'Entered value is: {value}'

if __name__ == '__main__':
    app.run_server()