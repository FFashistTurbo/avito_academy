import csv
from typing import Iterable

first_message = '''
Введите 1, если хотите показать иерархию
Введите 2, если хотите показать сводный отчёт
Введите 3, если хотите сохранить сводный отчёт
'''


def get_hierarchy(reader: Iterable) -> dict:
    """get hierarchy from file

    Args:
        reader (Iterable): file reader object

    Returns:
        dict: dictionary with hierarchy
    """
    hierarchy = {}
    for row in reader:
        dep, team = row['Департамент'], row['Отдел']
        if dep not in hierarchy:
            hierarchy[dep] = set()
        hierarchy[dep].add(team)
    return hierarchy


def print_hierarchy(hierarchy: dict):
    """output hierarchy info into console

    Args:
        hierarchy (dict): dictionary with hierarchy
    """
    print("*" * 40)
    for i, dep in enumerate(hierarchy.keys()):
        print(f'  {i}. {dep}')
        for j, team in enumerate(hierarchy[dep]):
            print(f'\t  {j}. {team}')
    print("*" * 40)


def get_deps_data(reader: Iterable) -> dict:
    """get information about departments

    Args:
        reader (Iterable): file reader object

    Returns:
        dict: dictionary with hierarchy
    """
    hierarchy = {}
    for row in reader:
        dep, salary = row['Департамент'], int(row['Оклад'])
        if dep not in hierarchy:
            hierarchy[dep] = {}
            hierarchy[dep]['max'] = salary
            hierarchy[dep]['min'] = salary
        hierarchy[dep]['max'] = max(salary, hierarchy[dep]['max'])
        hierarchy[dep]['min'] = min(salary, hierarchy[dep]['min'])
        hierarchy[dep]['number'] = hierarchy[dep].get('number', 0) + 1
        hierarchy[dep]['total'] = hierarchy[dep].get('total', 0) + salary
    # считаем среднюю зп по департаменту
    for dep in hierarchy.keys():
        hierarchy[dep]['avg_salary'] = \
                            hierarchy[dep]['total'] / hierarchy[dep]['number']
    return hierarchy


def print_deps_info(deps: dict):
    """output information about departments into console

    Args:
        deps (dict): dictionary with deparments info
    """
    print("*" * 40)
    print("Номер\t\tДепартамент\t Сотрудников\t\t\tВилка\t\tСредняя Зарплата")
    for i, dep in enumerate(deps.keys()):
        print(f'  {i:>3}. {dep:>20}\t\t {deps[dep]["number"]:>3} \
            {deps[dep]["min"]}-{deps[dep]["max"]}\t \
            {deps[dep]["avg_salary"]:.0f}')
    print("*" * 40)


def save_as_csv(data: dict):
    """save departments info into csv report

    Args:
        data (dict): data to save
    """
    with open('Dep_report.csv', 'w', newline='', encoding='utf-16') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Департамент', 'Численность',
                         'Вилка ЗП', 'Средняя Зарплата'])
        for dep in data:
            writer.writerow([
                dep,
                data[dep]['number'],
                f'{data[dep]["min"]}-{data[dep]["max"]}',
                data[dep]['avg_salary']])


def command_handler(reader: Iterable):
    """handler to user command

    Args:
        reader (Iterable): file reader object

    Raises:
        ValueError: on wrong input
    """
    print(first_message)
    command_num = int(input())
    if command_num == 1:
        h = get_hierarchy(reader)
        print_hierarchy(h)
        return
    if command_num == 2:
        dep_data = get_deps_data(reader)
        print_deps_info(dep_data)
        return
    if command_num == 3:
        dep_data = get_deps_data(reader)
        save_as_csv(dep_data)
        return
    else:
        raise ValueError('Некорректный ввод')


def parse_file():
    """init function
    """
    with open('Corp_Summary.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        command_handler(reader)


if __name__ == '__main__':
    parse_file()
