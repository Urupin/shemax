import unittest
from src.odoo_client import OdooClient

class TestOdooClient(unittest.TestCase):

    def setUp(self):
        self.client = OdooClient('https://odoo.example.com', 'db_name', 'username', 'password')

    def test_authentication(self):
        self.assertTrue(self.client.authenticate())

    def test_data_retrieval(self):
        data = self.client.get_data('model_name')
        self.assertIsInstance(data, list)

    def test_data_manipulation(self):
        response = self.client.create_record('model_name', {'field_name': 'value'})
        self.assertIn('id', response)

    def test_error_handling(self):
        with self.assertRaises(Exception):
            self.client.get_data('invalid_model_name')

if __name__ == '__main__':
    unittest.main()