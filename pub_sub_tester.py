from typing import List

from publisher.cricket_score_board_publisher import CricketScoreBoardPublisher
from publisher.cricket_publisher import CricketPublisher
from subscriber.predicted_score_subscriber import PredictedScoreSubscriber
from subscriber.run_rate_subscriber import RunRateSubscriber
from subscriber.subscriber import Subscriber
from subscriber.top_discussion_subscriber import TopDiscussionSubscriber


class PubSubTester:
    @staticmethod
    def test():
        """Testing the observer design pattern implementation.
        Publisher subscribers testing
        """
        cricket_score_board_publisher = CricketScoreBoardPublisher()

        predicted_score_subscriber = PredictedScoreSubscriber(cricket_score_board_publisher)
        run_rate_subscriber = RunRateSubscriber(cricket_score_board_publisher)
        top_discussion_subscriber = TopDiscussionSubscriber(cricket_score_board_publisher)

        PubSubTester.connect([predicted_score_subscriber,
                              run_rate_subscriber,
                              top_discussion_subscriber],
                             cricket_score_board_publisher)

        cricket_score_board_publisher.notify_all(100, 2, 20.1)
        # unsubscribe top_discussion_subscriber from its publisher
        top_discussion_subscriber.publisher.unsubscribe(top_discussion_subscriber)
        cricket_score_board_publisher.notify_all(110, 3, 21.1)

        """Output as below lines.
        PredictedScoreSubscriber: runs = 100 wickets = 2 over = 20.1
        RunRateSubscriber: runs = 100 wickets = 2 over = 20.1
        TopDiscussionSubscriber: runs = 100 wickets = 2 over = 20.1
        PredictedScoreSubscriber: runs = 110 wickets = 3 over = 21.1
        RunRateSubscriber: runs = 110 wickets = 3 over = 21.1
        """

    @staticmethod
    def connect(subscribers: List[Subscriber],
                publisher: CricketPublisher):
        """subscribers_subscribe_to_publisher or connect publisher & subscriber
        """
        for subscriber in subscribers:
            publisher.subscribe(subscriber)


if __name__ == '__main__':
    PubSubTester.test()
