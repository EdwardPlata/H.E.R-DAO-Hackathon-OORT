import unittest
from oortwrapper import OortWrapper

class TestOortWrapper(unittest.TestCase):

    passed_tests = 0
    failed_tests = 0

    def setUp(self):
        self.oort = OortWrapper()

    def tearDown(self):
        if self._outcome.success:
            TestOortWrapper.passed_tests += 1
        else:
            TestOortWrapper.failed_tests += 1
            print("Error: ", self._testMethodName, "\n")

    @classmethod
    def tearDownClass(cls):
        print("\nTotal passed tests: ", cls.passed_tests)
        print("Total failed tests: ", cls.failed_tests)

    def test_create_bucket(self):
        print("Testing create_bucket...")
        bucket_name = 'test-clear-bucket'
        self.oort.create_bucket(bucket_name)
        self.assertIn(bucket_name, self.oort.list_buckets())
        self.oort.delete_bucket(bucket_name)
        print("...Passed\n")

    def test_delete_bucket(self):
        print("Testing delete_bucket...")
        bucket_name = 'test-delete-bucket'
        self.oort.create_bucket(bucket_name)
        self.oort.delete_bucket(bucket_name)
        self.assertNotIn(bucket_name, self.oort.list_buckets())
        print("...Passed\n")

    def test_put_object(self):
        print("Testing put_object...")
        bucket_name = 'test-put-object-bucket'
        self.oort.create_bucket(bucket_name)

        object_key = 'test-file.txt'
        object_data = b'Test data'
        self.oort.put_object(bucket_name, object_key, object_data)

        self.assertIn(object_key, self.oort.list_objects(bucket_name))

        self.oort.delete_object(bucket_name, object_key)
        self.oort.delete_bucket(bucket_name)
        print("...Passed\n")

    def test_get_object(self):
        print("Testing get_object...")
        bucket_name = 'test-get-object-bucket'
        self.oort.create_bucket(bucket_name)

        object_key = 'test-file.txt'
        object_data = b'Test data'
        self.oort.put_object(bucket_name, object_key, object_data)

        retrieved_data = self.oort.get_object(bucket_name, object_key)
        self.assertEqual(object_data, retrieved_data)

        self.oort.delete_object(bucket_name, object_key)
        self.oort.delete_bucket(bucket_name)
        print("...Passed\n")

    def test_delete_object(self):
        print("Testing delete_object...")
        bucket_name = 'test-delete-object-bucket'
        self.oort.create_bucket(bucket_name)

        object_key = 'test-file.txt'
        object_data = b'Test data'
        self.oort.put_object(bucket_name, object_key, object_data)

        self.oort.delete_object(bucket_name, object_key)
        self.assertNotIn(object_key, self.oort.list_objects(bucket_name))

        self.oort.delete_bucket(bucket_name)
        print("...Passed\n")

if __name__ == '__main__':
    unittest.main()
