from model.group import Group


def test_edit_first_group(app):
    edited_group = Group("Name2", "Header2", "Footer2")
    app.group.create_if_none()
    groups_before = app.group.get_list()
    edited_group.id = groups_before[0].id
    app.group.edit_first(edited_group)
    gropus_after = app.group.get_list()
    assert len(groups_before) == len(gropus_after)
    groups_before[0] = edited_group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(gropus_after, key=Group.id_or_max)
