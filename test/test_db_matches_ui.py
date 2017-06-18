from model.group import Group
import re
from timeit import timeit

def test_group_lis(app,db):
    ui_list = app.group.get_list()
    def clean(group):
        name = group.name.strip()
        # double spaces inside group name lead to test fail too
        name = re.sub('  ', ' ', name)
        return Group(id=group.id, name=name)
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

# def test_group_lis(app,db):
#     print(timeit( lambda: app.group.get_list(), number = 1 ))
#     print(timeit( lambda: db.get_group_list(), number = 1000 ))
#     assert False