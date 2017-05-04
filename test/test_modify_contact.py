from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_first_contact(Contact(name="Imia-NEW"))


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_first_contact(Contact(phone="5555555-NEW"))
