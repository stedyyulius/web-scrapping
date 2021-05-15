from selenium import webdriver
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://tiktok.com')

content = BeautifulSoup(driver.page_source)

hashtags = []

for tag in content:
    hashtags.extend(re.findall(r"#(\w+)", tag.text))

print(hashtags)
