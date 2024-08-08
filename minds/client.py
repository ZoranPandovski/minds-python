import requests
from typing import Optional, Dict, Any
from .mind import Mind
from .exceptions import MindsAPIError


class Client:
    BASE_URL = 'https://llm.mdb.ai'
    
    def __init__(self, api_key: str = None, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = self._construct_headers()
        self.mind = Mind(self)

    def _construct_headers(self) -> Dict[str, str]:
        """
        Construct headers for the API requests.

        :return: Dictionary containing headers
        """
        if not self.api_key:
            raise ValueError("API key must be provided.")
        return {
            'Content-Type': self.CONTENT_TYPE,
            'Authorization': f'Bearer {self.api_key}'
        }

    def _request(self, method: str, endpoint: str, data: Optional[dict] = None):
        """
        Make a request to the Mind API.

        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: API endpoint
        :param data: Optional data to send in the request
        :return: Response JSON as a dictionary
        :raises MindsAPIError: Custom error for API issues
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise MindsAPIError(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise MindsAPIError(f"An error occurred: {err}")
        
        return response.json()