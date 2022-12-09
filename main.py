from io import BytesIO
import os
import pandas as pd
import pandas_gbq
from google.cloud import storage


BUCKET_NAME = ""
PROJECT_ID = ""
TABLE_ID = ""


def main(event, context):
    file_name = event["name"]
    print(f"Processing {file_name}.")

    df = read_storage_csv(BUCKET_NAME, file_name)
    rdf = data_process(df)

    pandas_gbq.to_gbq(rdf, TABLE_ID, project_id=PROJECT_ID, if_exists='append')
    print("Successfully Uploaded into BQ.")


def read_storage_csv(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_bytes()

    df = pd.read_csv(BytesIO(content))

    return df


def data_process(df):
    rdf = df.rename({"Date": "date", "Amount": "amount", "Account Number": "account_number",
                     "Transaction Type": "transaction_type", "Transaction Details": "transaction_details",
                     "Balance": "balance", "Category": "category", "Merchant Name": "merchant_name"
                     }, axis=1)
    rdf = rdf[["date", "amount", "account_number", "transaction_type",
               "transaction_details", "balance", "category", "merchant_name"]]
    rdf["date"] = pd.to_datetime(rdf.date)
    rdf["account_number"] = rdf.account_number.astype(str)
    rdf = rdf.fillna("")

    return rdf
