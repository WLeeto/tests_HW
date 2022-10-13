import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from Tests_HW.main import *


# FIXTURES_doc_num = [
#     ("2207 876234", True),
#     ("11-2", True),
#     ("10006", True),
#     ("223 322", False)
# ]
#
# FIXTURES_doc_owner_name = [
#     ("2207 876234", "Василий Гупкин"),
#     ("11-2", "Геннадий Покемонов"),
#     ("10006", "Аристарх Павлов"),
#     ("223 322", None)
# ]


class TestFunctions(unittest.TestCase):
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

    # Пример добавления параметров
    # @parameterized.expand(FIXTURES_doc_num)
    # def test_check_document_existance(self, a, exp_res):
    #     result = check_document_existance(a)
    #     self.assertEqual(result, exp_res)









