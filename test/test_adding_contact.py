# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(0, maxlen)])


def random_day():
    return str(random.randrange(1,31))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return random.choice(months)


def random_year():
    return str(random.randrange(1900,2900))


testdata = [
    Contact(first_name=first_name, middle_name=middle_name, last_name=last_name,
            nickname=nickname, photo=photo, title=title, company=company, address1=address1, phone_home=phone_home,
            phone_mobile=phone_mobile, phone_work=phone_work, phone_fax=phone_fax, email1=email1, email2=email2,
            email3=email3, homepage=homepage, bday_day=bday_day, bday_month=bday_month, bday_year=bday_year,
            aday_day=aday_day, aday_month=aday_month, aday_year=aday_year, address2=address2,
            phone2=phone2, notes=notes)
    for first_name in [random_string("First Name", 10)]
    for middle_name in [random_string("Middle Name", 10)]
    for last_name in [random_string("Last Name", 10)]
    for nickname in [random_string("Footer", 10)]
    for photo in ["/opt/lampp/htdocs/addressbook/title.gif"]
    for title in [random_string("Footer", 10)]
    for company in [random_string("Footer", 10)]
    for address1 in [random_string("Footer", 10)]
    for phone_home in [random_string("Footer", 10)]
    for phone_mobile in [random_string("Footer", 10)]
    for phone_work in [random_string("Footer", 10)]
    for phone_fax in [random_string("Footer", 10)]
    for email1 in [random_string("Footer", 10)]
    for email2 in [random_string("Footer", 10)]
    for email3 in [random_string("Footer", 10)]
    for homepage in [random_string("Footer", 10)]
    for bday_day in [random_day()]
    for bday_month in [random_month()]
    for bday_year in [random_year()]
    for aday_day in [random_day()]
    for aday_month in [random_month()]
    for aday_year in [random_year()]
    for address2 in [random_string("Footer", 10)]
    for phone2 in [random_string("Footer", 10)]
    for notes in [random_string("Footer", 10)]
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_adding_contact(app, contact):
    contacts_before = app.contact.get_list()
    app.contact.add(contact)
    contacts_after = app.contact.get_list()
    assert len(contacts_before) + 1 == app.contact.count()
    contacts_before.append(contact)
    assert sorted(contacts_before, key=Contact.id_or_max) == sorted(contacts_after, key=Contact.id_or_max)

