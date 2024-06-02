from typing import List

from publisher.cricket_publisher import CricketPublisher
from publisher.foot_ball_publisher import FootBallPublisher
from subscriber.cricket_subscriber import CricketSubscriber
from subscriber.foot_ball_subscriber import FootBallSubscriber


class PredictedScoreSubscriber(CricketSubscriber, FootBallSubscriber):
    __runs: int
    __wickets: int
    __over: float
    __goal1: int
    __goal2: int
    __duration: float
    __cricket_publishers: List[CricketPublisher]
    __foot_ball_publishers: List[CricketPublisher]

    def __init__(self, cricket_publishers: List[CricketPublisher],
                 foot_ball_publishers: List[FootBallPublisher]):
        self.__cricket_publishers = cricket_publishers
        self.__foot_ball_publishers = foot_ball_publishers
        for cricket_publisher in self.__cricket_publishers:
            cricket_publisher.subscribe(self)
        for foot_ball_publisher in self.__foot_ball_publishers:
            foot_ball_publisher.subscribe(self)

    def update(self, publisher: CricketPublisher):
        self.__runs = publisher.runs
        self.__wickets = publisher.wickets
        self.__over = publisher.over
        # persists details in db
        # calculate projected score
        # update the board display with projected score
        print("PredictedScoreSubscriber: runs=", self.__runs, "wickets=", self.__wickets, "over=", self.__over)

    def update(self, publisher: FootBallPublisher):
        self.__goal1 = publisher.goal1
        self.__goal1 = publisher.goal2
        self.__duration = publisher.duration
        # persists details in db
        # calculate projected score
        # update the board display with projected score
        print("PredictedScoreSubscriber: runs=", self.__runs, "wickets=", self.__wickets, "over=", self.__over)

    def subscribe(self, publisher: CricketPublisher):
        """Add one publisher for this subscriber
        """
        self.__cricket_publishers.append(publisher)
        publisher.subscribe(self)

    def unsubscribe(self, publisher: CricketPublisher):
        """Remove one publisher for this subscriber
        """
        self.__cricket_publishers.remove(publisher)
        publisher.unsubscribe(self)

    def subscribe(self, publisher: FootBallPublisher):
        """Add one publisher for this subscriber
        """
        self.__foot_ball_publishers.append(publisher)
        publisher.subscribe(self)

    def unsubscribe(self, publisher: FootBallPublisher):
        """Remove one publisher for this subscriber
        """
        self.__foot_ball_publishers.remove(publisher)
        publisher.unsubscribe(self)

    @property
    def runs(self):
        return self.__runs

    @property
    def wickets(self):
        return self.__wickets

    @property
    def over(self):
        return self.__over

    @property
    def cricket_publishers(self):
        return self.__cricket_publishers

    @property
    def foor_ball_publishers(self):
        return self.__foot_ball_publishers

    @property
    def goal1(self):
        return self.__goal1

    @property
    def goal12(self):
        return self.__goal2

    @property
    def duration(self):
        return self.__duration
