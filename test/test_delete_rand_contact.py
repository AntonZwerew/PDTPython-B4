# -*- coding: utf-8 -*-
from random import randrange


def test_delete_rand_contact(app):
    app.contact.create_if_none()
    contacts_before = app.contact.get_list()
    index = randrange(0, len(contacts_before))
    app.contact.delete_by_index(index)
    contacts_after = app.contact.get_list()
    assert len(contacts_before) - 1 == app.contact.count()
    contacts_before[index:index+1] = []
    assert contacts_before == contacts_after
