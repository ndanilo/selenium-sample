from selenium import webdriver
from io import BytesIO
from PIL import Image
import os

url=os.environ["SITE_URL"]
url="https://www.mtgowikiprice.com/card/thb/229/Uro_Titan_of_Natures_Wrath"
chrome=webdriver.Chrome('C:\\Utils\\Selenium\\Chrome\\79\\chromedriver.exe')
chrome.get(url)

element=chrome.find_element_by_id('highcharts-0')

location=element.location
size=element.size

left=location['x']
top=location['y']
right=left+size['width']
bottom=top+size['height']

png=chrome.get_screenshot_as_png()

im = Image.open(BytesIO(png))
graph=im.crop((left,top,right,bottom))

graph.show()
chrome.quit()

"""
standard_editions=chrome.find_elements_by_css_selector('#standard ul li')

del standard_editions[0]
standard_editions.reverse()

standard_editions[0].click()
"""
"""
for e in standard_editions:
    print(e.text)
"""


