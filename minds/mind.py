from openai import OpenAI
from typing import List, Dict, Any
from .models import DataSourceConfig
from minds.exceptions import MindsAPIError

class Mind:
    def __init__(self, client):
        self.client = client

    def create(
        self, name: str, data_source_configs: List[DataSourceConfig]
    ) -> Dict[str, Any]:
        """
        Create a new Mind with the given name and data source configurations.

        :param name: Name of the mind to be created
        :param data_source_configs: List of DataSourceConfig instances
        :return: Response from the API as a dictionary
        """
        data = {
            "name": name,
            "data_source_configs": [config.dict() for config in data_source_configs],
        }
        return self.client._request("POST", "/minds", data)

    def chat(self, mind_name: str, message: str) -> str:
        """
        This function sends a message to the Mind and returns the response.
        :param mind_name: Name of the Mind model to chat with
        :param message: The message to send to the Mind
        :return: The response message from the Mind
        :raises OpenAIError: If there is an error with the OpenAI request
        """
        try:
            openai_client = OpenAI(
                api_key=self.client.api_key,
                base_url='https://llm.mdb.ai/'
            )

            completion = openai_client.chat.completions.create(
                model=mind_name,
                messages=[
                    {'role': 'user', 'content': message}
                ],
                stream=False
            )
            return completion.choices[0].message.content
        except MindsAPIError as e:
            raise MindsAPIError(f"Failed to chat with the Mind: {e}")