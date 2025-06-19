class SyncService:
    def __init__(self, odoo_client, ysell_client):
        self.odoo_client = odoo_client
        self.ysell_client = ysell_client

    def sync_data(self):
        odoo_data = self.odoo_client.fetch_data()
        ysell_data = self.ysell_client.fetch_data()

        self._sync_to_ysell(odoo_data)
        self._sync_to_odoo(ysell_data)

    def _sync_to_ysell(self, odoo_data):
        for item in odoo_data:
            response = self.ysell_client.send_data(item)
            if not response.success:
                self._handle_error(response)

    def _sync_to_odoo(self, ysell_data):
        for item in ysell_data:
            response = self.odoo_client.send_data(item)
            if not response.success:
                self._handle_error(response)

    def _handle_error(self, response):
        # Implement error handling logic here
        print(f"Error: {response.error_message}")