# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_adding_contact(app, json_contact):
    contact = json_contact
    contacts_before = app.contact.get_list()
    app.contact.add(contact)
    contacts_after = app.contact.get_list()
    assert len(contacts_before) + 1 == app.contact.count()
    contacts_before.append(contact)
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)

