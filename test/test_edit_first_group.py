from model.group import Group


def test_edit_first_group(app):
    edited_group = Group("Name2", "Header2", "Footer2")
    app.group.create_if_none()
    gropus_before = app.group.get_list()
    app.group.edit_first(edited_group)
    gropus_after = app.group.get_list()
    assert len(gropus_before) == len(gropus_after)
