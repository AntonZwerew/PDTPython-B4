# -*- coding: utf-8 -*-
from model.contact import Contact


def test_adding_contact(app):
    edited_contact = Contact("Petr", "Petrovich", "Petrov", "Petya", "/opt/lampp/htdocs/addressbook/title.png", "Title2",
                    "Macrosoft", "Moscow, Leningradsky rail terminal", "8-800-999-99-99", "89859999999", "+7(800)999-99-99",
                    "++7788000099999999999999", "petya@fsb.ru", "Petr@kgb.su", "petrovich@petr.petr", "yandex.io", "16",
                    "December", "1999", "15", "December", "2000", "Name2", "Adrees", "hfh",
                    "jdjfjfjkafj!")
    app.contact.edit_first(edited_contact)
