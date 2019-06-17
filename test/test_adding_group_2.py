# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(0, maxlen)])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("Name", 10)]
    for header in ["", random_string("Header", 10)]
    for footer in ["", random_string("Footer", 10)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_adding_group(app, group):
    groups_before = app.group.get_list()
    app.group.create(group)
    groups_after = app.group.get_list()
    assert len(groups_before) + 1 == app.group.count()
    groups_before.append(group)
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)

