import abc
from abc import ABC

from publisher.foot_ball_publisher import FootBallPublisher


class FootBallSubscriber(ABC):
    """ Interface
    """

    @abc.abstractmethod
    def update(self, publisher: FootBallPublisher):
        pass
