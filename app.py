import dash
import dash_core_components as dcc
import dash_html_components as html
from shot_viz import shot_chart

app = dash.Dash()

app.layout = html.Div([
    html.Div(html.H1(children = "NBA Clustering Project")),
    html.Label("Shot Cahrt"),
    html.Div(
        dcc.Graph(id='Ben Simmons',
                  figure= shot_chart('Ben Simmons', '2018')
                  )
    )
])

if __name__== "__main__":
    app.run_server(debug=True)