# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_adding_contact(app):
    contact_vanya = Contact("Ivan", "Ivanovich", "Ivanov", "Vanya", "/opt/lampp/htdocs/addressbook/title.gif", "Title",
                  "Microsoft", "Moscow, Kursky rail terminal", "8-800-555-35-35", "89855553535", "+7(800)555-35-35",
                  "++7788000055555533553355", "vanya@fsb.ru", "ivan@kgb.su", "Ivanych@ivan.ivan", "google.ru", "15",
                  "November", "2001", "13", "November", "1999", "Name1", "AaddrreesS", "Yjme",
                  "NOasdkalsdjhlkasjgdflhajgdshsjld!")
    app.login("admin", "secret")
    app.add_user(contact_vanya)
    app.logout()

def test_addin_gempy_contact(app): #Этот тест падает
    contact_empty = Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "", "", "", "")
    app.login("admin", "secret")
    app.add_user(contact_empty)
    app.logout()
