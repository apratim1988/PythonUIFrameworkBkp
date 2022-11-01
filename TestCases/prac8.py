import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")
url = 'https://pos-diy.iiflinsurance.com/partner/login'
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(url)
time.sleep(5)
#page1
driver.find_element(By.XPATH, "//input[@formcontrolname='username']").send_keys("9011111100")
driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("pos@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
#page2
driver.find_element(By.XPATH, "//p[contains(text(),'Retail Health POS')]").click()
time.sleep(5)
#page3
button = driver.find_element(By.XPATH, "//p[contains(text(),'Rising Health Costs')]")
driver.execute_script("arguments[0].click();", button)
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(5)
#page4
driver.find_element(By.XPATH, "//span[contains(text(),'Self')]").click()
driver.find_element(By.XPATH, "//p[contains(text(),'Age')]").click()
driver.find_element(By.XPATH, "//p[contains(text(),'18')]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(5)
#page5
driver.find_element(By.XPATH, "//p[contains(text(),'Chennai')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[contains(text(),'NEXT')]").click()
time.sleep(5)
#page6
button = driver.find_element(By.XPATH, "//button[contains(text(),'No Health Concerns')]")
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
#page7
button = driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number']")
ActionChains(driver).move_to_element(button).click(button).perform()
driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number']").send_keys("9999999999")
time.sleep(1)
driver.find_element(By.XPATH, "//img[@data-toggle='modal']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[contains(text(),' NO I THINK I CAN DECIDE ON MY OWN ')]").click()
time.sleep(5)
#page8
button = driver.find_element(By.XPATH, "//button[contains(text(),'/ Year')][1]")
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
#page9
driver.find_element(By.XPATH, "//button[contains(text(),' PROCEED ')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='submitBtn btn-sub']").click()
time.sleep(5)
#page10
driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("Suriya Pranav")
time.sleep(5)
wait = WebDriverWait(driver, 30)
dob = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='date']")))
driver.execute_script("arguments[0].value = arguments[1]", dob, "2004-03-01")
# button = driver.find_element(By.XPATH, "//input[@formcontrolname='dob']")
# date = button.get_attribute("max")
# d = date.split('-')
# d[1]=str(int(d[1])-1)
# driver.execute_script("arguments[0].valueAsDate = new Date("+d[0]+","+d[1]+","+d[2]+");",button)
# driver.execute_script("arguments[0].setAttribute('class', 'ng-touched ng-dirty ng-valid')", button)