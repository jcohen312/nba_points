import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from shot_viz import shot_chart

app = dash.Dash()

app.layout = html.Div([
    html.Div(html.H1(children = "NBA Clustering Project")),
    html.Label("Shot Chart"),

    html.Div(
        dcc.Input(
            id='player_input',
            placeholder='PLAYER NAME',
            type='text',
            value=''
        )
    ),

    html.Div(
        dcc.Graph(id='Shot Chart',
                  )
    ),

])

@app.callback(dash.dependencies.Output("Shot Chart", "figure"),
              [dash.dependencies.Input("player_input", "value")]
              )

def update_shot_chart(input_value):
    return shot_chart(input_value, '2018')

if __name__== "__main__":
    app.run_server(debug=True)