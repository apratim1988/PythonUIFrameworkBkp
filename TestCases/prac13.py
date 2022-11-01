import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
###WebTable Automation
chrome_options = Options()
# chrome_options.add_argument("--headless")
s = Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")
url = "https://www.techlistic.com/p/demo-selenium-practice.html"
driver = webdriver.Chrome(service=s,options=chrome_options)
driver.maximize_window()
driver.get(url)
time.sleep(2)
print(url.title())
table = driver.find_element(By.ID, "customers")
headers = table.find_elements(By.XPATH,"//tr[@style='box-sizing: inherit;']/th")
rows = table.find_elements(By.TAG_NAME,"tr")
rowsno = len(rows)
for i in range(rowsno):
    columns = rows[i].find_elements(By.TAG_NAME, "td")
    for j in columns:
        print(j.text)
###broken links
links = driver.find_elements(By.TAG_NAME,"a")
for i in links:
    r = requests.head(i.get_attribute('href'))
    print(r.status_code)
    if r != 200:
        print("broken")
