from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="Imia2", surname="Familia2", address="Home 2", phone="5555555-2",
                               email="mail-2@example.com"))
    app.session.logout()
