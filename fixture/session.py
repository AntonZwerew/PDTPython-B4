# -*- coding: utf-8 -*-
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def login(self, username, password):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_name("user")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        # ожидание логаута
        wd.find_element_by_name("user")

    def is_logged_in(self):
        wd = self.app.wd
        if len(wd.find_elements_by_link_text("Logout")) > 0:
            return True
        else:
            return False

    def is_logged_in_as(self, username):
        return username == self.get_username()

    def get_username(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text[1:-1]

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
