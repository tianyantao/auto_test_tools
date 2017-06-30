from selenium.webdriver.common.keys import Keys
import time
import re
import requests


def get_cookie():
    t = re.findall("user=tk=.*?(?=;)", str(requests.get(
        'http://my.ewt360.com/login/prelogin?sid=2&username=18516212224&password=123456').headers))[
        0]
    return t


def get_province():
    res = requests.get("http://passport.ewt360.com/Ajax/GetUser?type=1",
                       headers={'Content-Type':'application/x-www-form-urlencoded','cookie':get_cookie()}).content
    return re.findall("(?<=Province:').*?(?=')", res)[0]


def get_expireyear():
    res = requests.get("http://passport.ewt360.com/Ajax/GetUser?type=1",
                       headers={'Content-Type': 'application/x-www-form-urlencoded', 'cookie': get_cookie()}).content
    ex_year = re.findall("(?<=ExpireYear:').*?(?=')", res)[0]
    return ex_year


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, n):
        for i in range(n):
            self.driver.execute_script("document.body.scrollTop+=10")
            time.sleep(0.05)

    def login(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys('18516212224')
        self.driver.find_element_by_name('username').send_keys(Keys.TAB)
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_name('submit').click()
        time.sleep(2)
