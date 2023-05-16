from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

print("Tüm bilgileri büyük harfler")
il = input("İl giriniz:")
ilce = input("İlçe giriniz:")
ilce = ilce.upper()
sandikno = input("Sandık no giriniz:")

driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
driver.get("https://sts.chp.org.tr/")
wait = WebDriverWait(driver, 30)
button = wait.until(EC.visibility_of_element_located((By.ID, "rdveriKaynagi_1")))

button = driver.find_element_by_id("rdveriKaynagi_1")
button.click()

select = driver.find_element_by_id("ddlIller")
select.click()
option = driver.find_element_by_xpath("//option[contains(text(), '"f"{il}')]")
option.click()

select = wait.until(EC.visibility_of_element_located((By.ID, "ddlIlceler")))
select = driver.find_element_by_id("ddlIlceler")
select.click()
option = driver.find_element_by_xpath("//option[contains(text(), '"f"{ilce}')]")
option.click()

select = wait.until(EC.visibility_of_element_located((By.ID, "ddlSandiklar")))
select = driver.find_element_by_id("ddlSandiklar")
select.click()
option = driver.find_element_by_xpath("//option[contains(text(), '"f"{sandikno}')]")
option.click()

button = driver.find_element_by_id("btnSorgula")
button.click()

elements = driver.find_elements_by_xpath("//input[starts-with(@id, 'txt')]")
for element in elements:
    id = element.get_attribute("id")
    value = element.get_attribute("value")
    print(id, value)
