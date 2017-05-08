from model.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts