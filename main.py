import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import processing

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
                    {'label': 'DecisionTree Classifier', 'value': 'DecisionTree'},
                    {'label': 'Random Forest Classifier', 'value': 'RandomForest'},
                    {'label': 'Logistic Regression', 'value': 'LogisticRegression'}                     
                ],
                value='DecisionTree'
            ),

            html.P("Instances"),
            dcc.Dropdown(id='instances-dropdown'),

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
                html.H1("Accuracy"),
                html.H3(id="accuracy_text")
            ],
            id="accuracy",
            className="mini_container indicator",
            ),

            # Recall
            html.Div([                
                html.H1("F1-Score"),
                html.H3(id="f1_text")
            ],
            id="f1-score",
            className="mini_container indicator",
            ),

            #F1-Score
            html.Div([                
                html.H1("ROC AUC"),
                html.H3(id="rocauc_text")
            ],
            id="roc-auc",
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

@app.callback(
    [
        Output("accuracy_text", "children"),
        Output("f1_text", "children"),
        Output("rocauc_text", "children"),
    ],
    [Input("algorithm-dropdown", "value")],
)
def update_indicators(value):
    accuracy, f1, rocauc = processing.get_indicators(value)
    return accuracy, f1, rocauc    

@app.callback(
    [
        Output("instances-dropdown", "options")
    ],
    [Input("algorithm-dropdown", "value")],
)
def update_instances_dropdown(value):
    print(processing.get_instances(value))
    return processing.get_instances(value)

if __name__ == '__main__':
    app.run_server(debug=True)