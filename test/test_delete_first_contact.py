# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.contact.create_if_none()
    app.contact.delete_first()
