import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import processing

dashboard = processing.Dashboard()

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
                clearable=False,
                options=[
                    {'label': 'DecisionTree Classifier', 'value': 'DecisionTree'},
                    {'label': 'Random Forest Classifier', 'value': 'RandomForest'},
                    {'label': 'Logistic Regression', 'value': 'LogisticRegression'}                     
                ],
                value='DecisionTree'
            ),

            html.P("Instances"),
            dcc.Dropdown(id='instances-dropdown', clearable=False),

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
        html.Div([
            dcc.Graph(id='xai-graph'),               
        ],
        id="xai",
        ),

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
        Output("instances-dropdown", "options"),
        Output("instances-dropdown", "value")
    ],
    [Input("algorithm-dropdown", "value")],
)
def algorithm_updated(value):
    dashboard.update_model(value)
    accuracy, f1, rocauc = dashboard.get_indicators()
    instances, value = dashboard.get_instances()
    return accuracy, f1, rocauc, instances, value

@app.callback(    
    Output("xai-graph", "figure"),     
    [Input("instances-dropdown", "value")],
)
def instance_updated(value):
    shap_values = dashboard.get_shap_values(value)
    traces = [shap_values]  
    print(traces)
    '''
    for name, shap in shap_values.items():  
        traces.append(dict(
            x=shap,
            y=name
        ))    
    '''
    graph = {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'bar', 'title': 'SHAP values', 'range':[-1, 1]},
            yaxis={'title': 'Variable', 'type': 'bar', 'range': [-1, 8]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }

    return graph


if __name__ == '__main__':
    app.run_server(debug=True)
