from factory import Faker, SubFactory, DictFactory


class QueryStringParametersFactory(DictFactory):
    name = Faker("name")


class EventFactory(DictFactory):
    queryStringParameters = SubFactory(QueryStringParametersFactory)
