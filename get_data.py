from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

path = '/Users/tonyqin/Downloads/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-site-isolation-trials")
browser = webdriver.Chrome(chrome_options=options, executable_path=path)
browser.maximize_window()
link = 'https://www.whoscored.com/'
browser.get(link)
# player_list = []
player_list = {'Son Heung-Min': [2022, 2021], 'Mohamed Salah': [2022, 2021, 2020, 2019, 2018], 'Cristiano Ronaldo': [2022], 'Harry Kane': [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015], 'Sadio Mané': [2022, 2020, 2019], 'Diogo Jota': [2022], 'Jamie Vardy': [2022, 2021, 2020, 2019, 2018, 2016], 'Kevin De Bruyne': [2022], 'Bruno Fernandes': [2021], 'Patrick Bamford': [2021], 'Dominic Calvert-Lewin': [2021], 'Danny Ings': [2020], 'Pierre-Emerick Aubameyang': [2020, 2019], 'Raheem Sterling': [2020, 2019, 2018], 'Anthony Martial': [2020], 'Marcus Rashford': [2020], 'Raúl Jiménez': [2020], 'Sergio Agüero': [2020, 2019, 2018, 2017, 2016, 2015, 2014], 'Tammy Abraham': [2020], 'Eden Hazard': [2019, 2017], 'Romelu Lukaku': [2018, 2017, 2016, 2014, 2013], 'Roberto Firmino': [2018], 'Alexis Sánchez': [2017, 2015], 'Diego Costa': [2017, 2015], 'Dele Alli': [2017], 'Zlatan Ibrahimovic': [2017], 'Joshua King': [2017], 'Christian Benteke': [2017, 2013], 'Fernando Llorente': [2017], 'Jermain Defoe': [2017, 2016], 'Riyad Mahrez': [2016], 'Olivier Giroud': [2016, 2014], 'Odion Ighalo': [2016], 'Charlie Austin': [2015], 'Luis Suárez': [2014, 2013], 'Daniel Sturridge': [2014], 'Yaya Touré': [2014], 'Wayne Rooney': [2014], 'Edin Dzeko': [2014], 'Wilfried Bony': [2014], 'Jay Rodriguez': [2014], 'Robin van Persie': [2013], 'Gareth Bale': [2013], 'Michu': [2013], 'Dimitar Berbatov': [2013], 'Frank Lampard': [2013], 'Rickie Lambert': [2013]}
player_goals = {}
player_shots = {}


def search(number):
    search_button = browser.find_element_by_id('search-box')
    player = list(player_list.keys())[number]
    search_button.send_keys(player)
    search_button.send_keys(Keys.RETURN)
    lynk = browser.find_element_by_link_text(player)
    lynk.click()


def get_data(player, player_year):
    item = 1
    search_result = []
    prem_league = []
    years_i_want = []
    history = browser.find_element_by_link_text('History')
    history.click()
    time.sleep(5)
    main = browser.find_element_by_id('player-table-statistics-body')
    while item < 40:
        try:
            data = main.find_element_by_css_selector('#player-table-statistics-body > tr:nth-child(' + str(item) + ')')
            search_result.append(data)
            item += 1
        except Exception:
            print('hello')
            break
    for i in search_result:
        try:
            print(i.text)
            tournament = i.find_element_by_class_name('tournament-link')
            print(tournament.text)
            if tournament.text == 'EPL':
                prem_league.append(i)
        except Exception:
            break
    # for year in player_year:
    #     print(str(year - 1) + '/' + str(year))
    for j in prem_league:
        for year in player_year:
            year_text = j.find_element_by_class_name('col12-lg-1')
            if year_text.text == str(year - 1) + '/' + str(year):
                # print(str(year - 1) + '/' + str(year))
                years_i_want.append(j)
    for z in years_i_want:
        goal = z.find_element_by_class_name('goal   ')
        if player not in player_goals.keys():
            player_shots[player] = [goal.text]
        else:
            player_goals[player].append(goal.text)


def get_shots(player, player_year):
    item = 1
    history = browser.find_element_by_link_text('History')
    history.click()
    time.sleep(5)
    detailed = browser.find_element_by_link_text('Detailed')
    detailed.click()
    total_change = browser.find_element_by_id('statsAccumulationType')
    change = total_change.find_element_by_css_selector('#statsAccumulationType > option:nth-child(4)')
    change.click()
    time.sleep(3)
    search_button = browser.find_element_by_class_name('search-button')
    search_button.click()
    browser.execute_script('window.scrollTo(0, 1600)')
    time.sleep(5)
    main = browser.find_element_by_id('player-tournament-stats')
    search_result = []
    prem_league = []
    years_i_want = []
    a = main.find_element_by_id('player-tournament-stats-detailed')
    b = a.find_element_by_id('statistics-table-detailed')
    dude = b.find_element_by_id('player-table-statistics-body')
    while item < 40:
        try:
            c = dude.find_element_by_css_selector('#player-table-statistics-body > tr:nth-child(' + str(item) + ')')
            search_result.append(c)
            item += 1
        except Exception:
            break
    for i in search_result:
        try:
            tournament = i.find_element_by_class_name('tournament-link')
            if tournament.text == 'EPL':
                prem_league.append(i)
        except Exception:
            break
    for j in prem_league:
        for year in player_year:
            year_text = j.find_element_by_class_name('col12-lg-1')
            if year_text.text == str(year - 1) + '/' + str(year):
                # print(str(year - 1) + '/' + str(year))
                years_i_want.append(j)
    for z in years_i_want:
        shots = z.find_element_by_class_name('shotsTotal   ')
        if player not in player_shots.keys():
            player_shots[player] = [shots.text]
        else:
            player_shots[player].append(shots.text)



def mainshit():
    for i in range(len(player_list.keys())):
        player = list(player_list.keys())[i]
        player_year = list(player_list.values())[i]
        search(i)
        time.sleep(5)
        # try:
        #     close = browser.find_element_by_class_name('webpush-swal2-close')
        #     print('close found')
        #     close.click()
        # except Exception:
        #     print('close not found')
        #     time.sleep(3)
        get_data(player, player_year)
        print(player_goals)


def main_dude():
    for i in range(len(player_list.keys())):
        player = list(player_list.keys())[i]
        player_year = list(player_list.values())[i]
        search(i)
        # time.sleep(5)
        get_shots(player, player_year)
        print(player_shots)


main_dude()
# player = list(player_list.keys())[3]
# player_year = list(player_list.values())[3]
# search(3)
# time.sleep(5)
# try:
#     close = browser.find_element_by_class_name('webpush-swal2-close')
#     print('close found')
#     close.click()
# except Exception:
#     print('close not found')
#     time.sleep(3)
# get_data(player, player_year)
# print(player_goals)
# player = list(player_list.keys())[3]
# player_year = list(player_list.values())[3]
# search(3)
# get_shots(player, player_year)
# print(player_shots)



