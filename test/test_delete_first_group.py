from model.group import Group

def test_delete_first_group(app):
    app.group.create_if_none()
    app.group.delete_first()
