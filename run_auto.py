#coding:utf-8
from config import *
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from base import *

for code in area:
    body['ProvinceCode'] = code
    for i in (1, 2):
        body['WenLi'] = i
        requests.post(url=url, data=body, headers=header)

        browser = webdriver.Chrome()
        Page(browser).login("http://www.ewt360.com/Innovate")

        try:
            browser.find_element_by_xpath("//div[@class='nav clear']/ul/li[2]/span").click()
        except NoSuchElementException:
            time.sleep(1)
        print body['ProvinceCode'], body['WenLi'], area[code]
        time.sleep(1)
        screen_dir = "f:/screen062901"
        if not os.path.exists(screen_dir):
            os.mkdir(screen_dir)
        if i == 1:
            browser.save_screenshot((screen_dir + "/" + area[code] + '_文科' + '.png').decode('utf-8'))
        if i == 2:
            browser.save_screenshot((screen_dir + "/" + area[code] + '_理科' + '.png').decode('utf-8'))
        browser.close()
        browser.quit()

