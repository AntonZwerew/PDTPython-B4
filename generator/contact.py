# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import sys
import getopt


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as e:
    getopt.usage()
    sys.exit(2)


n = 5
file = "data/contact.json"


for o, a in opts:
    if o == "-o":
        n = int(a)
    elif o=="-n":
        file = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + '''string.punctuation''' + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(0, maxlen)])


def random_phone(maxlen):
    phone = '''string.ascii_letters''' + string.digits + string.punctuation + " "
    return "".join([random.choice(phone) for i in range(0, maxlen)])


def random_day():
    return str(random.randrange(1,31))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return random.choice(months)


def random_year():
    return str(random.randrange(1900,2900))


testdata = [
    Contact(first_name="",
            middle_name="",
            last_name="",
            nickname="",
            title="",
            company="",
            address1="",
            phone_home="",
            phone_mobile="",
            phone_work="",
            phone_fax="",
            email1="",
            email2="",
            email3="",
            homepage="",
            address2="",
            phone2="",
            notes="")
           ] + [
    Contact(first_name=random_string("First Name", 10),
            middle_name=random_string("Middle Name", 10),
            last_name=random_string("Last Name", 10),
            nickname=random_string("Nickname", 10),
            photo="/opt/lampp/htdocs/addressbook/title.gif",
            title=random_string("Title", 10),
            company=random_string("Company", 10),
            address1=random_string("Address 1", 10),
            phone_home=random_phone(10),
            phone_mobile=random_phone(10),
            phone_work=random_phone(10),
            phone_fax=random_phone(10),
            email1=random_string("Email 1", 10),
            email2=random_string("Email 2", 10),
            email3=random_string("Email 3", 10),
            homepage=random_string("Homeoage", 10),
            bday_day=random_day(),
            bday_month=random_month(),
            bday_year=random_year(),
            aday_day=random_day(),
            aday_month=random_month(),
            aday_year=random_year(),
            address2=random_string("Address 2", 10),
            phone2=random_phone(10),
            notes=random_string("Notes", 10))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)


with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
