from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            self.session.ensure_login(username="admin", password="secret")
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
