from unittest import TestCase, expectedFailure
from main import solution


class TestEquation(TestCase):
    def test_positive_discriminant(self) -> None:
        a = 1
        b = 2
        c = -3
        res = solution(a, b, c)
        expected = (1, -3)
        self.assertEqual(res, expected)

    def test_zero_discriminant(self) -> None:
        a = 1
        b = -10
        c = 25
        res = solution(a, b, c)
        expected = 5
        self.assertEqual(res, expected)

    def test_negative_discriminant(self) -> None:
        a = 1
        b = -5
        c = 7
        res = solution(a, b, c)
        expected = None
        self.assertEqual(res, expected)

    def test_fractional_number(self) -> None:
        a = 4
        b = -10
        c = 1
        res = solution(a, b, c)
        expected = (2.3956439, 0.1043561)
        self.assertAlmostEqual(res[0], expected[0])
        self.assertAlmostEqual(res[1], expected[1])

    @expectedFailure
    def test_two_arguments(self) -> None:
        a = 3
        b = 4
        res = solution(a, b)
        self.assertIsNotNone(res)


import pytest


class TestPyEquation():
    @pytest.mark.parametrize(
        'a, b, c, expected', [
            (1, 2, -3, (1, -3)),
            (2, -1, -15, (3, -2.5)),
            (1, -5, 6, (3, 2))
        ]
    )
    def test_positive_discriminant(self, a: float, b: float,
                                   c: float, expected: tuple):
        res = solution(a, b, c)
        assert res == expected

    def test_zero_discriminant(self):
        a = 1
        b = -10
        c = 25
        res = solution(a, b, c)
        expected = 5
        assert res == expected

    def test_negative_discriminant(self):
        a = 1
        b = -5
        c = 7
        res = solution(a, b, c)
        expected = None
        assert res == expected

    @pytest.mark.parametrize(
        'a, b, c, expected', [
            (4, -10, 1, (2.3956439, 0.1043561)),
            (11, 2, -8, (0.7667256, -0.9485437)),
            (98, 28, 2, -0.1428571)
        ]
    )
    def test_fractional_number(self, a: float, b: float,
                               c: float, expected: tuple):
        res = solution(a, b, c)
        if isinstance(expected, tuple):
            assert res[0] == pytest.approx(expected[0])
            assert res[1] == pytest.approx(expected[1])
        else:
            assert res == pytest.approx(expected)

    @pytest.mark.xfail
    def test_two_arguments(self):
        a = 3
        b = 4
        res = solution(a, b)
        assert res is not None