# -*- coding: utf-8 -*-
from model.group import Group


def test_adding_group(app, json_group):
    group = json_group
    groups_before = app.group.get_list()
    app.group.create(group)
    groups_after = app.group.get_list()
    assert len(groups_before) + 1 == app.group.count()
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)

