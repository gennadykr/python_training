from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="afd", header="afds", footer="asdf"))
