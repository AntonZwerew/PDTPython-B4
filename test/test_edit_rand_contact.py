# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app, orm, check_ui, json_contact):
    edited_contact = json_contact
    app.contact.create_if_none()
    contacts_before = orm.get_contact_list()
    index = randrange(0, len(contacts_before))
    # index = 0
    edited_contact.id = contacts_before[index].id
    app.contact.edit_by_index(contact=edited_contact, index=index)
    contacts_after = orm.get_contact_list()
    contacts_before[index] = edited_contact
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)
    if check_ui:
        assert sorted(contacts_after, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)
