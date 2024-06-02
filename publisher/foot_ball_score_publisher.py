from typing import List

from publisher.cricket_publisher import FootBallPublisher
from subscriber.cricket_subscriber import CricketSubscriber


class FootBallScorePublisher(FootBallPublisher):
    __goal1: int
    __goal2: int
    __duration: float
    __subscribers: List[CricketSubscriber]

    def __init__(self):
        self.__subscribers = []

    def notify_all(self, goal1: int, goal2: int, duration: float):
        self.__goal1 = goal1
        self.__goal1 = goal2
        self.__duration = duration
        for subscriber in self.__subscribers:
            subscriber.update(self)

    def subscribe(self, subscriber: CricketSubscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: CricketSubscriber):
        self.__subscribers.remove(subscriber)

    @property
    def goal1(self):
        return self.__goal1

    @property
    def goal2(self):
        return self.__goal2

    @property
    def duration(self):
        return self.__duration
