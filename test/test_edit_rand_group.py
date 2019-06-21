from model.group import Group
from random import randrange


def test_edit_rand_group(app, db, check_ui, json_group):
    edited_group = json_group
    app.group.create_if_none()
    groups_before = db.get_group_list()
    index = randrange(0, len(groups_before))
    edited_group.id = groups_before[index].id
    app.group.edit_group_by_index(group=edited_group, index=index)
    groups_after = db.get_group_list()
    groups_before[index] = edited_group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
    if check_ui:
        for group in groups_after:
            group.name = group.name.strip()
            group.header = None
            group.footer = None
        assert sorted(groups_after, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)

