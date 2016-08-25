"""
На вход подаются две строки, содержащие url двух документов A и B.
Выводится Yes, если из A в B можно перейти за два перехода, иначе выводится No.
"""

import requests
import re

A = input().strip()
B = input().strip()

res1 = requests.get(A) # получим по ссылке А ресурс
matchs = re.findall("https://.+?\.html", res1.text) # находим все ссылки в ресурсе

metka = False

for match in matchs: # для каждой ссылки
    res = requests.get(match) # получим по ссылке ресурс
    if res.status_code == 200: # если ресурс доступен
        if re.search(B, res.text) != None: # если найдем строку B в ресурсе
            metka = True

if metka == True:
    print('Yes')
else:
    print('No')