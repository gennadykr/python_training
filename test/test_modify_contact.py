from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="Imia-NEW")
    contact.id = old_contacts[index].id
    contact.surname = old_contacts[index].surname
    app.contact.modify_contact_by_index(index=index,contact=contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_phone(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(name="test"))
#    app.contact.modify_first_contact(Contact(phone="5555555-NEW"))
