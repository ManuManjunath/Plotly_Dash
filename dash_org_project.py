from dash import Dash, dcc, html, callback, Input, Output, State
import polars as pl

"""
Columns:
    Index
    Organization Id
    Name
    Website
    Country
    Description
    Founded
    Industry
    Number of employees

1st row (Industry Insights --> with Industry dropdown) 
    --> Number of companies by Industry
    --> Oldest companies by Industry
    --> Number of employees by Industry
2nd row (Country Insights --> with Country dropdown)
    --> Number of companies by Country
    --> Oldest companies by Country
    --> Number of employees by Country
"""

df = pl.read_csv("organizations.csv")
dd_industry = df["Industry"].unique().to_list()
dd_country = df["Country"].unique().to_list()

layout_industry_selector = html.Div([
        html.H2("Industry insights"),
        dcc.Dropdown(
            dd_industry,
            id = "dd-industry",
            multi = True, 
            maxHeight = 150,
            placeholder = "Choose Industries"
            )
    ],
    style = {"width": "50%"},
)

layout_industry_visualizations = html.Div(children = [
        dcc.Graph(
            id = "graph-number-of-companies-by-industry",
            style = {"display": "inline-block", "width": "60vh"}
        ),
        dcc.Graph(
            id = "graph-oldest-companies-by-industry",
            style = {"display": "inline-block", "width": "60vh"}
        ),
        dcc.Graph(
            id = "graph-employees-by-industry",
            style = {"display": "inline-block", "width": "60vh"}
        ),
    ]
)

layout_country_selector = html.Div([
        html.H2("Country insights"),
        dcc.Dropdown(
            dd_country,
            id = "dd-country",
            multi = True,
            maxHeight = 150,
            placeholder = "Choose Countries"
            )
    ],
    style = {"width": "50%"}
)

layout_country_visualizations = html.Div(children = [
        dcc.Graph(
            id = "graph-number-of-companies-by-country",
            style = {"display": "inline-bock"}
        ),
        dcc.Graph(
            id = "graph-oldest-companies-by-country",
            style = {"display": "inline-bock"}
        ),
        dcc.Graph(
            id = "graph-employees-by-country",
            style = {"display": "inline-bock"}
        ),
    ]
)


app = Dash()

app.layout = html.Div([
        html.H1("Organizations dashboard"),
        layout_industry_selector,
        layout_industry_visualizations,
        html.Hr(),
        layout_country_selector,
        layout_country_visualizations
    ]
)

if __name__ == "__main__":
    app.run_server()