from model.group import Group

def test_add_group(app, db, data_groups):
    group = data_groups
    #old_groups = app.group.get_list()
    old_groups = db.get_group_list()
    print(old_groups)
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    #new_groups = app.group.get_list()
    new_groups = db.get_group_list()
    print(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)