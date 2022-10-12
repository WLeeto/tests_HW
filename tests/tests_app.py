import unittest

from parameterized import parameterized

from unittest.mock import patch, Mock

from Tests_HW.app import *
from Tests_HW.main import *


FIXTURES_doc_num = [
    ("2207 876234", True),
    ("11-2", True),
    ("10006", True),
    ("223 322", False)
]

FIXTURES_doc_owner_name = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("223 322", None)
]

class TestFunctions(unittest.TestCase):
    @parameterized.expand(FIXTURES_doc_num)
    def test_check_document_existance(self, a, exp_res):
        result = check_document_existance(a)
        self.assertEqual(result, exp_res)

    @patch.object(".app.user_doc_number", return_value="2207 876234")
    def test_get_doc_owner_name(self):
        result = get_doc_owner_name()
        self.assertEqual(result, "Василий Гупкин")



