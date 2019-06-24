# -*- coding: utf-8 -*-
from model.contact import Contact


def test_adding_contact(app, orm, check_ui, json_contact):
    contact = json_contact
    contacts_before = orm.get_contact_list()
    app.contact.add(contact)
    contacts_after = orm.get_contact_list()
    contacts_before.append(contact)
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
    if check_ui:
        assert sorted(contacts_after, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)

