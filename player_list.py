from bs4 import BeautifulSoup
import re
import requests
import random
import time

web_link = 'https://fbref.com/en/comps/9/Premier-League-Stats'
res = requests.get(web_link)
text = BeautifulSoup(res.content, 'html.parser')
find = text.find_all('a')
title = '<a href="\/en\/players\/[\d*\w*]+\/\w+[-]*\w+'
string_ver = str(text)
answer = re.findall(title, string_ver)
for i in answer:
    result = re.sub('<a href="/en/players/', '', i)
    result_new = re.sub('[\d*\w*]+/', '', result)
    print(result_new)



#href="en/players/(\d*\w*)+\w+\s\w+</a> &bull

#<a href="\/en\/players\/(\d*\w*)+\/Jarrod-Bowen">Jarrod Bowen<\/a>