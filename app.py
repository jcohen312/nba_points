import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from shot_viz import shot_chart

app = dash.Dash()

app.layout = html.Div([
        html.Div(
            html.H1(children = "NBA Clustering Project")
        ),

        html.Label("Shot Chart"),

        html.Div(
            [dcc.Input(
                id='player_input',
                placeholder='PLAYER NAME',
                type='text',
                value=''
            ),
            dcc.Dropdown(
              id="season-dropdown",
              options=[
                  {'label': '2017', 'value': '2017'},
                  {'label': '2018', 'value': '2018'},
                  {'label': '2019', 'value': '2019'}
              ],
              value='2018'
            ),

            ]
        ),

        html.Div(
            dcc.Graph(id='Shot Chart',
                      )
        ),

])

@app.callback(dash.dependencies.Output("Shot Chart", "figure"),
              [Input("player_input", "value"),
               Input("season-dropdown", "value")],

              )

def update_shot_chart(player, year):
    return shot_chart(player, year)

if __name__== "__main__":
    app.run_server(debug=True)