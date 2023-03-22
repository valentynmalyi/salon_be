from abc import ABC, abstractmethod

from pydantic import BaseModel, ValidationError


class View(ABC):
    event_cls: BaseModel

    @abstractmethod
    def get_data(self, event: BaseModel, context):
        pass

    def __call__(self, event_data: dict, context):
        try:
            event: BaseModel = self.event_cls.parse_obj(event_data)
        except ValidationError as e:
            return self.get_data_400(e)
        return self.get_data(event, context)

    @staticmethod
    def get_data_400(e: ValidationError) -> dict:
        return {
            'statusCode': 200,
            'body': e.json(),
        }
