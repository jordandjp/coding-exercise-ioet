import abc

from src.model import Pay


class Formatter(abc.ABC):
    @abc.abstractmethod
    def format(self, pay: Pay):
        ...


class StringFormatter(Formatter):
    """Abstraction to format the output message with a given template"""

    def __init__(self, message_template, obj_keyword: str = "pay") -> None:
        self.message_template = message_template
        self.obj_keyword = obj_keyword

    def format(self, pay: Pay) -> str:
        return self.message_template.format_map({self.obj_keyword: pay})
