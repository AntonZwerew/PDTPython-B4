# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app, json_contact):
    edited_contact = json_contact
    app.contact.create_if_none()
    contacts_before = app.contact.get_list()
    index = randrange(0, len(contacts_before))
    # index = 0
    edited_contact.id = contacts_before[index].id
    app.contact.edit_by_index(contact=edited_contact, index=index)
    contacts_after = app.contact.get_list()
    assert len(contacts_before) == app.contact.count()
    contacts_before[index] = edited_contact
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
