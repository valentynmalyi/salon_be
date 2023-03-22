from utils.view import View

from apps.aws_lambda import factories as aws_lambda_factories, models as aws_lambda_models
from apps.asd import models


class Asd(View):
    event_cls = aws_lambda_models.Event

    def get_data(self, event: aws_lambda_models.Event, context):
        name = event.queryStringParameters.name
        person = models.Person.objects.get_or_create(name=name)
        return {
            'statusCode': 200,
            'body': str(person)
        }


asd = Asd()

if __name__ == '__main__':
    aws_event: dict = aws_lambda_factories.EventFactory()
    print(asd(aws_event, None))
