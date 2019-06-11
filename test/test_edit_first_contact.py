# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    edited_contact = Contact("Petr", "Petrovich", "Petrov", "Petya", "/opt/lampp/htdocs/addressbook/title.png", "Title2",
                    "Macrosoft", "Moscow, Leningradsky rail terminal", "8-800-999-99-99", "89859999999", "+7(800)999-99-99",
                    "++7788000099999999999999", "petya@fsb.ru", "Petr@kgb.su", "petrovich@petr.petr", "yandex.io", "16",
                    "December", "1999", "15", "December", "2000", "Name2", "Adrees", "hfh",
                    "jdjfjfjkafj!")
    app.contact.create_if_none()
    contacts_before = app.contact.get_list()
    edited_contact.id = contacts_before[0].id
    app.contact.edit_first(edited_contact)
    contacts_after = app.contact.get_list()
    assert len(contacts_before) == len(contacts_after)
    contacts_before[0] = edited_contact
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
