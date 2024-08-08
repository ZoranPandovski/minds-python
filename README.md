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
from minds.models import DataSourceConfig, ConnectionArgs

# get your API_KEY from https://mdb.ai/minds
MIND_API_KEY = "YOUR_API_KEY"
client = Client(MIND_API_KEY)

# use MindsDB's demo Datasource
data_source_config = DemoDataSources.house_sales()

# Create a new mind
mind = client.mind.create(name=f'mind_{uuid.uuid4()}', data_source_configs=[data_source_config])

print(f"{mind} was created successfully. You can now use this Mind using the OpenAI chat/completitions")
```

You can use OpenAI SDK to test the above Mind:

```python
from openai import OpenAI

client = OpenAI(
    api_key= MIND_API_KEY,
    base_url='https://llm.mdb.ai/'
)

# chat with the Mind you created
completion = client.chat.completions.create(
    model=mind['name'],
    messages=[
        {'role': 'user', 'content': 'What is the Average house price?'}
    ],
    stream=False
)

print('Answering the question may take up to 10 seconds...')
print(completion.choices[0].message.content)

```