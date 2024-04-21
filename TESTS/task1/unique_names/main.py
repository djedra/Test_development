def unique_names(mentors: list) -> str:
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split(" ")[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'