from bs4 import BeautifulSoup
import re
import requests
import random
import time
import pandas as pd

web_link = 'https://nba.hupu.com/stats/players'
res = requests.get(web_link)
text = BeautifulSoup(res.content, 'html.parser')
find = text.find_all('a')
player = '<a href="https://nba.hupu.com/players/\w*-\d*.html">(.*?)</a></td>'
points = '<td class="bg_b">\d*\.\d*</td>'
string_ver = str(text)
player_name = re.findall(player, string_ver)
player_points = re.findall(points, string_ver)
sequence = 0
while sequence < len(player_points):
    for i in player_name:
        #result = re.sub('<a href="/en/players/', '', i)
        #result_new = re.sub('[\d*\w*]+/', '', result)
        new_points = re.sub('<td class="bg_b">', ' ', player_points[sequence])
        end_points = re.sub('</td>', '', new_points)
        player_points[sequence] = end_points
        #print(i + end_points)
        sequence += 1
time.sleep(random.uniform(0, 20))

dataframe = pd.DataFrame({'Name': player_name, 'Points': player_points})
dataframe.to_csv('nba_scoring', sep=',')
print(dataframe)




#player_name_title : <a href="https://nba.hupu.com/players/\w*-\d*.html">(.*?)</a></td>

#<td class="bg_b">\d*.\d*</td>