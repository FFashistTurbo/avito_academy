def step2_umbrella():
    """печает ответ с зонтом
    """
    print('Утку унесло на зонте ураганом')


def step2_no_umbrella():
    """печатает ответ без зонта
    """
    print('Утку смыло дождём')


def step1():
    """
    Returns:
    функция, в зависимости от ввода пользователя
    """
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
