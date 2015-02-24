import datetime
import unittest

from django.utils import timezone
from models import Task
from training.bowling import Game


class TaskTests(unittest.TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Task(created=time)
        self.assertEqual(future_question.was_published_recently(), False)


class TaskTests2(unittest.TestCase):

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Task(created=time)
        self.assertEqual(old_question.was_published_recently(), False)


class TaskTests3(unittest.TestCase):

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Task(created=time)
        self.assertEqual(recent_question.was_published_recently(), True)


class BowlingTest(unittest.TestCase):

    def test_score(self):
        SCORE_VARIANTS = {
            "8/9-X X 6/4/X 8-X XXX": 194,
            '--------------------': 0,
            '-----1------1-------': 2,
            'XXXXXXXXXXXX': 300,
            "1/1/1/1/1/1/1/1/1/1/1/1": 110,
            '7-7-7-7-7-7-7-7-7-7-': 70,
            'X7/15X-88/-6XXXXX': 169,
            'X7/9-X-88/-6XXX81': 167,
            }
        for k, v in SCORE_VARIANTS.items():
            game = Game(k)
            self.assertEqual(max(game.get_frame_result()), v)


def suite():

    suite = unittest.TestSuite()
    suite.addTest(TaskTests())
    suite.addTest(TaskTests2())

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)


# DJANGO_SETTINGS_MODULE=mysite.settings nosetests training/tests.py:BowlingTest


