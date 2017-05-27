from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_list()
    contact = Contact(name="Imia", surname="Familia", address="Home", phone_home="5555555",
                      email="mail@example.com")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
