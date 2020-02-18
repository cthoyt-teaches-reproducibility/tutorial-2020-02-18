import unittest

import rcr
import os

HERE = os.path.dirname(__file__)
MY_TEST_DATA_PATH = os.path.join(HERE, 'test_data.tsv')


class TestRcr(unittest.TestCase):
    """This tests all of our shit."""

    def test_who_i_am(self):
        my_name = rcr.get_who_am_i()

        # assert isinstance(my_name, str)
        self.assertIsInstance(
            my_name,
            str,
            msg='My name was not a string',
        )

        # assert my_name == 'Jean Val Jean'
        self.assertEqual('Jean Val Jean', my_name, msg='Got wrong name')

    def test_prisoner_number(self):
        n = rcr.get_my_prisoner_number()
        self.assertIsNotNone(n)
        self.assertIsInstance(n, int)
        self.assertEqual(n, 24601)
