# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# chrome_options = Options()
# s = Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")
# url = "https://www.flipkart.com/"
# driver = webdriver.Chrome(service=s,options=chrome_options)
# driver.get(url)
# time.sleep(4)
# driver.find_element(By.XPATH, "//img[@alt='Mobiles']").click()
# time.sleep(2)
# elements = driver.find_elements(By.XPATH, "//p[@class='_1aqDWQ']")
# print(elements)
# for i in elements:
#     i.click()
#     time.sleep(2)
#     driver.back()
#     time.sleep(3)
#     continue


#lst1 = [1,2,3,4,5,6]
# print(lst1[:-4:-1])
# print(lst1[1:4])

# #1,2,3
# for i in lst1[1:4]:
#     print(i)

# a = range(1,10)
# print(type(a))
# flag = False
dict = {"name":"test1","age":30,("role","project"):"abcd"}
# for i,j in dict.items():
#     print(i,":",j)
dict.pop("abcd")
print(dict)



# if flag == True:
#     raise Exception




