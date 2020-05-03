from unittest import TestCase

from DateParser import DateParser


class TestDateParser(TestCase):
    def test_parse_complete_date_separated_by_slashes(self):
        self.assertEqual(DateParser().reformat("3/9/2020"), "2020-09-03")

    def test_parse_complete_date_separated_by_spaces(self):
        self.assertEqual(DateParser().reformat("3 9 2020"), "2020-09-03")

    def test_parse_incomplete_date_separated_by_slashes(self):
        self.assertEqual(DateParser(default_year="2020").reformat("3/9"), "2020-09-03")

    def test_parse_incomplete_date_separated_by_spaces(self):
        self.assertEqual(DateParser(default_year="2020").reformat("3 9"), "2020-09-03")
