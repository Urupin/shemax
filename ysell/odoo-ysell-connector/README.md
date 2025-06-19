# Odoo Ysell Connector

This project is a connector between Odoo 17 and the Ysell service, facilitating data synchronization through their respective APIs.

## Project Structure

```
odoo-ysell-connector
├── src
│   ├── odoo_client.py       # Handles communication with the Odoo 17 API
│   ├── ysell_client.py      # Manages interactions with the Ysell API
│   ├── sync_service.py      # Orchestrates synchronization between Odoo and Ysell
│   └── utils.py             # Contains utility functions for common tasks
├── tests
│   ├── test_odoo_client.py  # Unit tests for the OdooClient class
│   ├── test_ysell_client.py # Unit tests for the YsellClient class
│   └── test_sync_service.py # Unit tests for the SyncService class
├── requirements.txt         # Lists project dependencies
├── README.md                # Project documentation
└── .gitignore               # Specifies files to ignore by Git
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/odoo-ysell-connector.git
   cd odoo-ysell-connector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Configure the Odoo and Ysell API credentials in your environment or configuration file.
2. Use the `SyncService` class to initiate synchronization between Odoo and Ysell.

## API Details

Refer to the following documentation for details on the Odoo and Ysell APIs:

- [Odoo API Documentation](https://www.odoo.com/documentation/17.0/api.html)
- [Ysell API Documentation](https://wiki.ysell.pro/doku.php?id=ru:api_start)

## Running Tests

To run the unit tests, execute the following command:
```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.