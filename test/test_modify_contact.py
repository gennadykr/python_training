from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(name="Imia-NEW"))


def test_modify_contact_phone(app):
    app.contact.modify_first_contact(Contact(phone="5555555-NEW"))
