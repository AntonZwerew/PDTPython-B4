# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_adding_group(app):
    group = Group("Name1", "Header1", "Footer1")
    app.session.login(username="admin", password="secret")
    app.group.create(group)
    app.session.logout()


def test_adding_empty_group(app):
    emtpy_group = Group("", "", "")
    app.session.login(username="admin", password="secret")
    app.group.create(emtpy_group)
    app.session.logout()
