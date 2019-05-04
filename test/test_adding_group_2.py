# -*- coding: utf-8 -*-

from group import Group
from application_group import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_adding_group(app):
    group = Group("Name1", "Header1", "Footer1")
    app.login(username="admin", password="secret")
    app.create_group(group)
    app.logout()


def test_adding_empty_group(app):
    emtpy_group = Group("", "", "")
    app.login(username="admin", password="secret")
    app.create_group(emtpy_group)
    app.logout()
