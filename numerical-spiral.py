"""
Выводит таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, 
выходящей из левого верхнего угла и закрученной по часовой стрелке.
"""

n = int(input())
a = [[0 for i in range(n)] for i in range(n)]
i = 0
j = 0
k = 0
a[i][j] = k + 1
k = k + 1
while k < (n * n):
    while  0 <= j + 1 < n and a[i][j+1] == 0:
        j = j + 1
        a[i][j] = k + 1
        k = k + 1
    while 0 <= i + 1 < n and a[i+1][j] == 0:
        i = i + 1
        a[i][j] = k + 1
        k = k + 1
    while 0 <= j - 1 < n and a[i][j-1] == 0:
        j = j - 1
        a[i][j] = k + 1
        k = k + 1
    while 0 <= i - 1 < n and a[i-1][j] == 0:
        i = i - 1
        a[i][j] = k + 1
        k = k + 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()