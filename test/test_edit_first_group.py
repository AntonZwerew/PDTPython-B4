from model.group import Group


def test_edit_first_group(app):
    edited_group = Group("Name2", "Header2", "Footer2")
    app.group.create_if_none()
    app.group.edit_first(edited_group)
