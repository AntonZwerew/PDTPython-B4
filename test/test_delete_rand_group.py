from random import randrange


def test_delete_rand_group(app):
    app.group.create_if_none()
    groups_before = app.group.get_list()
    index = randrange(0, len(groups_before))
    app.group.delete_by_index(index)
    groups_after = app.group.get_list()
    assert len(groups_before) - 1 == app.group.count()
    groups_before[index:index+1] = []
    assert groups_before == groups_after
