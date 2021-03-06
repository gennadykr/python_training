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
        self.group_cache = None

    def select_first_element(self):
        self.select_element_by_index(0)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def modify_first_group(self,group):
        self.modify_group_by_index(index=0,group=group)

    def select_element_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_element_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_group_by_index(self,index):
        self.open_group_page()
        wd = self.app.wd
        # select the first group
        self.select_element_by_index(index)
        # delete
        wd.find_element_by_name("delete").click()
        self.returns_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.open_group_page()
        wd = self.app.wd
        self.select_element_by_id(id)
        wd.find_element_by_name("delete").click()
        self.returns_to_groups_page()
        self.group_cache = None

    def modify_group_by_index(self, index, group):
        self.open_group_page()
        wd = self.app.wd
        # select the first group
        self.select_element_by_index(index)
        # open group modification
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_the_form(group)
        # update group
        wd.find_element_by_name("update").click()
        self.returns_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, group):
        self.open_group_page()
        wd = self.app.wd
        self.select_element_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_the_form(group)
        wd.find_element_by_name("update").click()
        self.returns_to_groups_page()
        self.group_cache = None

    def count(self):
        self.open_group_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_list(self):
        if self.group_cache is None:
            print("No group cache")
            self.open_group_page()
            wd = self.app.wd
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                name = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=name,id=id))
        else:
            print("Group cache will be used")
        return list(self.group_cache)

    def compare(self, group_list):
        cleaned_group_list = map(Group.clean, group_list)
        assert sorted(cleaned_group_list, key=Group.id_or_max) == sorted(self.get_list(), key=Group.id_or_max)