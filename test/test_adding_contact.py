# -*- coding: utf-8 -*-
from model.contact import Contact


def test_adding_contact(app):
    vanya = Contact("Ivan", "Ivanovich", "Ivanov", "Vanya", "/opt/lampp/htdocs/addressbook/title.gif", "Title",
                  "Microsoft", "Moscow, Kursky rail terminal", "8-800-555-35-35", "89855553535", "+7(800)555-35-35",
                  "++7788000055555533553355", "vanya@fsb.ru", "ivan@kgb.su", "Ivanych@ivan.ivan", "google.ru", "15",
                  "November", "2001", "13", "November", "1999", "Name1", "AaddrreesS", "Yjme",
                  "NOasdkalsdjhlkasjgdflhajgdshsjld!")
    contacts_before = app.contact.get_list()
    app.contact.add(vanya)
    contacts_after = app.contact.get_list()
    assert len(contacts_before) + 1 == app.contact.count()
    contacts_before.append(vanya)
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
