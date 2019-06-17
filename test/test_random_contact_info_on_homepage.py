import re
import random


def test_random_contact_info_on_homepage(app):
    app.contact.create_if_none()
    index = random.randrange(0, len(app.contact.get_list()))
    contact_from_homepage = app.contact.get_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.first_name == contact_from_edit_page.first_name
    assert contact_from_homepage.last_name == contact_from_edit_page.last_name
    assert contact_from_homepage.address1 == contact_from_edit_page.address1
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[
                                    contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone2]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,[contact.email1, contact.email2, contact.email3])))
