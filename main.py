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
            "Indian Diabetes",
            style={"margin-bottom": "0px"},
        ), 
        html.H3(
            "Alvaro Huarte and Xabier Etxezarreta",
            style={"margin-bottom": "0px"},
        ),           
    ],
    id="title",
    className="one-half column",
    ),

    # dashboard
    html.Div([
        # filters
        html.Div([
            html.P("Filter 1"),
            html.P("Filter 2"),
            html.P("Filter 3"),
        ],
        id="filters",
        className="container columns filter",        
        ),

        # indicators
        html.Div([
            # Precision
            html.Div([
                html.P("Precision")
            ],
            id="precision",
            className="mini_container",
            ),

            # Recall
            html.Div([
                html.P("Recall")
            ],
            id="recall",
            className="mini_container",
            ),

            #F1-Score
            html.Div([
                html.P("F1-Score")
            ],
            id="f1-score",
            className="mini_container",
            ),
        ],
        id="indicators",
        className="flex-display",        
        ),

        # graph 1
        html.Div([]),

        # graph 2
        html.Div([]),
    ],
    id="dashboard",
    className="flex-display",
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)