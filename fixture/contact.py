from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.contact_cache = None

    def open_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_link_text("All e-mail")) > 0):
            wd.get(self.app.base_url)

    def add(self, contact):
        wd = self.app.wd
        self.open_main_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact=contact)
        wd.find_element_by_name("submit").click()

    def fill_contact(self, contact):
        filler = self.app.filler
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

    def select_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.select_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first(self, contact):
        self.edit_by_index(contact, 0)

    def edit_by_index(self, contact, index):
        wd = self.app.wd
        self.open_to_edit_by_index(index)
        self.fill_contact(contact=contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def view_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        wd.find_elements_by_css_selector("img[alt=Details]")[index].click()

    def open_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        wd.find_elements_by_css_selector("img[alt=Edit]")[index].click()

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
            self.contact_cache = None

    def get_list(self):
        contact_cache = self.contact_cache
        if contact_cache is None:
            wd = self.app.wd
            self.open_main_page()
            contact_cache = []
            for element in wd.find_elements_by_css_selector("[name=entry]"):
                fields = element.find_elements_by_css_selector("td")
                contact_id = fields[0].find_element_by_name("selected[]").get_attribute("value")
                contact_last_name = fields[1].get_attribute("innerText")
                contact_first_name = fields[2].get_attribute("innerText")
                contact_address = fields[3].get_attribute("innerText")
                contact_phones = fields[5].get_attribute("innerText")# .splitlines()
                contact_emails = fields[4].get_attribute("innerText")
                contact_cache.append(Contact(first_name=contact_first_name,
                                             last_name=contact_last_name,
                                             address1=contact_address,
                                             contact_id=contact_id,
                                             all_phones_from_homepage=contact_phones,
                                             all_emails_from_homepage=contact_emails))
        return list(contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        contact = Contact(first_name=firstname,
                          last_name=lastname,
                          contact_id=id,
                          address1=address,
                          phone_home=homephone,
                          phone_work=workphone,
                          phone_mobile=mobilephone,
                          phone_fax=fax,
                          phone2=phone2,
                          email1=email1,
                          email2=email2,
                          email3=email3)
        return contact

    def get_contact_info_from_view_page(self,index):
        wd = self.app.wd
        self.view_by_index(index)
        contact_text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", contact_text).group(1)
        phone_work = re.search("W: (.*)", contact_text).group(1)
        phone_mobile = re.search("M: (.*)", contact_text).group(1)
        phone2 = re.search("P: (.*)", contact_text).group(1)
        return Contact(phone_home=phone_home,
                       phone_work=phone_work,
                       phone_mobile=phone_mobile,
                       phone2=phone2)
