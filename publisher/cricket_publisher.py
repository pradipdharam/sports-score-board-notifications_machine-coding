import abc

from subscriber.cricket_subscriber import CricketSubscriber


class CricketPublisher(abc.ABC):
    @abc.abstractmethod
    def notify_all(self, runs: int, wickets: int, over: float):
        pass

    @abc.abstractmethod
    def subscribe(self, subscriber: CricketSubscriber):
        pass

    @abc.abstractmethod
    def unsubscribe(self, subscriber: CricketSubscriber):
        pass

    @abc.abstractmethod
    @property
    def runs(self):
        pass

    @abc.abstractmethod
    @property
    def wickets(self):
        pass

    @abc.abstractmethod
    @property
    def over(self):
        pass
