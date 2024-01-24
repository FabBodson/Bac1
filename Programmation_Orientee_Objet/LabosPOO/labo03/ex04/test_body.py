import unittest
from ex02.mass import Mass
from ex03.length import Length
from ex04.body import Body


class BodyTest(unittest.TestCase):

    def test_body_with_none(self):
        body = Body(None, None)
        expected_weight = Mass(0)
        expected_length = Length(0)

        self.assertEqual(expected_weight, body.weight)
        self.assertEqual(expected_length, body.height)

    def test_bmi(self):
        body = Body(Mass(50.0), Length(1.60))

        expected_bmi = 50.0 / (1.60**2)

        self.assertEqual(expected_bmi, body.get_bmi())