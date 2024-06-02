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
