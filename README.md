# H.E.R-DAO-Hackathon-OORT
The `OortWrapper` is a Python class that simplifies the process of interacting with Oort cloud storage. It provides an easy-to-use interface for working with Oort buckets and objects, enabling you to create buckets, upload, download, and delete objects, and list the contents of buckets.

To use the OortWrapper class, you first need to set up your Oort credentials as environment variables. You can do this by creating a .env file in the root directory of your project, and adding the following lines:

```
OORT_ACCESS_KEY=<your_access_key>
OORT_SECRET_KEY=<your_secret_key>
OORT_ENDPOINT_URL=<your_endpoint_url>

```

Replace *<your_access_key>*, *<your_secret_key>* , and *<your_endpoint_url>* with your actual Oort credentials.

Once you have your credentials set up, you can start using the OortWrapper class to interact with your Oort buckets. Here's an example of how to use the OortWrapper class to upload a file to an Oort bucket:

```python
from oort_wrapper import OortWrapper

oort = OortWrapper()

# Create a new bucket
oort.create_bucket("my-bucket")

# Upload a file to the bucket
with open("my-file.txt", "rb") as f:
    oort.put_object("my-bucket", "my-file.txt", f.read())

```

# OortWrapper Technical overview 

The `OortWrapper` class provides a simple Python interface for working with Oort buckets and objects.

## Methods

### `list_buckets() -> List[str]`

List all available Oort buckets.

**Returns:**

- `List[str]`: A list of bucket names.

### `create_bucket(bucket_name: str)`

Create a new Oort bucket.

**Arguments:**

- `bucket_name` (str): The name of the new bucket.

### `put_object(bucket_name: str, object_name: str, data: bytes)`

Upload an object to an Oort bucket.

**Arguments:**

- `bucket_name` (str): The name of the bucket where the object will be uploaded.
- `object_name` (str): The name of the object (e.g., the file name).
- `data` (bytes): The binary data of the object.

### `get_object(bucket_name: str, object_name: str) -> bytes`

Download an object from an Oort bucket.

**Arguments:**

- `bucket_name` (str): The name of the bucket where the object is stored.
- `object_name` (str): The name of the object to download.

**Returns:**

- `bytes`: The binary data of the object.

### `list_objects(bucket_name: str) -> List[str]`

List all objects in an Oort bucket.

**Arguments:**

- `bucket_name` (str): The name of the bucket to list objects for.

**Returns:**

- `List[str]`: A list of object names in the bucket.

### `delete_object(bucket_name: str, object_name: str)`

Delete an object from an Oort bucket.

**Arguments:**

- `bucket_name` (str): The name of the bucket where the object is stored.
- `object_name` (str): The name of the object to delete.

