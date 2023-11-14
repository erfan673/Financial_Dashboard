import pandas as pd
from dash import Dash, dcc, html


from src.components import ids
from dash.dependencies import Input, Output

def render(app:Dash) -> html.Div:
 @app.callback(
     Output()
 )