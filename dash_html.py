from dash import Dash, html, dcc

app = Dash()

overall_style = {'color': 'green', 'border': '2px green solid'}
innerDiv_style = {'color': 'blue', 'border': '3px blue solid'}

app.layout = html.Div([
        'Outermost Div',
        html.Div('Div inside outermost Div', style = {'color': 'red'}),
        # Using an image as a link
        html.A([
            html.Img(
                        src = app.get_asset_url(('nihilus.jpg')),
                        alt = 'image',
                        style = {'height': '4%', 'width': '4%'}
                )
        ], href = "https://www.google.com"
        ),

        html.Div(['Yet another inner Div'], style = innerDiv_style),
        html.Div(children=[
            html.H1("Horizontal alignment"),
            dcc.Graph(id = 'graph1', style = {'display': 'inline-block'}),
            dcc.Graph(id = 'graph2', style = {'display': 'inline-block'}),
                ]
        )
        ],
        style = overall_style
)

if __name__ == '__main__':
    app.run_server()
