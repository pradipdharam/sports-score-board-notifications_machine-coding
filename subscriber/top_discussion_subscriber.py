from typing import List

from publisher.publisher import Publisher
from subscriber.subscriber import Subscriber


class TopDiscussionSubscriber(Subscriber):
    __runs: int
    __wickets: int
    __over: float
    __publishers: List[Publisher]

    def __init__(self, publishers: List[Publisher]):
        self.__publishers = publishers
        for publisher in self.__publishers:
            publisher.subscribe(self)

    def update(self, publisher: Publisher):
        self.__runs = publisher.runs
        self.__wickets = publisher.wickets
        self.__over = publisher.over
        # persists details in db
        # calculate projected score
        # update the board display with projected score
        print("TopDiscussionSubscriber: runs=", self.__runs, "wickets=", self.__wickets, "over=", self.__over)

    def subscribe(self, publisher: Publisher):
        """Add one publisher for this subscriber
        """
        self.__publishers.append(publisher)
        publisher.subscribe(self)

    def unsubscribe(self, publisher: Publisher):
        """Remove one publisher for this subscriber
        """
        self.__publishers.remove(publisher)
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
    def publishers(self):
        return self.__publishers
