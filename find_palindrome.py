def input_number():
    """Ввод данных пользователем

    Пользователь вводить данные: палиндром и количество итераций,
    причем количество итераций можно не вводить,
    чтобы оно было равно стандартному значению

    :return: кортеж состоящий из числа, палиндром которого ищется,
    и количеством итераций, если оно указано.
    Если количество итераций не указано или указано не число,
    то возвращается кортеж только из числа
    Ложь, если пользователь ввел 'выход'
    Истина, если пользователь ввел строку не из чисел
    """
    palindrome = input(
        'Введите "выход", чтобы выйти или '
        'любое другое число, чтобы найти палиндром: '
    )

    if palindrome.lower() == "выход":
        return False
    if not check_int(palindrome):
        return True

    iteration_count = input(
        "Введите максимальное количество итераций \n"
        "оставьте поле пустым, чтобы итераций было не более 50: "
    )

    if not check_int(iteration_count) and iteration_count != "0":
        return palindrome,

    return palindrome, iteration_count


def check_int(checkable):
    """Проверка на то, состоит ли строка только из чисел

    Функция пробует преобразовать строку в число,
    чтобы проверить состоит ли строка только из чисел

    :param checkable: Строка, введенная пользователем
    :type checkable: str
    :return: Преобразует str в int, если это возможно. Иначе ложь
    """
    try:
        return int(checkable)
    except ValueError:
        return False


def find_palindrome(palindrome, iteration_count=50):
    """Функция ищет палиндром числа

    Число складывается с развернутой версией себя (например, 24 + 42),
    пока не найдется палиндром. Количество сложений ограничено пользователем
    :param palindrome: число строкой, которое складывается с самим собой,
                       пока не найдется палиндром
    :type palindrome: str, int
    :param iteration_count: количетсво итераций для поиска палиндрома
    :type iteration_count: int

    Raises:
        ValueError - если palindrome не является строкой, состоящей только из чисел
        (например, строка 'asd' вызовет исключение)

    :return: Истина, если палиндром найден, иначе ложь
             Ложь, если palindrome  - пустая строка
    Examples:
        >>> find_palindrome('2454543')
        Палиндром - 19899891. Число итераций: 3
        True
        >>> find_palindrome("")
        Вы ввели пустую строку
        False
        >>> find_palindrome("2")
        Палиндром - 2. Число итераций: 0
        True
        >>> find_palindrome("196")
        Палиндром не найден
        False
        >>> find_palindrome("22")
        Палиндром - 22. Число итераций: 0
        True
        >>> find_palindrome(123)
        Палиндром - 444. Число итераций: 1
        True

    """
    if palindrome == "":
        print("Вы ввели пустую строку")
        return False

    for n in range(iteration_count + 1):
        if str(palindrome) == str(palindrome)[::-1]:
            print(f"Палиндром - {palindrome}. Число итераций: {n}")
            return True
        palindrome = str(int(palindrome) + int(str(palindrome)[::-1]))
    else:
        print("Палиндром не найден")
        return False


def main():
    """Основная функция, связывающая все функции программы

    Зацикливает ввод чисел для нахождения палиндромов,
    вызывает по очереди функции ввода и поиска палиндрома,
    если функция ввода истинна
    """
    while True:
        option = input_number()

        if option is False:
            break
        elif option is True:
            print("Ошибка!")
            continue
        else:
            find_palindrome(*option)


if __name__ == "__main__":
    main()
