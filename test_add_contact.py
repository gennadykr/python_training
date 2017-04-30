import time
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="Imia", surname="Familia", address="Home", phone="5555555",
                                        email="mail@example.com"))
    app.logout()
    time.sleep(3)