# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddingGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_adding_group(self):
        driver = self.wd
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_id("loginform").submit()
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("newgroup")
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("header")
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("footer")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except nosuchelementexception as e: return false
        return true

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except noalertpresentexception as e: return false
        return true

    def teardown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
