from publisher.publisher import Publisher
from subscriber.subscriber import Subscriber


class RunRateSubscriber(Subscriber):
    __runs: int
    __wickets: int
    __over: float
    __publisher: Publisher

    def update(self, runs: int, wickets: int, over: float):
        self.__runs = runs
        self.__wickets = wickets
        self.__over = over
        # persists details in db
        # calculate projected score
        # update the board display with projected score

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
