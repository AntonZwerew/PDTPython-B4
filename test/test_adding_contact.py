# -*- coding: utf-8 -*-
from model.contact import Contact


def test_adding_contact(app):
    vanya = Contact("Ivan", "Ivanovich", "Ivanov", "Vanya", "/opt/lampp/htdocs/addressbook/title.gif", "Title",
                  "Microsoft", "Moscow, Kursky rail terminal", "8-800-555-35-35", "89855553535", "+7(800)555-35-35",
                  "++7788000055555533553355", "vanya@fsb.ru", "ivan@kgb.su", "Ivanych@ivan.ivan", "google.ru", "15",
                  "November", "2001", "13", "November", "1999", "Name1", "AaddrreesS", "Yjme",
                  "NOasdkalsdjhlkasjgdflhajgdshsjld!")
    app.session.login("admin", "secret")
    app.contact.add(vanya)
    app.session.logout()
