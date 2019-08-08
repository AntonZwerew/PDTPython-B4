import re
import random
from model.contact import Contact
import pytest


@pytest.mark.skip(reason="test_all_contacts_info_on_homepage includes this test")
def test_random_contact_info_on_homepage(app, orm, check_ui):
    app.contact.create_if_none()
    index = random.randrange(0, len(app.contact.get_list()))
    contact_from_homepage = app.contact.get_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_db = sorted(orm.get_contact_list_homepage(), key=Contact.last_name)[index]
    clear_fields_from_db(contact_from_db)
    assert contact_from_homepage.first_name == contact_from_db.first_name
    assert contact_from_homepage.last_name == contact_from_db.last_name
    assert contact_from_homepage.address1 == contact_from_db.address1
    # В БД хранится как былоо передано, в веб-приложении удаляются часть символов
    # Видимо, это ожидаемое поведение, поэтому делаем то же самое перед сравнением
    # в re.sub внес все, что удалось найти
    assert contact_from_homepage.all_phones_from_homepage == \
           re.sub("[/.\r ]", "", merge_phones_like_on_homepage(contact_from_db))
    assert contact_from_homepage.all_emails_from_homepage == \
           re.sub("[/.]", "", merge_emails_like_on_homepage(contact_from_db))
    if check_ui:
        assert contact_from_homepage.first_name == contact_from_edit_page.first_name
        assert contact_from_homepage.last_name == contact_from_edit_page.last_name
        assert contact_from_homepage.address1 == contact_from_edit_page.address1
        assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
        assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


def test_all_contacts_info_on_homepage(app, orm, check_ui):
    app.contact.create_if_none()
    contacts_from_homepage = app.contact.get_list()
    for index in range(len(contacts_from_homepage)):
        contact_ui = app.contact.get_list()[index]
        contact_db = sorted(orm.get_contact_list_homepage(), key=Contact.last_name)[index]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        clear_fields_from_db(contact_db)
        assert contact_ui.first_name == contact_db.first_name
        assert contact_ui.last_name == contact_db.last_name
        assert contact_ui.address1 == contact_db.address1
        # В БД хранится как былоо передано, в веб-приложении удаляются часть символов
        # Видимо, это ожидаемое поведение, поэтому делаем то же самое перед сравнением
        # в re.sub внес все, что удалось найти
        # Но правила удаления символов видимо более сложные, поэтому тест валится с ошибками
        assert contact_ui.all_phones_from_homepage == \
               re.sub("[/.\r ]", "", merge_phones_like_on_homepage(contact_db))
        assert contact_ui.all_emails_from_homepage == merge_emails_like_on_homepage(contact_db)
        if check_ui:
            assert contact_ui.first_name == contact_from_edit_page.first_name
            assert contact_ui.last_name == contact_from_edit_page.last_name
            assert contact_ui.address1 == contact_from_edit_page.address1
            assert contact_ui.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
            assert contact_ui.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def clear_fields_from_db(contact):
    # В БД хранится как былоо передано, в веб-приложении удаляются пробелы на конце
    # Видимо, это ожидаемое поведение, поэтому делаем то же самое перед сравнением
    try:
        contact.first_name = contact.first_name.rstrip()
    except AttributeError:
        pass
    try:
        contact.last_name = contact.last_name.rstrip()
    except AttributeError:
        pass
    try:
            contact.address1 = contact.address1.rstrip()
    except AttributeError:
        pass
    # contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_db)
    # contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_db)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[
                                    contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone2]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,[contact.email1, contact.email2, contact.email3])))
