"""
Простой калькулятор, который считывает с пользовательского ввода три строки: 
первое число, второе число и операцию, после чего применяет операцию к введённым числам 
("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где 
mod — это взятие остатка от деления, 
pow — возведение в степень, 
div — целочисленное деление.

Если выполняется деление и второе число равно 0, выводится строка "Деление на 0!".
"""

a = float(input())
b = float(input())
operation = input()
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif operation == '*':
    print(a * b)
elif operation == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif operation == 'pow':
    print(a ** b)
elif operation == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)