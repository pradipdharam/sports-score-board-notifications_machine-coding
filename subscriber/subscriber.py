import abc
from abc import ABC

from publisher.publisher import Publisher


class Subscriber(ABC):
    """ Interface
    """

    @abc.abstractmethod
    def update(self, publisher: Publisher):
        pass
