import unittest
from classes.user_repository import UserRepository


class UserRepositoryTest(unittest.TestCase):
    def test_get_user_for_pwd_bonjour(self):
        repository = UserRepository()

        found = repository.get_users_matching("password")
        self.assertListEqual(['P100077', 'P981234'], found)

    def test_returns_empty_list_on_no_password_match(self):
        repository = UserRepository()

        found = repository.get_users_matching("rien à voir")
        self.assertEqual(0, len(found))
