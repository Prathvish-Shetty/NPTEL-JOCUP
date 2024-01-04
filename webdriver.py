# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:06:39 2023

@author: Prathvish Shetty
"""

from selenium import webdriver
browser=webdriver.Chrome(r"C:\Users\Prathvish Shetty\Downloads\chromedriver-win64")
browser.get("https://www.seleniumhq.org")
elem=browser.find_element_by_link_text('Download')
elem.click()

search=browser.find_element_by_id('q')
search.send_keys('Download')