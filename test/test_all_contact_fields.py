from model.contact import Contact
from random import randrange
import re

def test_contac_fields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    all_contacts = app.contact.get_list()
    index = randrange(len(all_contacts))
    #index = 2

    contact_from_home_page = all_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(index)

    #print(contact_from_edit_page)
    #print(contact_from_home_page)

    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.surname == contact_from_edit_page.surname
    assert contact_from_home_page.address == contact_from_edit_page.address

    assert contact_from_home_page.all_phones == merge_phones(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails(contact_from_edit_page)

def merge_phones(contact):
    return "\n".join( filter(lambda x: x != "",
                              map(lambda x: clear(x),
                                  filter(lambda x: x is not None,
                                         [contact.phone_home, contact.phone_mobile, contact.phone_work]))))

def merge_emails(contact):
    return "\n".join( filter(lambda x: x != "",[contact.email, contact.email2, contact.email3]))


def clear(s):
    return re.sub("[() -]", "", s)