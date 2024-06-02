from typing import List

from publisher.publisher import Publisher
from subscriber.subscriber import Subscriber


class ESPNCricketScoreBoardPublisher(Publisher):
    __runs: int
    __wickets: int
    __over: float
    __subscribers: List[Subscriber]

    def __init__(self):
        self.__subscribers = []

    def notify_all(self, runs: int, wickets: int, over: float):
        self.__runs = runs
        self.__wickets = wickets
        self.__over = over
        for subscriber in self.__subscribers:
            subscriber.update(self)

    def subscribe(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.__subscribers.remove(subscriber)

    @property
    def runs(self):
        return self.__runs

    @property
    def wickets(self):
        return self.__wickets

    @property
    def over(self):
        return self.__over
