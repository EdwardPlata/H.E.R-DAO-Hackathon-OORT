import os
import boto3
from dotenv import load_dotenv
import botocore

class OortWrapper:
    def __init__(self):
        """
        Initialize the OortWrapper with access keys and endpoint URL.
        """
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
        """
        Create a new bucket with the given name.

        :param bucket_name: The name of the bucket to create.
        :return: The response from the create_bucket API call.
        """
        try:
            return self.s3_client.create_bucket(Bucket=bucket_name)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'BucketAlreadyExists' or e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
                print(f"Bucket '{bucket_name}' already exists. Skipping bucket creation.")
            else:
                raise e

    def delete_bucket(self, bucket_name):
        """
        Delete the specified bucket.

        :param bucket_name: The name of the bucket to delete.
        :return: The response from the delete_bucket API call.
        """
        try:
            return self.s3_client.delete_bucket(Bucket=bucket_name)
        except botocore.exceptions.ClientError as e:
            print(f"Error deleting bucket '{bucket_name}': {e}")
            raise e

    def list_buckets(self):
        """
        List all buckets.

        :return: A list of bucket names.
        """
        response = self.s3_client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]

    def list_objects(self, bucket_name):
        """
        List all objects in the specified bucket.

        :param bucket_name: The name of the bucket to list objects from.
        :return: A list of object keys.
        """
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            return [item['Key'] for item in response['Contents']]
        else:
            return []

    def put_object(self, bucket_name, key, data):
        """
        Put an object into the specified bucket.

        :param bucket_name: The name of the bucket to store the object in.
        :param key: The key (name) of the object.
        :param data: The data (content) of the object.
        :return: The response from the put_object API call.
        """
        try:
            return self.s3_client.put_object(Bucket=bucket_name, Key=key, Body=data)
        except botocore.exceptions.ClientError as e:
            print(f"Error putting object '{key}' in bucket '{bucket_name}': {e}")
            raise e

    def get_object(self, bucket_name, key):
        """
        Get an object from the specified bucket.

        :param bucket_name: The name of the bucket to retrieve the object from.
        :param key: The key (name) of the object.
        :return: The data (content) of the object.
        """
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=key)
            return response['Body'].read()
        except botocore.exceptions.ClientError as e:
            print(f"Error getting object '{key}' from bucket '{bucket_name}': {e}")
            raise e

    def delete_object(self, bucket_name, key):
        """
        Delete an object from the specified bucket.

        :param bucket_name: The name of the bucket to delete the object from.
        :param key: The key (name) of the object.
        :return: The response from the delete_object API call.
        """
        try:
            return self.s3_client.delete_object(Bucket=bucket_name, Key=key)
        except botocore.exceptions.ClientError as e:
            print(f"Error deleting object '{key}' from bucket '{bucket_name}': {e}")
            raise e
