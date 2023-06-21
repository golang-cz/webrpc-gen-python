import unittest
import requests
import json
from unittest.mock import MagicMock
from client import (
    TestApi,
    WebrpcRequestFailedError,
    SendOneArgs,
    Simple,
    SendMultiArgs,
    GetEmptyArgs,
    GetSchemaErrorArgs,
    GetComplexArgs,
    GetErrorArgs,
    GetMultiArgs,
    GetOneArgs,
)


class TestApiClient(unittest.TestCase):

    def setUp(self):
        self.client = TestApi("http://localhost:8000")

    def test_GetEmpty(self):
        response_data = {}
        requests.post = MagicMock(return_value=MagicMock(json=MagicMock(return_value=response_data), ok=True))
        args = GetEmptyArgs()  # Empty args
        response = self.client.GetEmpty(args)
        requests.post.assert_called_once()

    def test_GetError(self):
        requests.post = MagicMock(side_effect=requests.exceptions.HTTPError("Request failed"))
        args = GetErrorArgs()  # Empty args
        with self.assertRaises(WebrpcRequestFailedError):
            self.client.GetError(args)

    def test_GetOne(self):
        response_data = {"one": {"id": 1, "name": "Item 1"}}
        requests.post = MagicMock(return_value=MagicMock(json=MagicMock(return_value=response_data), ok=True))
        args = GetOneArgs()  # Empty args
        response = self.client.GetOne(args)
        requests.post.assert_called_once()

    def test_SendOne(self):
        response_data = {}
        requests.post = MagicMock(return_value=MagicMock(json=MagicMock(return_value=response_data), ok=True))
        args = SendOneArgs(one=Simple(id=1, name="Item 1"))
        response = self.client.SendOne(args)
        requests.post.assert_called_once()
        self.assertEqual(response.to_dict(), response_data)

    def test_GetMulti(self):
        response_data = {'one': {'id': 1, 'name': 'Item 1'}, "two": {"id": 2, "name": "Item 2"}, "three": {"id": 3, "name": "Item 3"}}
        requests.post = MagicMock(return_value=MagicMock(json=MagicMock(return_value=response_data), ok=True))
        args = GetMultiArgs()  # Empty args
        response = self.client.GetMulti(args)
        requests.post.assert_called_once()

    def test_SendMulti(self):
        response_data = {}
        requests.post = MagicMock(return_value=MagicMock(json=MagicMock(return_value=response_data), ok=True))
        args = SendMultiArgs(
            one=Simple(id=1, name="Item 1"),
            two=Simple(id=2, name="Item 2"),
            three=Simple(id=3, name="Item 3")
        )
        response = self.client.SendMulti(args)
        requests.post.assert_called_once()
        self.assertEqual(response.to_dict(), response_data)


    def test_GetComplex(self):
        response_data = {
            "complex": {
                "meta": "data",
                "metaNestedExample": "nested data",
                "namesList": ["name1", "name2"],
                "numsList": [1, 2, 3],
                "doubleArray": [[1.0, 2.0], [3.0, 4.0]],
                "listOfMaps": [{"key1": "value1"}, {"key2": "value2"}],
                "listOfUsers": [
                    {"id": 1, "username": "User 1", "role": "Admin"},
                    {"id": 2, "username": "User 2", "role": "User"}
                ],
                "mapOfUsers": {
                    "user1": {"id": 1, "username": "User 1", "role": "Admin"},
                    "user2": {"id": 2, "username": "User 2", "role": "User"}
                },
                "user": {"id": 1, "username": "User 1", "role": "Admin"},
                "enum": "AVAILABLE"
            }
        }

        requests.post = MagicMock(return_value=MagicMock(json=MagicMock(return_value=response_data), ok=True))
        args = GetComplexArgs()
        response = self.client.GetComplex(args)
        requests.post.assert_called_once()

    def test_GetSchemaError(self):
        requests.post = MagicMock(side_effect=requests.exceptions.HTTPError("Request failed"))
        args = GetSchemaErrorArgs(code=-1)
        with self.assertRaises(WebrpcRequestFailedError):
            self.client.GetSchemaError(args)


if __name__ == "__main__":
    unittest.main()

