# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.contact.create_if_none()
    contacts_before = app.contact.get_list()
    app.contact.delete_first()
    contacts_after = app.contact.get_list()
    assert len(contacts_before) - 1 == len(contacts_after)
    contacts_before[0:1] = []
    assert contacts_before == contacts_after
