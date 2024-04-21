from unittest import TestCase, expectedFailure
from main import yandex_login

class TestLogin(TestCase):
    def test_correct_login_data(self) -> None:
        res = yandex_login(email='', password='')
        self.assertEqual(res, True)

    @expectedFailure
    def test_empty_email(self) -> None:
        res = yandex_login(email='', password='random')
        self.assertEqual(res, True)

    @expectedFailure
    def test_empty_password(self) -> None:
        res = yandex_login(email='random', password='')
        self.assertEqual(res, True)

    @expectedFailure
    def test_empty_login_data(self) -> None:
        res = yandex_login(email='', password='')
        self.assertEqual(res, True)