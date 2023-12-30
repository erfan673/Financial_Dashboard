import pandas as pd

class DataSchema:
    USER = "Person"
    YEAR = "Year"
    MONTH = "Month"

    Erfan = "Erfan"
    Hiva = "Hiva"

    # ScotiaBank credit card export
    AMOUNT_SCOTIA_CC = "Amount"
    PAYEE_SCOTIA_CC = "Payee"
    LOCATION_SCOTIA_CC = "Address"
    DATE_SCOTIA_CC = "Posted Date"

    scotia_cc_schema_list = [AMOUNT_SCOTIA_CC, PAYEE_SCOTIA_CC, LOCATION_SCOTIA_CC,DATE_SCOTIA_CC]

    #Source-Person IDs
    SOURCE_SCOTIA_CC_E = "scotia-cc-erfan"

def load_credit_card_statement(path, source) -> pd.DataFrame:
    data_preview = pd.read_csv(path)
    print(data_preview.head())
    # need to figure out the column names match which bank export format.
    # these will need to be hardcoded for now until a ui can be developed for generating new data schemas
    # Check if all target_column_names are present in column_names
    if all(col_name in data_preview.columns for col_name in DataSchema.scotia_cc_schema_list):
        print("Class Erfan, Credit Card Scotia.")
        # which person? #TODO
        # load the data from the CSV file
        data = data_preview.copy(deep=True)
        data[DataSchema.DATE_SCOTIA_CC] = pd.to_datetime(data[DataSchema.DATE_SCOTIA_CC])
        data[DataSchema.USER] = DataSchema.Erfan
        data[DataSchema.YEAR] = data[DataSchema.DATE_SCOTIA_CC].dt.year.astype(str)
        data[DataSchema.MONTH] = data[DataSchema.DATE_SCOTIA_CC].dt.month.astype(str)
    return data

#TODO
'''
def 
'''