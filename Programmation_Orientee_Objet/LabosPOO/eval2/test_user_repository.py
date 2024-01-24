import unittest
from files import FileUserRepository


class MyTestCase(unittest.TestCase):
    def test_something(self):
        repository = FileUserRepository("user_repository.csv")
        liste = repository.get_users_from_csv()

        found = repository.get_users_matching(liste, "password")
        self.assertListEqual(['P100077', 'P981234'], found)

        found2 = repository.get_users_matching(liste, "rien à voir")
        self.assertListEqual([], found2)

