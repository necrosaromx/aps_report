#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Saul Vargas Leon

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(driver, user, password):
    
    driver.find_element_by_name("username").send_keys(user)
    driver.find_element_by_name("password").send_keys(password)
    submit = driver.find_element_by_id("login_button").click()
