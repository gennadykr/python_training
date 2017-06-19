from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()
    (index, selected_group) = random.choice(list(enumerate(old_groups)))

    group = Group(name="afdasdfasdfasdf1v2")
    group.id = selected_group.id

    app.group.modify_group_by_id(id=selected_group.id,group=group)

    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        app.group.compare(new_groups)

