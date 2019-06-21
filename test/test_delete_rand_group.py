import random
from model.group import Group


def test_delete_rand_group(app, db, check_ui):
    if db.count_groups() == 0:
        app.group.create(Group(name="123"))
    groups_before = db.get_group_list()
    group = random.choice(groups_before)
    app.group.delete_by_id(group.id)
    groups_after = db.get_group_list()
    groups_before.remove(group)
    assert groups_before == groups_after
    if check_ui:
        for group in groups_after:
            group.name = group.name.strip()
            group.header = None
            group.footer = None
        assert sorted(groups_after, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)
