from model.contact import Contact
import random


def test_modify_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))

    old_contacts = db.get_contact_list()
    (index, selected_contact) = random.choice(list(enumerate(old_contacts)))

    contact = Contact(name="Imia-NEW")
    contact.id = selected_contact.id
    contact.surname = selected_contact.surname

    app.contact.modify_contact_by_id(id=selected_contact.id,contact=contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        app.contact.compare(new_contacts)