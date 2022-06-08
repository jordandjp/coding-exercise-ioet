import abc


class Handler(abc.ABC):
    @abc.abstractmethod
    def emit(self, message: str) -> None:
        ...


class StreamHandler(Handler):
    def __init__(self, file) -> None:
        self.file = file

    def emit(self, message: str) -> None:
        self.file.write(message + "\n")
        self.file.flush()
