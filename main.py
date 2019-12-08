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
            html.P("Classification Algorithm:"),
            dcc.Dropdown(
                id='algorithm-dropdown',
                options=[
                    {'label': 'Random Forest Classifier', 'value': 'RandomForest'},
                    {'label': 'XGBoost Classifier', 'value': 'XGBoost'}
                ],
                value='RandomForest'
            ),

            html.P("Filter 2"),
            dcc.Dropdown(
                id='filter2-dropdown',
                options=[
                    {'label': 'Filter 2', 'value': 'Filter 2'},
                    {'label': 'Filter 2', 'value': 'Filter 2.1'}
                ],
                value='Filter 2'
            ),

            html.P("Filter 3"),       
            dcc.Dropdown(
                id='filter3-dropdown',
                options=[
                    {'label': 'Filter 3', 'value': 'Filter 3'},
                    {'label': 'Filter 3', 'value': 'Filter 3.1'}
                ],
                value='Filter 3'
            ),     
        ],
        id="filters",
        className="container",        
        ),

        # indicators
        html.Div([
            # Precision
            html.Div([
                html.P("Precision")
            ],
            id="precision",
            className="mini_container indicator",
            ),

            # Recall
            html.Div([
                html.P("Recall")
            ],
            id="recall",
            className="mini_container indicator",
            ),

            #F1-Score
            html.Div([
                html.P("F1-Score")
            ],
            id="f1-score",
            className="mini_container indicator",
            ),
        ],
        id="indicators",    
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