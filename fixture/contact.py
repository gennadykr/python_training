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

    def fill_the_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_the_form(self, contact):
        wd = self.app.wd
        self.fill_the_field("firstname",contact.name)
        self.fill_the_field("lastname", contact.surname)
        self.fill_the_field("address", contact.address)
        self.fill_the_field("home", contact.phone)
        self.fill_the_field("email", contact.email)

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
                self.contact_cache.append(Contact(id=id, name=first_name, surname=last_name))
        else:
            print("Will use cached contact list")
        return list(self.contact_cache)