import pandas as pd
from dash import Dash, dcc, html, dash_table
import os

from src.components import ids
from dash.dependencies import Input, Output

def render(app:Dash, data:pd.DataFrame) -> html.Div:

    table_div = html.Div([
        dash_table.DataTable(
            data=data.to_dict('records'),
            columns=[{"name": i, "id": i, "editable": True} for i in data.columns],
            id=ids.TABLE_TRANSACTIONS,
            editable=True),
        html.Div(id='hidden-div', style={'display':'none'})]
    )
    @app.callback(
        Output('hidden-div', 'children'),
        Input(ids.TABLE_TRANSACTIONS, 'data')
     )
    def update_table(data):
        updated_df = pd.DataFrame(data)
        #save the updated dataframe
        updated_df.to_csv()
        output_folder = 'stored_data'
        file_name ='updated_data' #TODO come up with smart way to store data.
        os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
        output_path = os.path.join(output_folder, f'{file_name}.csv')
        updated_df.to_csv(output_path, index= False)
        return None
    return table_div



