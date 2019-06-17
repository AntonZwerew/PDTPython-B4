from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.filler import FillerHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError("Unknown browser: %s" % browser)
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.filler = FillerHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            self.session.ensure_login(username=self.username, password=self.password)
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
