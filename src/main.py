import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login import login
from learn_test import learn_test
from do_test import do_test

options: Options = Options()
options.add_argument('--no-sandbox')  # Bypass OS security model
browser: webdriver.Chrome = webdriver.Chrome(options=options,
                           executable_path=f'{os.getcwd()}\\chromedriver_win32\\chromedriver.exe')  # Gets the web driver
browser.get('https://www.educake.co.uk/')  # Goes to the educake website
browser.maximize_window()

username: str = 'enog0001'
password: str = 'Azemine1'

login(browser=browser, username=username, password=password)
learn_test(browser=browser)
while True:
    do_test(browser=browser)