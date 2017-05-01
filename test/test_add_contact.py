from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="Imia", surname="Familia", address="Home", phone="5555555",
                               email="mail@example.com"))
    app.session.logout()
