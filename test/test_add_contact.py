from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(name="Imia", surname="Familia", address="Home", phone="5555555",
                               email="mail@example.com"))
