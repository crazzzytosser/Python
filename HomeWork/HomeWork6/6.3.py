# 3. Написать функцию, аргументы - имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.


def function(*names):
    new_name = {name.title() for name in names}
    first_letter = [name[0].upper() for name in names]
    result_dict = {j: list() for j in first_letter}
    for name in names:
        result_dict[name[0]].append(name)
    return result_dict


print(function("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))