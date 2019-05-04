from model.group import Group

def test_delete_first_group(app):
    group = Group("Name1", "Header1", "Footer1")
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()
