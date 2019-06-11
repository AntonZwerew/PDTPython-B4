
def test_delete_first_group(app):
    app.group.create_if_none()
    groups_before = app.group.get_list()
    app.group.delete_first()
    groups_after = app.group.get_list()
    assert len(groups_before) - 1 == len(groups_after)
    groups_before[0:1] = []
    assert groups_before == groups_after
