from model.group import Group


def test_group_list(app, orm):

    def clean(group):
        return Group(group_id=group.id, name=group.name.strip())

    ui_groups = app.group.get_list()
    db_groups = map(clean, orm.get_group_list())
    assert sorted(ui_groups, key=Group.id_or_max) == sorted(db_groups, key=Group.id_or_max)
