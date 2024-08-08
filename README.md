# Minds SDK

The Minds SDK provides an interface for interacting with the Minds API, allowing you to create and manage minds and data sources.

## Installation

To install the SDK, use Poetry:

```bash
git clone https://github.com/ZoranPandovski/minds-python.git
poetry install
```

# Usage

Here's an example of how to use the Minds SDK:

```python
import uuid
from minds.client import Client
from minds.models import DemoDataSources

# get your API_KEY from https://mdb.ai/minds
client = Client("YOUR_API_KEY")

# use MindsDB's demo Datasource
data_source_config = DemoDataSources.house_sales()

# Create a new mind and chat
mind = client.mind.create(name=f'mind_{uuid.uuid4()}', data_source_configs=[data_source_config])
response = client.mind.chat(mind['name'], "What is the Average price of the house?")

print(response)
```
