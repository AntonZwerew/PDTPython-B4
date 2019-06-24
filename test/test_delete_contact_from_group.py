from model.group import Group
from model.contact import Contact
from random import choice


def test_delete_contact_from_group(app, orm):
    app.contact.create_if_none()
    app.group.create_if_none()
    groups_with_contacts = []
    for group in orm.get_group_list:
        if len(orm.get_contacts_in_group(group)) > 0:
            groups_with_contacts.append(group)
    if len(groups_with_contacts) == 0:
        app.contact.add_to_group(contact=Contact(first_name="123"), group=Group(name="123"))
    group = choice(groups_with_contacts)
    app.contact.view_by_group(group)
    contacts = orm.get_contacts_in_group(group)
    contact = choice(contacts)
    app.contact.select_by_id(contact.id)
    app.wd.find_element_by_name("remove").click()  # тест падает в этой строчке, если название группы - пустая строка,
    # т к. в этом случае отсутствует кнопка уделания выделенного контакта из группы
    app.wd.find_element_by_class_name("msgbox")
    contacts.remove(contact)
    assert sorted(contacts, key=Contact.id_or_max) == sorted(orm.get_contacts_in_group(group), key=Contact.id_or_max)

