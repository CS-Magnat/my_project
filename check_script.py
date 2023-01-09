import time
import re
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path="C:\\Users\\qwerty\\PycharmProjects\\resource\\chromedriver.exe")
driver.get("https://catalog.onliner.by/notebook?common_date%5Bfrom%5D=2022&common_date%5Bto%5D=2022&cpunb%5B0%5D=corei9&cpunb%5Boperation%5D=union&nbusage%5B0%5D=gamer&nbusage%5Boperation%5D=union")
driver.maximize_window()

naselennyy_punkt = "//*[@id='schema-filter']/div[6]/div[1]/a"
# driver.execute_script("window.scrollTo(0,1000)")
get_naselennyy_punkt = WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, naselennyy_punkt)))
action = ActionChains(driver)
action.move_to_element(get_naselennyy_punkt).perform()
# text = get_naselennyy_punkt.text
# print(text)
time.sleep(10)

# q  = "от 11 350,00 р."
# # number = re.findall(r'\d+', q)
# w = q.replace(" ", "")
# # e = w.replace(",", ".")
# r = re.findall("([0-9]+[ ,]+[0-9]+)", w)
# t = "".join(r)
# # listToStr = ''.join(map(str, r))
#
# # print(w)
# # print(e)
# # # print(re.findall("([0-9]+[,.]+[0-9]+)", e ))
# print(w)
# print(r)
# print(t)
# # print(type(t))
# # print(listToStr)

