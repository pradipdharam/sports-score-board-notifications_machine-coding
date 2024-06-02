import abc
from abc import ABC


class Subscriber(ABC):
    """ Interface
    """

    @abc.abstractmethod
    def update(self, runs: int, wickets: int, over: float):
        pass
