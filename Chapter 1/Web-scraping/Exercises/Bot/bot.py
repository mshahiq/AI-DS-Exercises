import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import numpy as np

url = 'https://www.youtube.com/watch?v=HUgMWJKn2YY'

pth = 'chromedriver.exe'

driver = webdriver.Chrome(pth)

driver.get(url)

sleep(7)

driver.find_element_by_css_selector('#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.footer.style-scope.ytd-consent-bump-v2-lightbox > div.buttons.style-scope.ytd-consent-bump-v2-lightbox > ytd-button-renderer:nth-child(2) > a').click()

i = 1
while i < 100:

    command = input("Enter the command:")

    if command == 'pause':
        driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
    elif command == 'play':
        driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()