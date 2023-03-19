import utils.django

from apps.aws_lambda import factories as aws_lambda_factories
from apps.asd import models


def lambda_handler(event: dict, context):
    name = event["queryStringParameters"]["name"]
    person = models.Person.objects.get_or_create(name=name)
    return {
        'statusCode': 200,
        'body': str(person)
    }


if __name__ == '__main__':
    event: dict = aws_lambda_factories.EventFactory()
    lambda_handler(event, None)
