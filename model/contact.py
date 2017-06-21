from sys import maxsize
import re

class Contact:
    def __init__(self, name=None, surname=None, address=None,
                 phone_home=None, phone_mobile=None, phone_work=None, all_phones=None,
                 email=None, email2=None, email3=None, all_emails=None,
                 id=None):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.all_phones = all_phones
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails
        self.id = id

    def __repr__(self):
        return "(id:%s,name:%s,surname:%s,home:%s,phone:%s,email:%s)" % \
               (self.id, self.name, self.surname, self.address, self.phone_home, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.name == other.name and self.surname == other.surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clean(self):
        name = self.name.strip()
        name = re.sub('  ', ' ', name)
        surname = self.surname.strip()
        surname = re.sub('  ', ' ', surname)
        return Contact(id=self.id, name=name, surname=surname)
