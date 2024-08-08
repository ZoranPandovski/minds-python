from typing import List, Dict, Any
from .models import DataSourceConfig

class Mind:
    def __init__(self, client):
        self.client = client
    
    def create(self, name: str, data_source_configs: List[DataSourceConfig]) -> Dict[str, Any]:
        """
        Create a new Mind with the given name and data source configurations.

        :param name: Name of the mind to be created
        :param data_source_configs: List of DataSourceConfig instances
        :return: Response from the API as a dictionary
        """
        data = {
            'name': name,
            'data_source_configs': [config.dict() for config in data_source_configs]
        }
        return self.client._request("POST", "/minds", data)