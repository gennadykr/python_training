from model.contact import Contact


def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="Imia-NEW"))
    app.session.logout()


def test_modify_contact_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(phone="5555555-NEW"))
    app.session.logout()
