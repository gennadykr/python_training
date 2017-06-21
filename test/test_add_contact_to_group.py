# Найти группу, если нет, то создать
# Найти контакты вне группы, если нет, то создать
# Добавить контакт в группу, проверить, что он в группе

from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())

    if len(db.get_contacts_not_in_group(group=group)) == 0:
        app.contact.create(Contact(name="test"))
    contact = random.choice(db.get_contacts_not_in_group(group=group))

    app.contact.add_contact_to_group(id=contact.id, group_id=group.id)
    assert contact in db.get_contacts_in_group(group=group)