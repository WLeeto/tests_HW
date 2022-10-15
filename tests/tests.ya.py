import unittest
from Tests_HW.ya_api import Ya_api


class TestFunctions(unittest.TestCase):
    def test_create_folder(self):
        with open('ya_token.txt') as token:
            ya_token = token.read()
        api = Ya_api(ya_token)
        folder_name = "new"
        result = 201
        self.assertEqual(api.create_folder(folder_name), result)