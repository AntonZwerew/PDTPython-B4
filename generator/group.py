# -*- coding: utf-8 -*-
from model.group import Group
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
file = "data/group.json"


for o, a in opts:
    if o == "-o":
        n = int(a)
    elif o=="-n":
        file = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + '''string.punctuation''' + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(0, maxlen)])


testdata = [
               Group(name="", header="", footer="")
           ] + [
               Group(name=random_string("Name", 10),
                     header=random_string("Header", 10),
                     footer=random_string("Footer", 10))
               for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)


with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
