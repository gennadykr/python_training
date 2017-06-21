from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/") and len(wd.find_elements_by_name("add")) > 0:
            #print("Already contacts page!")
            pass
        else:
            wd.find_element_by_link_text("home").click()

    def get_the_field(self, field_name):
        wd = self.app.wd
        return wd.find_element_by_name(field_name).get_attribute("value")

    def fill_the_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            element = wd.find_element_by_name(field_name)
            element.click()
            element.clear()
            element.send_keys(text)

    def fill_the_form(self, contact):
        wd = self.app.wd
        self.fill_the_field("firstname",contact.name)
        self.fill_the_field("lastname", contact.surname)
        self.fill_the_field("address", contact.address)
        self.fill_the_field("home", contact.phone_home)
        self.fill_the_field("mobile", contact.phone_mobile)
        self.fill_the_field("work", contact.phone_work)
        self.fill_the_field("email", contact.email)
        self.fill_the_field("email2", contact.email2)
        self.fill_the_field("email3", contact.email3)

    def create(self, contact):
        self.open_contact_page()
        wd = self.app.wd
        # init contact cration
        wd.find_element_by_link_text("add new").click()
        # fill the form
        self.fill_the_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.open_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        self.open_contact_page()
        wd = self.app.wd
        # select first element
        wd.find_elements_by_name("selected[]")[index].click()
        # Delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(index=0,contact=contact)

    def modify_contact_by_index(self, index, contact):
        self.open_contact_page()
        wd = self.app.wd
        # Edit first element
        wd.find_elements_by_xpath("//a[./*[@title='Edit']]")[index].click()
        # fill the form
        self.fill_the_form(contact)
        # Update
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def get_contact_info_from_edit_page_by_index(self, index):
        self.open_contact_page()
        wd = self.app.wd
        wd.find_elements_by_xpath("//a[./*[@title='Edit']]")[index].click()
        name = self.get_the_field("firstname")
        surname = self.get_the_field("lastname")
        address = self.get_the_field("address")
        phone_home = self.get_the_field("home")
        phone_mobile = self.get_the_field("mobile")
        phone_work = self.get_the_field("work")
        email = self.get_the_field("email")
        email2 = self.get_the_field("email2")
        email3 = self.get_the_field("email3")
        self.open_contact_page()
        return Contact(name=name, surname=surname, address=address,
                       phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work,
                       email=email, email2=email2, email3=email3)


    def count(self):
        self.open_contact_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_list(self):
        if self.contact_cache is None:
            print("No contact cache")
            self.open_contact_page()
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                tds = element.find_elements_by_css_selector("td")
                last_name = tds[1].text
                first_name = tds[2].text
                address = tds[3].text
                all_emails = tds[4].text
                all_phones = tds[5].text
                self.contact_cache.append(Contact(id=id, name=first_name, surname=last_name,
                                                  address=address, all_emails=all_emails, all_phones=all_phones))
        else:
            print("Will use cached contact list")
        return list(self.contact_cache)

    def compare(self, contact_list):
        cleaned_contact_list = map(Contact.clean, contact_list)
        l1 = sorted(cleaned_contact_list, key=Contact.id_or_max)
        l2 = sorted(self.get_list(), key=Contact.id_or_max)
        print(l1)
        print(l2)
        for idx, val in enumerate(l1):
            print(idx)
            print(l1[idx])
            print(l2[idx])
            assert l1[idx] == l2[idx]
        assert l1 == l2
        #assert sorted(contact_list, key=Contact.id_or_max) == sorted(self.get_list(), key=Contact.id_or_max)