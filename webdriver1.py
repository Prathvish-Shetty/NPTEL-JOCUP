# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:31:38 2023

@author: Prathvish Shetty
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("C:\Users\Prathvish Shetty\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver, 600)
target='"Ravikiran"'#friend's name
string="Message sent using python!!"#message to be sent
x_arg='//span[contains(@title, '+ target +')]'
target=wait.untill(EC.presence_of_all_elements_located((By.XPATH,x_arg)))
target.click()
input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(50):
    input_box.send_keys(string+Keys.ENTER)