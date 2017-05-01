class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def fill_the_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.surname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

    def create(self, contact):
        wd = self.app.wd
        # init contact cration
        wd.find_element_by_link_text("add new").click()
        # fill the form
        self.fill_the_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first element
        wd.find_element_by_name("selected[]").click()
        # Delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # Edit first element
        wd.find_element_by_xpath("//a[./*[@title='Edit']]").click()
        # fill the form
        self.fill_the_form(contact)
        # Update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
