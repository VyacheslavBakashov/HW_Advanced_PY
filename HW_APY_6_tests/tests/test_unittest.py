import unittest
import app_for_test as app
from parameterized import parameterized
from unittest.mock import patch


class TestApp(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("setUp ==>")
    #
    # def tearDown(self) -> None:
    #     print("tearDown")

    @parameterized.expand([('10006', 'Аристарх Павлов'), ('11-21', None)])
    @patch('app_for_test.input')
    def test_get_doc_owner_name(self, doc, name, inp):
        inp.return_value = doc
        self.assertEqual(app.get_doc_owner_name(), name)

    @parameterized.expand([('10006', False), ('11-21', False)])
    def test_remove_doc_from_shelf(self, doc_num, bool_):
        app.remove_doc_from_shelf(doc_num)
        res = bool([dir_ for dir_ in app.directories.values() if doc_num in dir_])
        self.assertEqual(res, bool_)

    def test_remove_doc_from_shelf2(self, doc_num='10006'):
        app.remove_doc_from_shelf(doc_num)
        self.assertFalse(([dir_ for dir_ in app.directories.values() if doc_num in dir_]))

    @parameterized.expand([('4', True), ('2', False)])
    @patch('app_for_test.input')
    def test_add_new_shelf(self, shelf, bool_, inp):
        inp.return_value = shelf
        self.assertEqual(app.add_new_shelf(), (shelf, bool_))
        self.assertIsInstance(shelf, str)

    def test_append_doc_to_shelf(self, doc='11111', shelf='2'):
        app.append_doc_to_shelf(doc, shelf)
        self.assertIn(doc, app.directories[shelf])

    @patch('app_for_test.input')
    def test_delete_doc(self, doc):
        doc.return_value = '11-2'
        app.delete_doc()
        check_documents = [v for v in app.documents if doc in v.values()]
        check_shelves = [dir_ for dir_ in app.directories.values() if doc in dir_]
        self.assertEqual(all([check_documents, check_shelves]), False)

    @patch('app_for_test.input', side_effect=['2207 876234', '3'])
    def test_move_doc_to_shelf(self, inp):
        app.move_doc_to_shelf()
        self.assertIn('2207 876234', app.directories['3'])

    @patch('builtins.input')
    def test_add_new_doc(self, inp):
        new_doc = ['15-2', 'invoice', 'Петр Петров', '2']
        inp.side_effect = new_doc
        app.add_new_doc()
        new_val = [app.documents[-1]['number'], app.documents[-1]['type'], app.documents[-1]['name']]
        self.assertEqual(new_doc[:3], new_val)
        self.assertIn(new_doc[0], app.directories[new_doc[-1]])


