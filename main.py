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
            "Indian diabetes",
            style={"margin-bottom": "0px"},
        ),        
    ],
    className="one-half column",
    id="title",
    ),

    # Other
    html.Div([
        # callbacks aside
        html.Div([]),
        # precision, recall and f1 score
        html.Div([]),
        # graph 1
        html.Div([]),
        # graph 2
        html.Div([]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)