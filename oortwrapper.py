import os
import boto3
from dotenv import load_dotenv

class OortWrapper:
    def __init__(self):
        load_dotenv()
        access_key = os.getenv('OORT_ACCESS_KEY')
        secret_key = os.getenv('OORT_SECRET_KEY')
        endpoint_url = os.getenv('OORT_ENDPOINT_URL')

        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=endpoint_url
        )

    def create_bucket(self, bucket_name):
        return self.s3_client.create_bucket(Bucket=bucket_name)

    def delete_bucket(self, bucket_name):
        return self.s3_client.delete_bucket(Bucket=bucket_name)

    def list_buckets(self):
        response = self.s3_client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]

    def list_objects(self, bucket_name):
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        return [item['Key'] for item in response['Contents']]

    def put_object(self, bucket_name, key, data):
        return self.s3_client.put_object(Bucket=bucket_name, Key=key, Body=data)

    def get_object(self, bucket_name, key):
        response = self.s3_client.get_object(Bucket=bucket_name, Key=key)
        return response['Body'].read()

    def delete_object(self, bucket_name, key):
        return self.s3_client.delete_object(Bucket=bucket_name, Key=key)
