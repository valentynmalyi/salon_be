from utils.view import View

from apps.aws_lambda import factories as aws_lambda_factories
from apps.asd import models


class Asd(View):
    @staticmethod
    def get_data(event: dict, context):
        name = event["queryStringParameters"]["name"]
        person = models.Person.objects.get_or_create(name=name)
        return {
            'statusCode': 200,
            'body': str(person)
        }

    @classmethod
    def get(cls, event: dict, context):
        view = cls()
        return view.get_data(event, context)


if __name__ == '__main__':
    aws_event: dict = aws_lambda_factories.EventFactory()
    print(Asd.get(aws_event, None))
