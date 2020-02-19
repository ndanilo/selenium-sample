from selenium import webdriver
from io import BytesIO
import os

url=os.environ["SITE_URL"]
chrome=webdriver.Chrome('C:\\Utils\\Selenium\\Chrome\\79\\chromedriver.exe')
chrome.get(url)

standard_editions=chrome.find_elements_by_css_selector('#standard ul li')

del standard_editions[0]
standard_editions.reverse()

standard_editions[0].click()
"""
for e in standard_editions:
    print(e.text)
"""

#chrome.quit()