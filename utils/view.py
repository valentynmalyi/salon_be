from abc import ABC, abstractmethod


class View(ABC):
    @staticmethod
    @abstractmethod
    def get_data(event: dict, context):
        pass
