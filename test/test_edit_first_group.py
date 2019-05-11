from model.group import Group

def test_edit_first_group(app):
    edited_group = Group("Name2", "Header2", "Footer2")
    app.session.login(username="admin", password="secret")
    app.group.edit_first(edited_group)
    app.session.logout()
