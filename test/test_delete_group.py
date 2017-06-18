from model.group import Group
import random


def test_delete_group(app, db):
    #if app.group.count() == 0:
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    #old_groups = app.group.get_list()
    old_groups = db.get_group_list()
    #index = randrange(len(old_groups))
    #app.group.delete_group_by_index(index)
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    #assert len(old_groups) - 1 == app.group.count()
    #new_groups = app.group.get_list()
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    #old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups