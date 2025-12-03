import math
import sys
from utils_func import imba_input, rub_usd

def task1():
    """# Вычисление _a_ и _b_ значения через аргументы x y z"""
    x = imba_input("Введите значение x: ")
    y = imba_input("Введите значение y: ")
    z = imba_input("Введите значение z: ")
    try:
        a = (3+math.exp(2))/(1+(x**2)*abs(y-math.tan(z)))
        b = 1 + abs(y-x)+((y-x)**2/2)+((x-y)**2/3)
    except ArithmeticError:
        print("ERROR: Арифметическая ошибка")
    except ZeroDivisionError:
        print("ERROR: В процессе решения вышло деление на нуль! ОДЗ")
    except Exception as e:
        print(f"ERROR: Неизвестная ошибка! exception: {e}")
    print(f"-> Значение a\t{a:.4f}\n-> Значение b\t{b:.4f}")

def task2():
    """"""
    x = imba_input("Введите значение x: ")
    a = -2
    b = 5
    c = 3
    if c+x**3 == 0:
        print("ОДЗ! в знаменателе c+x**3 вышло 0")
        return
    y = ((b*x+a)**2/(c+x**3))+x**4
    print(f"f(x) = {y:.4f}")

def task3():
    """"""
    x = imba_input("Введите значение x: ")
    try:
        y = abs(math.log(math.cos(x**2)))/(math.sin(x**2+(x**0.5)))
        print(f"f(x) = {y:.4f}")
    except ZeroDivisionError:
        print("ОДЗ! в знаменателе math.sin(x**2+(x**0.5)) вышло 0")
    except ValueError:
        print("Неопределёность...")

def task4():
    """"""
    a = imba_input("Введите сторону a: ")
    b = imba_input("Введите сторону b: ")
    if (a**2+b**2)**0.5 == 0:
        print("ОДЗ! Деление на нуль")
        return
    h = (a*b)/(a**2+b**2)**0.5
    print(f"Длина высоты h = {h:.4f}")

def task5():
    """"""
    a = imba_input("Введите сторону a:\t", int)
    r = imba_input("Введите радиус r:\t", int)
    n = 1+(a/2*r)-(2/3**0.5)
    nums_balls = n*(n+1)//2

    if 2*r+(n-1)*r*(3**0.5) <= a*(3**0.5)/2:
        print(f"В р/с треугольник с сторонами {a} поместиться шаров с радиусом {r} всего {nums_balls}")
    else:
        print("Такого не бывает, как ты поместишь такой большой шар в мелкий треугольник?)")

def task7():
    """Решить систему уравнений
        | A1  B1 | C1
        | A2  B2 | C2
    """
    print("Напишите коэф. для данной системы\n| A1  B1 | C1\n| A2  B2 | C2\n ")
    while True:
        A1 = imba_input("A1 [-10;+∞) = ")
        if -10 <= A1:
            break
    B1 = imba_input("B1 = ")
    C1 = imba_input("C1 = ")
    A2 = imba_input("A2 = ")
    B2 = imba_input("B2 = ")
    while True:
        C2 = imba_input("C2 (-∞;10] = ")
        if C2 <= 10:
            break
    D=A1*B2-A2*B1
    try:
        x=(C1*B2-C2*B1)/D
        y=(A1*C2-A2*C1)/D
        print(f"x = {x}")
        print(f"y = {y:.4f}")
    except ZeroDivisionError:
        print("Деление на ноль!")

def task8():
    """Перевод темпеартуры с цельсий в фаренгеЙты"""
    while True:
        Tc = imba_input("Введите темпатуру в Цельсиях [0;100]: ")
        if 0<=Tc<=100:
            break
    Tf = Tc*(9/5)+32
    print(f"Температура в Фаренгейтах будет = {Tf:.4f}")

def task9():
    """"""
    while True:
        commission_percent = imba_input("Процент комиссии: ")
        if 0<=commission_percent<=100:
            break
    exchange_money = rub_usd()
    ruble = imba_input("Сумма в рублях: ")

    usd_money = ruble/exchange_money
    commission = usd_money*(commission_percent/100)
    usd_money = usd_money-commission
    print(f"RUB {ruble} <-- Курс {exchange_money:.4f}--> USD {usd_money:.4f}")

if __name__ == "__main__":
    task1()
