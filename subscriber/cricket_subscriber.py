import abc
from abc import ABC

from publisher.cricket_publisher import CricketPublisher


class CricketSubscriber(ABC):
    """ Interface
    """

    @abc.abstractmethod
    def update(self, publisher: CricketPublisher):
        pass
