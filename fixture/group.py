from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            #print("Already group page!")
            pass
        else:
            wd.find_element_by_link_text("groups").click()

    def returns_to_groups_page(self):
        self.open_group_page()
        #wd = self.app.wd
        #if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
        #    print("Already on group page!")
        #    wd.find_element_by_link_text("group page").click()

    def fill_the_form(self,group):
        wd = self.app.wd
        # fill group form
        self.fill_the_field("group_name",group.name)
        self.fill_the_field("group_header",group.header)
        self.fill_the_field("group_footer",group.footer)

    def fill_the_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        self.open_group_page()
        wd = self.app.wd
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_the_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.returns_to_groups_page()

    def delete_first_group(self):
        self.open_group_page()
        wd = self.app.wd
        # select the first group
        wd.find_element_by_name("selected[]").click()
        # delete
        wd.find_element_by_name("delete").click()
        self.returns_to_groups_page()

    def modify_first_group(self, group):
        self.open_group_page()
        wd = self.app.wd
        # select the first group
        wd.find_element_by_name("selected[]").click()
        # open group modification
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_the_form(group)
        # update group
        wd.find_element_by_name("update").click()
        self.returns_to_groups_page()

    def count(self):
        self.open_group_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_list(self):
        self.open_group_page()
        wd = self.app.wd
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            name = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=name,id=id))
        #print(groups)
        return groups