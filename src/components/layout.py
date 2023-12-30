import pandas as pd
from dash import Dash, html
from src.components import table_processor, uploader
from dash import dcc

def create_layout(app: Dash) -> html.Div:


    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            uploader.render(app),
            # table_processor.render(app, data)
        ]
    )