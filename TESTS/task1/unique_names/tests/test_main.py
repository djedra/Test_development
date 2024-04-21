from unittest import TestCase
from main import unique_names
from itertools import chain

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

output_list = unique_names(mentors).split(': ')
res = output_list[1].split(', ')


class TestUnique(TestCase):
    def test_mentor_name_present(self) -> None:
        self.assertIn('Олег', res)
        self.assertIn('Максим', res)
        self.assertIn('Эдгар', res)

    def test_mentor_lastname_not_present(self) -> None:
        self.assertNotIn('Юшина', res)
        self.assertNotIn('Нуруллин', res)
        self.assertNotIn('Хаслер', res)

    def test_all_names_present(self) -> None:
        for name in chain.from_iterable(mentors):
            self.assertIn(name.split()[0], res)

    def test_all_lastnames_not_present(self) -> None:
        for name in chain.from_iterable(mentors):
            self.assertNotIn(name.split()[1], res)

    def test_names_appear_only_once(self) -> None:
        for name in res:
            self.assertEqual(res.count(name), 1)

    def test_title(self) -> None:
        expected = 'Уникальные имена преподавателей'
        self.assertEqual(output_list[0], expected)

    def test_function_returns_string(self) -> None:
        self.assertIsInstance(unique_names(mentors), str)

    def test_empty_list(self) -> None:
        expected = 'Уникальные имена преподавателей: '
        self.assertEqual(unique_names([]), expected)

    def test_same_name(self) -> None:
        input = [['Александр Бардин', 'Александр Иванов'], []]
        expected = 'Уникальные имена преподавателей: Александр'
        self.assertEqual(unique_names(input), expected)


import pytest


class TestPyUnique():
    def test_mentor_name_present(self) -> None:
        assert 'Дмитрий' in res
        assert 'Филипп' in res
        assert 'Елена' in res

    def test_mentor_lastname_not_present(self) -> None:
        assert 'Корсаков' not in res
        assert 'Бочаров' not in res
        assert 'Шек' not in res

    def test_all_names_present(self) -> None:
        for name in chain.from_iterable(mentors):
            assert name.split()[0] in res

    def test_all_lastnames_not_present(self) -> None:
        for name in chain.from_iterable(mentors):
            assert name.split()[1] not in res

    def test_names_appear_only_once(self) -> None:
        for name in res:
            assert res.count(name) == 1

    def test_title(self) -> None:
        expected = 'Уникальные имена преподавателей'
        assert output_list[0] == expected

    def test_function_returns_string(self) -> None:
        assert isinstance(unique_names(mentors), str)

    def test_empty_list(self) -> None:
        expected = 'Уникальные имена преподавателей: '
        assert unique_names([]) == expected

    @pytest.mark.parametrize(
        'input, expected', [
            ([['Александр Бардин', 'Александр Иванов'], []],
             'Уникальные имена преподавателей: Александр'),
            ([['Евгений Шмаргунов'], ['Евгений Шек']],
             'Уникальные имена преподавателей: Евгений')
        ]
    )
    def test_same_name(self, input: list, expected: list) -> None:
        assert unique_names(input) == expected