# -*- coding: utf-8 -*-
from model.group import Group


def test_adding_group(app):
    group = Group("Name1", "Header1", "Footer1")
    gropus_before = app.group.get_list()
    app.group.create(group)
    gropus_after = app.group.get_list()
    assert len(gropus_before) + 1 == len(gropus_after)


def test_adding_empty_group(app):
    emtpy_group = Group("", "", "")
    gropus_before = app.group.get_list()
    app.group.create(emtpy_group)
    gropus_after = app.group.get_list()
    assert len(gropus_before) + 1 == len(gropus_after)
