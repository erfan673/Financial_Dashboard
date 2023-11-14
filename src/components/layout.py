import pandas as pd
from dash import Dash, html
from src.components import table_processor

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:


    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            table_processor.render(app, data)
        ]
    )