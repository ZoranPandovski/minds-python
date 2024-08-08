import unittest
from unittest.mock import patch, Mock
from minds.client import Client

class TestClient(unittest.TestCase):
      
    def setUp(self):
        self.api_key = 'test_api_key'
        self.client = Client(api_key=self.api_key)

    
    @patch('requests.request')
    def test_request_success(self, mock_request):
        mock_response = Mock()
        mock_response.json.return_value = {'key': 'value'}
        mock_request.return_value = mock_response

        response = self.client._request('GET', '/test')

        mock_request.assert_called_once_with('GET', 'https://llm.mdb.ai/test', headers=self.client.headers, json=None)
        self.assertEqual(response, {'key': 'value'})
