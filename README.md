# H.E.R-DAO-Hackathon-OORT
The `OortWrapper` is a Python class that simplifies the process of interacting with Oort cloud storage. It provides an easy-to-use interface for working with Oort buckets and objects, enabling you to create buckets, upload, download, and delete objects, and list the contents of buckets.

# OortWrapper

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

