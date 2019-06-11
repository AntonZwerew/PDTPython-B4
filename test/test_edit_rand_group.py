from model.group import Group
from random import randrange


def test_edit_rand_group(app):
    edited_group = Group("Name2", "Header2", "Footer2")
    app.group.create_if_none()
    groups_before = app.group.get_list()
    index = randrange(0, len(groups_before))
    edited_group.id = groups_before[index].id
    app.group.edit_group_by_index(group=edited_group, index=index)
    gropus_after = app.group.get_list()
    assert len(groups_before) == app.group.count()
    groups_before[index] = edited_group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(gropus_after, key=Group.id_or_max)
