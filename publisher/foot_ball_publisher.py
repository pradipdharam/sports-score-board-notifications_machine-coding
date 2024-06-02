import abc

from subscriber.subscriber import Subscriber


class FootBallPublisher(abc.ABC):
    @abc.abstractmethod
    def notify_all(self, goal1: int, goal2: int, duration: float):
        pass

    @abc.abstractmethod
    def subscribe(self, subscriber: Subscriber):
        pass

    @abc.abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        pass

    @abc.abstractmethod
    @property
    def goal1(self):
        pass

    @abc.abstractmethod
    @property
    def goal2(self):
        pass

    @abc.abstractmethod
    @property
    def duration(self):
        pass
