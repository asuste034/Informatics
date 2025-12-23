import sys
import re
import random
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def imba_input(msg: str, wanted_type: object = int) -> object:
    """Вспомогательная функция. Проверка на нужный формат"""
    while True:
        try:
            return wanted_type(input(msg))
        except ValueError:
            print(
                "\033[31m"
                + f"ERROR: Ты ввел фигню :) Ожидается -> {str(wanted_type)}"
                + "\033[0m"
            )
        except KeyboardInterrupt:
            print("\nУслышал тебя. Заканчиваю работу!")
            sys.exit(-1)


def task1():
    def print_char_list(array: list) -> None:
        print(f"Массив: {' '.join(array)}")

    n = imba_input("n = ")

    array = [hex(random.randint(2048, 2048 * 12))[2:] for i in range(n)]
    print_char_list(array)
    print_char_list([re.sub(r"\d", "*", i) for i in array])


def task3():
    text = imba_input("Введите текст: ", str)
    with open("task3.txt", "w") as f:
        f.write(text)


def task5():
    def detector(stroka: str):
        s = ord(stroka[0])
        # числа
        if 48 <= s <= 57:
            return True
        # english
        if 65 <= s <= 90:
            return True
        # Русский
        if 1040 <= s <= 1071 or s == 1025:
            return True
        return False

    print("Введите :q для выхода")
    while True:
        txt = imba_input("Введите текст: ", str)
        if txt == ":q":
            print("- Bye bye ;(\n\tДо скорой встречи :)")
            break
        if detector(txt):
            with open("task5_upper.txt", "w", encoding="utf-8") as f:
                f.write(txt)
        else:
            with open("task5_regular.txt", "w", encoding="utf-8") as f:
                f.write(txt)


def task6():
    # Константы
    START_TABLE_LINE = 10  # Номер линии начала таблицы
    NODEID_SIZE = 5  # Длина символов под NODE
    DATA_SIZE = 13  # Длина символов под значения S1,S2...
    # -----------------------------
    lines = []
    dic = {}
    with open("variant2.txt") as f:
        lines = [i.strip() for i in f][START_TABLE_LINE:]
    length = len(lines) - 1
    axis_x = [i for i in range(length)]
    for i, line in enumerate(lines[0].split()):
        if i == 0:
            dic[line] = [a[:NODEID_SIZE].strip() for a in lines[1:]]
        else:
            # для наглядности, как хранит питон строку
            # 6211  0.18801E+008 0.11002E+008-0.18891E+006 0.18990E+008 0.16533E+008
            step = DATA_SIZE * (i - 1)  # Шаг одного значения
            dic[line] = [
                "%.3E"
                % float(a[NODEID_SIZE + step : NODEID_SIZE + DATA_SIZE + step].strip())
                for a in lines[1:]
            ]
    for name in dic.keys():
        if name != "NODE":
            with open(f"task6_{name}.dat", "w") as f:
                f.write("\n".join(dic[name]))
            plt.plot(axis_x, dic[name], label=name)
        else:
            axis_x = dic[name]
    # plt.grid(True)
    plt.legend(loc="lower right")
    plt.show()


def task7():
    run_dir = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(run_dir):
        for name in files:
            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, run_dir)
            print(rel_path)


if __name__ == "__main__":
    task6()
