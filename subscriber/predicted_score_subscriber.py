from publisher.cricket_score_board_publisher import CricketScoreBoardPublisher
from subscriber.subscriber import Subscriber


class PredictedScoreSubscriber(Subscriber):
    __runs: int
    __wickets: int
    __over: float
    __cricket_score_board_publisher: CricketScoreBoardPublisher

    def update(self, runs: int, wickets: int, over: float):
        self.__runs = runs
        self.__wickets = wickets
        self.__over = over
        # persists details in db
        # calculate projected score
        # update the board display with projected score

    def subscribe(self, subscriber: Subscriber):
        self.__cricket_score_board_publisher.subscribe(self)

    def unsubscribe(self, subscriber: Subscriber):
        self.__cricket_score_board_publisher.unsubscribe(self)
