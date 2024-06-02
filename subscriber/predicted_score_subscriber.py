from publisher.publisher import Publisher
from subscriber.subscriber import Subscriber


class PredictedScoreSubscriber(Subscriber):
    __runs: int
    __wickets: int
    __over: float
    __publisher: Publisher

    def __init__(self, publisher: Publisher):
        self.__publisher = publisher

    def update(self):
        self.__runs = self.__publisher.runs
        self.__wickets = self.__publisher.wickets
        self.__over = self.__publisher.over
        # persists details in db
        # calculate projected score
        # update the board display with projected score
        print("PredictedScoreSubscriber: runs=", self.__runs, "wickets=", self.__wickets, "over=", self.__over)

    def subscribe(self, subscriber: Subscriber):
        self.__publisher.subscribe(self)

    def unsubscribe(self, subscriber: Subscriber):
        self.__publisher.unsubscribe(self)

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
    def publisher(self):
        return self.__publisher
