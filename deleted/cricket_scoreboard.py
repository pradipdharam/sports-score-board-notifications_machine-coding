from projected_score_board import ProjectedScoreBoard
from run_rate_board import RunRateBoard
from top_discussion_board import TopDiscussionBoard


class CricketScoreBoard:
    __runs: int
    __wickets: int
    __over: float
    __projected_score_board: ProjectedScoreBoard
    __run_rate_board: RunRateBoard
    __top_discussion_board: TopDiscussionBoard

    def update_score(self, runs: int, wickets: int, over: float):
        self.__runs = runs
        self.__wickets = wickets
        self.__over = over
        self.__projected_score_board.update(runs, wickets, over)
        self.__run_rate_board.update(runs, wickets, over)
        self.__top_discussion_board.update(runs, wickets, over)

    @property
    def runs(self):
        return self.__runs

    @property
    def wickets(self):
        return self.__wickets

    @property
    def over(self):
        return self.__over
