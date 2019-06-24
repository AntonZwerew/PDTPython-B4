# -*- coding: utf-8 -*-
from model.group import Group


def test_adding_group(app, orm, check_ui, json_group):
    group = json_group
    groups_before = orm.get_group_list()
    app.group.create(group)
    groups_after = orm.get_group_list()
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
    if check_ui:
        for group in groups_after:
            group.name = group.name.strip()
            group.header = None
            group.footer = None
        assert sorted(groups_after, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)
