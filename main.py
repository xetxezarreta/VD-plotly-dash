import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# load data
df = pd.read_csv('data/diabetes.csv')

# Create app layout
app = dash.Dash(__name__)
app.layout = html.Div([
    # Title
    html.Div([
        html.H1(
            "INDIAN DIABETES",
            style={"margin-bottom": "0px"},
        ), 
        html.H3(
            "Alvaro Huarte and Xabier Etxezarreta",
            style={"margin-bottom": "0px"},
        ),           
    ],
    className="one-half column",
    id="title",
    ),

    # Other
    html.Div([
        # filters
        html.Div([
            html.P("Filter 1"),
            html.P("Filter 2"),
            html.P("Filter 3"),
        ],
        className="container columns filter",
        id="filters",
        ),

        # precision, recall and f1 score
        html.Div([
            html.Div([
                html.P("Precision")
            ],
            id="precision",
            className="mini_container",
            ),

            html.Div([
                html.P("Recall")
            ],
            id="recall",
            className="mini_container",
            ),

            html.Div([
                html.P("F1-Score")
            ],
            id="f1-score",
            className="mini_container",
            ),
        ],
        className="containers flex-display",
        ),

        # graph 1
        html.Div([]),

        # graph 2
        html.Div([]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)