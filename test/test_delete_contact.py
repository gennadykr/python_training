from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.delete_first_contact()
