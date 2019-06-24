from random import choice


def test_adding_contact_to_group(app, orm):
    app.contact.create_if_none()
    app.group.create_if_none()
    contact = choice(orm.get_contact_list())
    group = choice(orm.get_group_list())
    app.contact.add_to_group(contact=contact, group=group)
    contact_id_from_group = orm.get_contacts_id_in_group(group)
    assert int(contact.id) in contact_id_from_group

