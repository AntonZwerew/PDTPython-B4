from model.contact import Contact


def test_contacts_on_homepage(app, orm):
    contact_from_homepage = app.contact.get_list()
    contacts_from_db = orm.get_contact_list()
    assert sorted(contact_from_homepage, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
