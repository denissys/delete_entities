# delete_entities/tests/test_delete_entities.py

import unittest
from unittest.mock import Mock, patch
from delete_entities.main import main

class TestMainFunction(unittest.TestCase):

    def setUp(self):
        # Mock the entity and key to simulate the behavior of Datastore entities
        self.mock_entity = Mock()
        self.mock_key = Mock()
        self.mock_entity.key = self.mock_key

        # Mock the Datastore client, query, and fetch methods
        self.mock_datastore_client = Mock()
        self.mock_query = Mock()
        self.mock_query.fetch.return_value = [self.mock_entity]  # only one entity for testing purposes

    @patch('delete_entities.main.google.cloud.datastore.Client')
    def test_main_function_deletes_entity(self, MockDatastoreClient):
        # Mock the initialization of the Datastore client
        MockDatastoreClient.return_value = self.mock_datastore_client
        self.mock_datastore_client.query.return_value = self.mock_query

        main()

        # Assertions to check if the methods were called correctly
        MockDatastoreClient.assert_called_once()
        self.mock_query.add_filter.assert_called_with('country', '=', 'BR')
        self.mock_datastore_client.delete.assert_called_with(self.mock_key)

    @patch('delete_entities.main.google.cloud.datastore.Client')
    def test_main_function_retries_on_exception(self, MockDatastoreClient):
        # Force an exception to be raised when the client is initialized
        MockDatastoreClient.side_effect = Exception("Test exception")

        with self.assertLogs() as log_cm:
            main()

        # Check if the log contains the error message
        self.assertIn('ERROR:root:Erro: Test exception. Attempt 1 of 100', log_cm.output[0])


    @patch('delete_entities.main.google.cloud.datastore.Client')
    def test_main_function_max_retries(self, MockDatastoreClient):
        # Mock to always raise an exception to reach max retries
        MockDatastoreClient.side_effect = Exception("Test exception")

        with self.assertLogs() as log_cm:
            main()

        self.assertIn("Maximum number of attempts reached!", log_cm.output[-1])

if __name__ == "__main__":
    unittest.main()
