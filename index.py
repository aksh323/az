import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

name = random.choice(['mehak','salman','rishi','manhan','vishal','shubham','shivam','komal','sunny','mohit','mahender'])
domain = random.choice(["@2go-mail.com","@emailhost99.com","@govdep5012.com","@homedepinst.com","@hubopss.com","@johnderasia.com","@lagsixtome.com","@officemalaga.com"])
digit = random.randint(100, 9999)

def create_email(name,digit):
    email = name+str(digit)+domain
    return email

def create_acc(self):
        driver = webdriver.Firefox()
        driver.get(
            "https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&prevRID=5CJTZB6DDEVZTWX6ZQ92&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        driver.find_element_by_id("ap_customer_name").clear()
        driver.find_element_by_id("ap_customer_name").send_keys(name)
        driver.find_element_by_id("ap_email").clear()
        driver.find_element_by_id("ap_email").send_keys(create_email(name,digit))
        driver.find_element_by_id("ap_password").clear()
        driver.find_element_by_id("ap_password").send_keys("Passon!23")
        driver.find_element_by_id("ap_password_check").clear()
        driver.find_element_by_id("ap_password_check").send_keys("Passon!23")
        driver.find_element_by_id("continue").click()

create_acc(name)