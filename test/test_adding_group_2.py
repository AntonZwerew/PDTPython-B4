# -*- coding: utf-8 -*-
from model.group import Group


def test_adding_group(app):
    group = Group("Name1", "Header1", "Footer1")
    groups_before = app.group.get_list()
    app.group.create(group)
    groups_after = app.group.get_list()
    assert len(groups_before) + 1 == app.group.count()
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)


def test_adding_empty_group(app):
    empty_group = Group("", "", "")
    groups_before = app.group.get_list()
    app.group.create(empty_group)
    groups_after = app.group.get_list()
    assert len(groups_before) + 1 == app.group.count()
    groups_before.append(empty_group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
