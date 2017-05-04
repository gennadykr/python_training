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

    def delete_first_contact(self):
        self.open_contact_page()
        wd = self.app.wd
        # select first element
        wd.find_element_by_name("selected[]").click()
        # Delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()

    def modify_first_contact(self, contact):
        self.open_contact_page()
        wd = self.app.wd
        # Edit first element
        wd.find_element_by_xpath("//a[./*[@title='Edit']]").click()
        # fill the form
        self.fill_the_form(contact)
        # Update
        wd.find_element_by_name("update").click()
        self.open_contact_page()

    def count(self):
        self.open_contact_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
