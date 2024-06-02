from typing import Final

from cricket_scoreboard import CricketScoreBoard


class TopDiscussionBoard:
    """ To display the scores on the board
    """
    __runs: int
    __wickets: int
    __over: float
    __cricket_score_board: Final[CricketScoreBoard]

    def __init__(self, cricket_score_board: CricketScoreBoard):
        self.__cricket_score_board = cricket_score_board

    def update(self, runs: int, wickets: int, over: float):
        is_updated = False
        updated_runs = self.__cricket_score_board.runs
        if updated_runs != self.__runs:
            self.__runs = updated_runs
            is_updated = True

        updated_wickets = self.__cricket_score_board.wickets
        if updated_wickets != self.__wickets:
            self.__wickets = updated_wickets
            is_updated = True

        updated_overs = self.__cricket_score_board.over
        if updated_overs != self.__over:
            self.__over = updated_overs
            is_updated = True

        if is_updated:
            # persists details in db
            # calculate projected score
            # update the board display with projected score
            pass
