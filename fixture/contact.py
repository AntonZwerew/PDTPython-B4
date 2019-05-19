from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.get("http://localhost/addressbook/")

    def add(self, contact):
        wd = self.app.wd
        filler = self.app.filler
        self.open_main_page()
        wd.find_element_by_link_text("add new").click()
        filler.fill_input_field(element="firstname", text=contact.first_name)
        filler.fill_input_field(element="middlename", text=contact.middle_name)
        filler.fill_input_field(element="lastname", text=contact.last_name)
        filler.fill_input_field(element="nickname", text=contact.nickname)
        filler.fill_photo_field(element="photo", text=contact.photo)
        filler.fill_input_field(element="title", text=contact.title)
        filler.fill_input_field(element="company", text=contact.company)
        filler.fill_input_field(element="address", text=contact.address1)
        filler.fill_input_field(element="home", text=contact.phone_home)
        filler.fill_input_field(element="mobile", text=contact.phone_mobile)
        filler.fill_input_field(element="work", text=contact.phone_work)
        filler.fill_input_field(element="fax", text=contact.phone_fax)
        filler.fill_input_field(element="email", text=contact.email1)
        filler.fill_input_field(element="email2", text=contact.email2)
        filler.fill_input_field(element="email3", text=contact.email3)
        filler.fill_input_field(element="homepage", text=contact.homepage)
        filler.fill_dropdown_list(element="bday", text=contact.bday_day)
        filler.fill_dropdown_list(element="bmonth", text=contact.bday_month)
        filler.fill_input_field(element="byear", text=contact.bday_year)
        filler.fill_dropdown_list(element="aday", text=contact.aday_day)
        filler.fill_dropdown_list(element="amonth", text=contact.aday_month)
        filler.fill_input_field(element="ayear", text=contact.aday_year)
        filler.fill_dropdown_list(element="new_group", text=contact.group)
        filler.fill_input_field(element="address2", text=contact.address2)
        filler.fill_input_field(element="phone2", text=contact.phone2)
        filler.fill_input_field(element="notes", text=contact.notes)
        wd.find_element_by_name("submit").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first(self, contact):
        wd = self.app.wd
        filler = self.app.filler
        self.open_main_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        filler.fill_input_field(element="firstname", text=contact.first_name)
        filler.fill_input_field(element="middlename", text=contact.middle_name)
        filler.fill_input_field(element="lastname", text=contact.last_name)
        filler.fill_input_field(element="nickname", text=contact.nickname)
        filler.fill_photo_field(element="photo", text=contact.photo)
        filler.fill_input_field(element="title", text=contact.title)
        filler.fill_input_field(element="company", text=contact.company)
        filler.fill_input_field(element="address", text=contact.address1)
        filler.fill_input_field(element="home", text=contact.phone_home)
        filler.fill_input_field(element="mobile", text=contact.phone_mobile)
        filler.fill_input_field(element="work", text=contact.phone_work)
        filler.fill_input_field(element="fax", text=contact.phone_fax)
        filler.fill_input_field(element="email", text=contact.email1)
        filler.fill_input_field(element="email2", text=contact.email2)
        filler.fill_input_field(element="email3", text=contact.email3)
        filler.fill_input_field(element="homepage", text=contact.homepage)
        filler.fill_dropdown_list(element="bday", text=contact.bday_day)
        filler.fill_dropdown_list(element="bmonth", text=contact.bday_month)
        filler.fill_input_field(element="byear", text=contact.bday_year)
        filler.fill_dropdown_list(element="aday", text=contact.aday_day)
        filler.fill_dropdown_list(element="amonth", text=contact.aday_month)
        filler.fill_input_field(element="ayear", text=contact.aday_year)
        filler.fill_input_field(element="address2", text=contact.address2)
        filler.fill_input_field(element="phone2", text=contact.phone2)
        filler.fill_input_field(element="notes", text=contact.notes)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_if_none(self):
        vanya = Contact("Ivan", "Ivanovich", "Ivanov", "Vanya", "/opt/lampp/htdocs/addressbook/title.gif", "Title",
                        "Microsoft", "Moscow, Kursky rail terminal", "8-800-555-35-35", "89855553535", "+7(800)555-35-35",
                        "++7788000055555533553355", "vanya@fsb.ru", "ivan@kgb.su", "Ivanych@ivan.ivan", "google.ru", "15",
                        "November", "2001", "13", "November", "1999", "[none]", "AaddrreesS", "Yjme",
                        "NOasdkalsdjhlkasjgdflhajgdshsjld!")
        if self.count() == 0:
            self.add(vanya)

