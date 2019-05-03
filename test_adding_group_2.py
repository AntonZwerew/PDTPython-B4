# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class TestAddingGroup2(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def login(self, wd, username, password):
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def submit_group(self, wd, group):
        wd.find_element_by_name("new").click()
        # Заполняем форму новой группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Отправляем форму группы
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        self.submit_group(wd,group)
        self.return_to_group_page(wd)

    def test_adding_group(self):
        wd = self.wd
        group = Group("Name1", "Header1", "Footer1")
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, group)
        self.logout(wd)

    def test_adding_empty_group(self):
        wd = self.wd
        emtpy_group = Group("", "", "")
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, emtpy_group)
        self.logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
