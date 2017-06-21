from model.contact import Contact
import re

def test_contac_fields(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    contacts_from_ui = app.contact.get_list()
    contacts_from_db = db.get_contact_list()

    print(contacts_from_ui)
    print(contacts_from_db)

    assert len(contacts_from_ui) == len(contacts_from_db)

    contacts_from_ui = sorted(contacts_from_ui, key=Contact.id_or_max)
    contacts_from_db = sorted(contacts_from_db, key=Contact.id_or_max)

    for idx, ui_contact in enumerate(contacts_from_ui):
        db_contact = contacts_from_db[idx]
        print(ui_contact)
        print(db_contact)
        assert ui_contact.name == clear_spaces(db_contact.name)
        assert ui_contact.surname == clear_spaces(db_contact.surname)
        assert ui_contact.address == clear_spaces(db_contact.address)

        assert ui_contact.all_phones == merge_phones(db_contact)
        assert ui_contact.all_emails == merge_emails(db_contact)

def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                              map(lambda x: clear(x),
                                  filter(lambda x: x is not None,
                                         [contact.phone_home, contact.phone_mobile, contact.phone_work]))))

def merge_emails(contact):
    return "\n".join(map(lambda x: clear_spaces(x),
                         filter(lambda x: x != "",[contact.email, contact.email2, contact.email3])))


def clear(s):
    return re.sub("[() -]", "", s)

def clear_spaces(s):
    s = s.strip()
    return re.sub("  ", " ", s)