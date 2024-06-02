import abc
from abc import ABC


class Subscriber(ABC):
    """ Interface
    """

    @abc.abstractmethod
    def update(self):
        pass
