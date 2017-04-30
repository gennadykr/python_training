import time

import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(name="Imia", surname="Familia", address="Home", phone="5555555",
                                        email="mail@example.com"))
    app.session.logout()
    time.sleep(3)