from typing import List

from publisher.cricket_publisher import CricketPublisher
from subscriber.cricket_subscriber import CricketSubscriber


class SonyCricketScoreBoardPublisher(CricketPublisher):
    __runs: int
    __wickets: int
    __over: float
    __subscribers: List[CricketSubscriber]

    def __init__(self):
        self.__subscribers = []

    def notify_all(self, runs: int, wickets: int, over: float):
        self.__runs = runs
        self.__wickets = wickets
        self.__over = over
        for subscriber in self.__subscribers:
            subscriber.update(self)

    def subscribe(self, subscriber: CricketSubscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: CricketSubscriber):
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
