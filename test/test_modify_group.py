from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    group = Group(name="afdasdfasdfasdf1")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index=index,group=group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.modify_first_group(Group(header="afds123412341234"))

