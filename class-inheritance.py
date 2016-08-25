"""
Дано описание наследования классов исключений в следующем формате. 
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений.
Гарантируется, что никакое исключение не обрабатывается дважды.

В отдельной строке выводится имя каждого исключения, обработку которого можно удалить из кода, 
не изменив при этом поведение программы.

"""

n = int(input())
i = 1
class_dict = {}
while i <= n:
    i += 1
    string = input()

    if ':' in string:
        son, parents = string.split(' : ')
        parents_list = parents.split()
        if son not in class_dict.keys():
            class_dict[son] = []
        for j in parents_list:
            if j not in class_dict.keys():
                class_dict[j] = []
            class_dict[j].append(son)
            for key in class_dict.keys():
                if (j in class_dict[key]) and (son not in class_dict[key]):
                    class_dict[key].append(son)


    else:
        if string not in class_dict.keys():
            class_dict[string] = []

for key in class_dict.keys():
    for value in class_dict[key]:
        for v in class_dict[value]:
            if v not in class_dict[key]:
                class_dict[key].append(v)

m = int(input())
l = 1
current_parent = []
used_classes = []
while l <= m:
    metka = False
    l += 1
    class_name = input()
    if class_name not in used_classes:
        used_classes.append(class_name)
    for key in class_dict.keys():
        if class_name in class_dict[key]:
            current_parent.append(key)
    for i in current_parent:
        if i in used_classes:
            metka = True
    if metka == True:
        print(class_name)
    current_parent = []