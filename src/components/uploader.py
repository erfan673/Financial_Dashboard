import base64

from dash import Dash, dcc, html, dash_table
import plotly.express as px
from src.components import ids, table_processor
from dash.dependencies import Input, Output, State
import pandas as pd
from dash.exceptions import PreventUpdate
from src.data import loader
from io import StringIO, BytesIO

def render(app:Dash) ->html.Div:
    upload_div = html.Div(children=[
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True),
        html.Div(
            id='upload-processor-table'
        )
        ])

    def parse_contents(contents, filename):
        print(type(filename))
        print(filename)
        contents = contents[0]
        filename = filename[0]
        content_type, content_string = contents.split(',')
        decoded_content = base64.b64decode(content_string)
        # # convert to a path_object which can in turn be fed to pd.read_csv or pd.read_excel
        # path_object = StringIO(decoded_content.decode('utf-8'))
        # # # Use pandas to read the CSV content
        # # df = pd.read_csv(StringIO(decoded_content.decode('utf-8')))
        # return path_object
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                path_object = StringIO(decoded_content.decode('utf-8'))
                print(f"path_object is {path_object}")
                return path_object
            elif 'xls' in filename:
                print("xls uploaded.") #TODO
                # Assume that the user uploaded an excel file
                # df = pd.read_excel(BytesIO(decoded_content))
        except Exception as e:
            print(e,'There was an error processing this file.')

    @app.callback(
        Output('upload-processor-table','children'),
        Input('upload-data','contents'),
        State('upload-data', 'filename'),
        State('upload-data', 'last_modified'),
        prevent_initial_call=True
    )
    def display_uploaded_data(list_of_contents, file_name, date_last_modified):
        # print(f"list of contents is {list_of_contents}")
        path = parse_contents(list_of_contents,file_name)
        print(f"path is {path}")
        data_loaded = loader.load_credit_card_statement(path, "Erfan Scotia CC")
        # table_processor.render(app,data_loaded) #TODO edit uploaded data

        display = html.Div([
        html.H5(file_name),
        # html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data_loaded.to_dict('records'),
            [{'name': i, 'id': i} for i in data_loaded.columns]
        ),

        html.Hr(),  # horizontal line
        ])
        return display
    return upload_div

