from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#
s = Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")
url = "https://anandrathi.demo.riskcovry.com/partner/login"
driver = webdriver.Chrome(service=s,)
driver.get(url)
print(driver.title)

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [i for i in lst1 if i % 2 == 0]
print(lst2)

x = lambda a, b: a * b

dropdown = Select(driver.find_element(By.XPATH, "test"))
dropdown.select_by_value()
dropdown.se
