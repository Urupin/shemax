import unittest
from src.sync_service import SyncService
from src.odoo_client import OdooClient
from src.ysell_client import YsellClient

class TestSyncService(unittest.TestCase):

    def setUp(self):
        self.odoo_client = OdooClient()
        self.ysell_client = YsellClient()
        self.sync_service = SyncService(self.odoo_client, self.ysell_client)

    def test_sync_data(self):
        # Mock the methods in OdooClient and YsellClient
        self.odoo_client.get_data = lambda: {'id': 1, 'name': 'Test Product'}
        self.ysell_client.send_data = lambda data: data

        result = self.sync_service.sync_data()
        self.assertEqual(result, {'id': 1, 'name': 'Test Product'})

    def test_sync_error_handling(self):
        # Simulate an error in YsellClient
        self.odoo_client.get_data = lambda: {'id': 1, 'name': 'Test Product'}
        self.ysell_client.send_data = lambda data: (_ for _ in ()).throw(Exception("Ysell API error"))

        with self.assertRaises(Exception) as context:
            self.sync_service.sync_data()
        self.assertTrue("Ysell API error" in str(context.exception))

    def test_sync_with_empty_data(self):
        # Mock the methods to return empty data
        self.odoo_client.get_data = lambda: {}
        self.ysell_client.send_data = lambda data: data

        result = self.sync_service.sync_data()
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()