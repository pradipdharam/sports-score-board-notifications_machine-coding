from typing import List

from publisher.publisher import Publisher
from subscriber.subscriber import Subscriber


class FootBallScorePublisher(Publisher):
    __goal1: int
    __goal2: int
    __duration: float
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
        raise RuntimeError("Not allowed for FootBallScorePublisher")

    @property
    def wickets(self):
        raise RuntimeError("Not allowed for FootBallScorePublisher")

    @property
    def over(self):
        raise RuntimeError("Not allowed for FootBallScorePublisher")

    @property
    def goal1(self):
        return self.__goal1

    @property
    def goal2(self):
        return self.__goal2

    @property
    def duration(self):
        return self.__duration
