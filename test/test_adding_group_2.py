# -*- coding: utf-8 -*-
from model.group import Group


def test_adding_group(app):
    group = Group("Name1", "Header1", "Footer1")
    app.group.create(group)


def test_adding_empty_group(app):
    emtpy_group = Group("", "", "")
    app.group.create(emtpy_group)
