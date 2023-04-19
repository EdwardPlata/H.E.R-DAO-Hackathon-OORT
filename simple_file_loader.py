import os
import urllib.request
import logging
from oortwrapper import OortWrapper

logging.basicConfig(level=logging.DEBUG)

# Define constants
OORT_BUCKET_NAME = "kaggle-data"

def fetch_and_upload_kaggle_data(dataset_url, file_name):
    # Download dataset from Kaggle
    urllib.request.urlretrieve(dataset_url, file_name)

    # Upload dataset to Oort bucket
    oort_wrapper = OortWrapper()
    if OORT_BUCKET_NAME not in oort_wrapper.list_buckets():
        oort_wrapper.create_bucket(OORT_BUCKET_NAME)

    logging.info(f"Uploading {file_name} to Oort bucket {OORT_BUCKET_NAME}")
    with open(file_name, "rb") as f:
        oort_wrapper.put_object(OORT_BUCKET_NAME, file_name, f.read())

    # Delete downloaded file
    os.remove(file_name)

if __name__ == "__main__":
    # Example usage
    dataset_url = "https://www.kaggle.com/uciml/pima-indians-diabetes-database/download"
    file_name = "diabetes.csv"
    fetch_and_upload_kaggle_data(dataset_url, file_name)
