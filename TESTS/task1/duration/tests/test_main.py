from unittest import TestCase, expectedFailure
from main import course_duration
from itertools import chain
import re

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

res = course_duration(courses, mentors, durations)


class TestDuration(TestCase):
    def test_correct_duration(self) -> None:
        for course_dur in zip(courses, durations):
            self.assertIn(f'{course_dur[0]} - {course_dur[1]} месяцев', res)

    def test_no_mentor_names(self) -> None:
        for name in chain.from_iterable(mentors):
            for name_or_last_name in name.split():
                self.assertNotIn(name_or_last_name, res)

    def test_ascending_order(self) -> None:
        pattern = re.compile(r'\d+')
        match = re.findall(pattern, res)
        self.assertEqual(match, sorted(match))

    def test_courses_appear_only_once(self) -> None:
        pattern = re.compile(r'\w+-разработчик\s[\w\s]+\w')
        match = re.findall(pattern, res)
        self.assertEqual(sorted(match), sorted(courses))

    @expectedFailure
    def test_empty_mentors_list(self) -> None:
        empty_mentors_res = course_duration(courses, [], durations)
        self.assertEqual(empty_mentors_res, res)


import pytest


class TestPyDuration():
    def test_correct_duration(self) -> None:
        for course_dur in zip(courses, durations):
            assert f'{course_dur[0]} - {course_dur[1]} месяцев' in res

    def test_no_mentor_names(self) -> None:
        for name in chain.from_iterable(mentors):
            for name_or_last_name in name.split():
                assert name_or_last_name not in res

    def test_ascending_order(self) -> None:
        pattern = re.compile(r'\d+')
        match = re.findall(pattern, res)
        assert match == sorted(match)

    def test_courses_appear_only_once(self) -> None:
        pattern = re.compile(r'\w+-разработчик\s[\w\s]+\w')
        match = re.findall(pattern, res)
        assert sorted(match) == sorted(courses)

    @pytest.mark.xfail
    def test_empty_mentors_list(self) -> None:
        empty_mentors_res = course_duration(courses, [], durations)
        assert empty_mentors_res == res