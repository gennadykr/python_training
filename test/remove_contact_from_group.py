# Найти группу, если нет, то создать
# Найти контакт, если нет, то создать
# Проверить, что контакт в групппе, если нет, то добавить
# Удалить контакт из группы, проверить, что его в группе нет (а других изменений в группе нет)

from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    contact = random.choice(db.get_contact_list())

    if contact not in db.get_contacts_in_group(group=group):
        app.contact.add_contact_to_group(id=contact.id, group_id=group.id)

    old_contacts_in_group = db.get_contacts_in_group(group=group)
    old_contacts_in_group.remove(contact)

    app.contact.remove_contact_from_group(id=contact.id, group_id=group.id)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == \
           sorted(db.get_contacts_in_group(group=group), key=Contact.id_or_max)