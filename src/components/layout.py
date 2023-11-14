import pandas as pd
from dash import Dash, html
from src.components import dropdown, barcharts

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:


    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    dropdown.render(app)
                ]
            ),
            barcharts.render(app)
        ]
    )