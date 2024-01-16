from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



path = '/Users/tonyqin/Downloads/chromedriver_mac64\ \(5\)/chromedriver'
browser = webdriver.Chrome(executable_path=path)
link = 'https://twitter.com'
browser.get(link)
actions = ActionChains(browser)
list_of_trends = []
n = 1


def move_along():
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)


def log_in(username, password):
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "登录"))
    )
    button.click()
    enter_username = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "text")
    ))
    enter_username.send_keys(username)
    enter_username.send_keys(Keys.RETURN)
    enter_password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "password")
                                       ))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)


def explore():
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "探索"))
    )
    button.click()
    result = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "趋势"))
    )
    result.click()


def get_result(start):
    # main = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]")
    # james = main.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]')
    # anfield = james.find_elements_by_class_name('css-1dbjc4n')
    # print(anfield)
    start = len(list_of_trends) + 1
    main = browser.find_elements_by_css_selector('div.css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-b88u0q.r-rjixqe.r-1bymd8e.r-bcqeeo.r-qvutc0')
    for i in main:
        if i.text not in list_of_trends:
            print(str(start) + ' ' + i.text)
            start += 1
            list_of_trends.append(i.text)


def create_csv():
    numbers = [x for x in range(1, 31)]
    dataframe = pd.DataFrame({'Rank': numbers, 'Trends': list_of_trends})
    dataframe.to_csv('result_twitter', sep=',')


def send_email(sender_address, sender_pass, receiver):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver
    message['Subject'] = 'hehe'
    mail_content = 'hehehe。'
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'result_twitter'
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver, text)
    session.quit()


log_in('9259158532', 'Luffyhaha')
browser.maximize_window()
explore()
time.sleep(10)
get_result(n)
browser.execute_script('window.scrollTo(0, 4000)')
time.sleep(10)
get_result(n)
create_csv()
send_email('luffyhappy123@gmail.com', 'Tonyqin2003', 'chelseastab23@gmail.com')

