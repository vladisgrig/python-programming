"""
Программа эмулирует работу с пространствами имен.
У каждого пространства имен есть уникальный текстовый идентификатор – его имя.

На вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе 
из пространства <namespace>, или None, если такого пространства не существует

Для каждого запроса get выводится в отдельной строке его результат.
"""

# создание пространств имен
# имя пространства уникально

def create_namespace(a, b):
    global namespace_dict
    namespace_dict[a] = b

# добавление имени в пространство

def add_var(a, b):
    global var_dict
    if a in var_dict.keys():
        var_dict[a].append(b)
    else:
        var_dict[a] = [b]

# получить имя пространства
def get_namespace(a, b):
    global var_dict
    global namespace_dict
    if a in var_dict.keys():
        if b in var_dict[a]:
            return print(a)
        else:
            if a in namespace_dict.keys():
                get_namespace(namespace_dict[a], b)
            else:
                return print('None')
    else:
        if a in namespace_dict.keys():
            get_namespace(namespace_dict[a], b)
        else:
            return print('None')

var_dict = {}
namespace_dict = {}
i = 0
n = int(input())
while i < n:
    a, b, c = input().split()
    if a == 'create':
        create_namespace(b, c)
    elif a == 'add':
        add_var(b, c)
    else:
        get_namespace(b, c)
    i += 1