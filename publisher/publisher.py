import abc

from subscriber.subscriber import Subscriber


class Publisher(abc.ABC):
    @abc.abstractmethod
    def notify_all(self, runs: int, wickets: int, over: float):
        pass

    @abc.abstractmethod
    def subscribe(self, subscriber: Subscriber):
        pass

    @abc.abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        pass
