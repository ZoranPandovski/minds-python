from pydantic import BaseModel, Field, validator
from typing import List, Dict

class ConnectionArgs(BaseModel):
    user: str
    password: str
    host: str
    port: int
    database: str
    schema: str

class DataSourceConfig(BaseModel):
    type: str
    connection_args: ConnectionArgs
    description: str

    @validator('type')
    def type_must_be_valid(cls, v):
        if v not in ['postgres', 'mysql']:
            raise ValueError('Invalid data source type')
        return v