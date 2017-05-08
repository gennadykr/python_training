from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_list()
    contact = Contact(name="Imia-NEW")
    contact.id = old_contacts[0].id
    contact.surname = old_contacts[0].surname
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_phone(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(name="test"))
#    app.contact.modify_first_contact(Contact(phone="5555555-NEW"))
