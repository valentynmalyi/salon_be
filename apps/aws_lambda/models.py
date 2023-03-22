from pydantic import BaseModel, Field


class QueryStringParameters(BaseModel):
    name: str


class Event(BaseModel):
    queryStringParameters: QueryStringParameters = Field(alias="query_string_parameters")

    class Config:
        allow_population_by_field_name = True
