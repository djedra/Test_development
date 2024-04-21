from itertools import chain
import re


def course_duration(courses: list, mentors: list, durations: list) -> str:
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}

    for id, course in enumerate(courses_list):
        key = course["duration"]
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)

    durations_dict = dict(sorted(durations_dict.items()))

    output_string = ''
    for duration, id in durations_dict.items():
        for id1 in id:
            output_string += f'{courses[id1]} - {duration} месяцев\n'

    return output_string.strip()