"""
На вход подается ссылка на HTML файл.
Необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > 
и вывести список сайтов, на которые есть ссылка.
"""

import re
import requests

link = input().strip()

resurs = requests.get(link)
matchs = re.findall(r"(<a.*?)(href *?= *?[\"|\'])([\w:/]*[/|])?(\w[\w.-]*)", resurs.text)

list = []

for match in matchs:
    if match != None:
        if match[3] not in list:
            list.append(match[3])

list.sort()
for l in list:
    print(l)