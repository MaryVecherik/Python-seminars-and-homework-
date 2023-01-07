# Модуль для ввода/вывода информации


def choose() -> str:
    """"Выбор режима работы приложения"""
    return (input('Введите режим программы(1-пример, 2-уравнение, 3-многочлен, 4-история): '))


def get_expr() -> str:
    """"Запрашивает у пользователя задачу"""
    expr = input('Введите Задачу: ')
    try:
        return (f'{expr}')
    except ValueError:
        print('Incorrect input')


def show_res(res: str):
    """Выводит результат"""
    print(f'Результат: {res}')


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    return print('Вы ввели неверный режим прграммы!')


def show_history(history: str):
    """Выводит истроию оперций"""
    print(f'История: \n{history}')