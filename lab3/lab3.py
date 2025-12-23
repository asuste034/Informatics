# Лабораторная работа 3 - Ветвящиеся Алгоритмы. Циклы.
# Вариант 2
import sys
import matplotlib.pyplot as plt
import math

def imba_input(msg: str, wanted_type: object = float) -> object:
    """Вспомогательная функция. Проверка на нужный формат"""
    while True:
        try:
            return wanted_type(input(msg))
        except ValueError:
            print('\033[31m'+f'ERROR: Ты ввел фигню :) Ожидается -> {str(wanted_type)}'+'\033[0m')
        except KeyboardInterrupt:
            print("\nУслышал тебя. Заканчиваю работу!")
            sys.exit(-1)

def integer_to_base(num: int, base) -> str|None:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # проверка
    if base > 35: raise Exception("Максимальная система счисления равна 35")
    if base > num: return str(num)
    itog = ""
    while num > 0:
        itog += digits[num%base]
        num //= base 
    return itog[::-1]

def fract_to_base(fract: int, base) -> str:
    # https://studfile.net/preview/8991849/page:4
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # проверка
    if base > 35: raise Exception("Максимальная система счисления равна 35")
    if base > fract: return str(fract)
    if fract == 0: return 0
    fract = float('0.'+str(fract))
    fract_ls = []
    for i in range(10):
        if fract>1: fract=fract-int(fract)
        fract*=base
        fract_ls.append(digits[int(fract)])
    fract = "".join(fract_ls)
    return fract

def task1():
    def check_even_last_symb(num) -> bool:
        return int(str(num)[-1])%2 == 0
    def positive_number(num) -> bool:
        return abs(num) == num
    while True:
        num = imba_input("Введите целое число - ", int)
        print( "Последняя цифра чётная" if check_even_last_symb(num) else "Последняя цифра нечётная")
        print("Число положительное" if positive_number(num) else "Число отрицательное")

def task2():
    def calculus_y(x):
        if x>=0:
            return 2*(x**3) - 2
        else: 
            return -math.sin(x)

    x_num = imba_input("x = ")
    print(f"f(x) = {calculus_y(x_num)}")
    print("Введите диапазон [a, b]")
    a = imba_input("a = ", int)
    b = imba_input("b = ", int)
    x_ls = [i for i in range(a, b, 1)]
    y_ls = [calculus_y(i) for i in x_ls]
    plt.plot(x_ls, y_ls)
    plt.grid(True)
    plt.show()

def task3():
    def decimal_in_binary_numeral_system(number: float):
        integer, fract = str(number).split('.')
        integer_num = integer_to_base(int(integer), 2)
        fract_num = fract_to_base(int(fract), 2)
        return '.'.join([integer_num, fract_num])
        
    def decimal_in_new_numeral_system(number: str, base=16):
        integer, fract = (str(number)).split('.')
        try:
            integer_num = integer_to_base(int(integer), base)
            fract_num = fract_to_base(int(fract), base)
            return '.'.join([integer_num, fract_num])
        except ValueError:
            print(f"Введённое вами число нельзя перевести в {base} систему счисления")
            sys.exit(-1)
    
    def decimal_in_new_numeral_system_any_input_base(number, base=2, input_base=10):
        if '.' not in number:
            number+=".0"
        integer, fract = (str(number)).split('.')
        try:
            integer_num = integer_to_base(int(integer, input_base), base)
            fract_num = fract_to_base(int(fract, input_base), base)
        except ValueError: 
            print(f"Введённое вами число нельзя перевести в {base} систему счисления")
            sys.exit(-1)
        return '.'.join([integer_num, fract_num])

    print("1) -> ПЕРЕВОД В ДВОИЧНУЮ СИСТЕМУ СЧИСЛЕНИЯ")
    print(f"Будет равно = {decimal_in_binary_numeral_system(imba_input('Число = '))}\n")

    print("2) -> ПЕРЕВОД В ДРУГУЮ СИСТЕМУ СЧИСЛЕНИЯ")
    any_base = imba_input("Система счисления, в которую вы хотите перевести = ", int)
    print(f"Будет равно = {decimal_in_new_numeral_system(imba_input('Число = '), any_base)}\n")

    print("3) -> ПЕРЕВОД В ДРУГУЮ СИСТЕМУ СЧИСЛЕНИЯ С ДРУГОЙ С.С")
    any_base = imba_input("Система счисления, в которую вы хотите перевести = ", int)
    input_base = imba_input("Система счисления вашего числа = ", int)
    print(f"Будет равно = {decimal_in_new_numeral_system_any_input_base(imba_input('Число = ', str), any_base, input_base)}\n")

def task5():
    print(f"Произведение чисел положительное? {"ДА!" if len([i for i in [int(imba_input(f"{i}) ")) for i in range(1, 5)] if i<0])%2==0 else "Ну конечно-же НЕТ!"}")

if __name__ == "__main__":
    task5()
