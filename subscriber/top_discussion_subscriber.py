from subscriber.subscriber import Subscriber


class PredictedScoreSubscriber(Subscriber):
    __runs: int
    __wickets: int
    __over: float

    def update(self, runs: int, wickets: int, over: float):
        self.__runs = runs
        self.__wickets = wickets
        self.__over = over
        # persists details in db
        # calculate projected score
        # update the board display with projected score
