import pandas as pd

class DataSchema:
    USER = "user"
    YEAR = "Year"
    MONTH = "Month"



    # ScotiaBank credit card export
    AMOUNT_SCOTIA_CC = "Amount"
    PAYEE_SCOTIA_CC = "Payee"
    LOCATION_SCOTIA_CC = "Address"
    DATE_SCOTIA_CC = "Posted Date"

class DataSchema_Sources:
    SCOTIA_CC_E = "scotia-cc-erfan"

def load_credit_card_statement(path: str, source) -> pd.DataFrame:
    # which bank/ person? #TODO
    if source == DataSchema_Sources.SCOTIA_CC_E:
        # load the data from the CSV file
        data = pd.read_csv(
            path,
            dtype={
                DataSchema.AMOUNT_SCOTIA_CC: float,
                DataSchema.PAYEE_SCOTIA_CC: str,
                DataSchema.DATE_SCOTIA_CC: str,
                DataSchema.LOCATION_SCOTIA_CC: str,
            },
            parse_dates=[DataSchema.DATE_SCOTIA_CC],
        )
        data[DataSchema.YEAR] = data[DataSchema.DATE_SCOTIA_CC].dt.year.astype(str)
        data[DataSchema.MONTH] = data[DataSchema.DATE_SCOTIA_CC].dt.month.astype(str)
    else:
        None
    return data

#TODO
'''
def 
'''