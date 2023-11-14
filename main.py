from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.data.loader import load_credit_card_statement
from src.data.loader import DataSchema

from src.components.layout import create_layout

DATA_PATH = r"data\October2023_2322.csv"

def main() -> None:
    #load the data and create the data manager
    data = load_credit_card_statement(DATA_PATH, DataSchema.SOURCE_SCOTIA_CC_E)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Heefan's Financial Dashboard"
    app.layout = create_layout(app, data)
    app.run(debug=True)



if __name__ == "__main__":
    main()