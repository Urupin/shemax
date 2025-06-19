import unittest
from src.ysell_client import YsellClient

class TestYsellClient(unittest.TestCase):

    def setUp(self):
        self.client = YsellClient(api_key='test_api_key')

    def test_authentication(self):
        response = self.client.authenticate()
        self.assertTrue(response['success'])
        self.assertIn('token', response)

    def test_send_data(self):
        data = {'key': 'value'}
        response = self.client.send_data(data)
        self.assertTrue(response['success'])
        self.assertIn('response_id', response)

    def test_receive_response(self):
        response_id = 'test_response_id'
        response = self.client.receive_response(response_id)
        self.assertTrue(response['success'])
        self.assertIn('data', response)

    def test_error_handling(self):
        with self.assertRaises(Exception):
            self.client.send_data(None)

if __name__ == '__main__':
    unittest.main()