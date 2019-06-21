# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_delete_rand_contact(app, db, check_ui):
    if db.count_contacts() == 0:
        app.contact.create(Contact(first_name="123"))
    contacts_before = db.get_contact_list()
    contact = random.choice(contacts_before)
    app.contact.delete_by_id(contact.id)
    contacts_after = db.get_contact_list()
    contacts_before.remove(contact)
    assert contacts_before == contacts_after
    if check_ui:
        assert sorted(contacts_after, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)

