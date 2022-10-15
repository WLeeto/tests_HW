import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from Tests_HW.main import *
from Tests_HW.ya_api import Ya_api


class TestFunctions(unittest.TestCase):
    def tearDown(self):
        with open('D:\Python\Tests_HW\ya_token.txt') as token:
            ya_token = token.read()
        api = Ya_api(ya_token)
        folder_name = "new"
        api.delete_folder(folder_name)

    # В этой функции input() не вынесен, чтобы попробовать patch
    def test_what_person(self):
        with patch('builtins.input', return_value='2207 876234'):
            assert input() == '2207 876234'
            result = "Василий Гупкин"
            self.assertEqual(what_person(), result)

    # В этой функции input() не вынесен, чтобы попробовать patch
    def test_what_shelf(self):
        with patch('builtins.input', return_value='2207 876234'):
            assert input() == '2207 876234'
            result = '\nДокумент № 2207 876234 находится на полке № 1'
            self.assertEqual(what_shelf(), result)

    def test_get_list(self):
        self.assertIsNotNone(get_list())

    def test_new_document(self):
        result = {'type': "1", 'number': "2", 'name': "3"}
        self.assertEqual(new_document("1", "2", "3"), result)

    def test_add_document(self):
        dict = {'type': "1", 'number': "2", 'name': "3"}
        result = 'Документ 2 на имя 3 добавлен на полку № 1'
        self.assertEqual(add_document(dict, "1"), result)

    def test_create_folder(self):
        with open('D:\Python\Tests_HW\ya_token.txt') as token:
            ya_token = token.read()
        api = Ya_api(ya_token)
        folder_name = "new"
        result = 201
        self.assertEqual(api.create_folder(folder_name), result)









