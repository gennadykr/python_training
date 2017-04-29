from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def open_home_page():
    wd.get("http://localhost/addressbook/")


def login(username, password):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


def open_group_page():
    wd.find_element_by_link_text("groups").click()


def create_group(group):
    # init group creation
    wd.find_element_by_name("new").click()
    # fill group form
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(group.name)
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(group.header)
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(group.footer)
    # submit group creation
    wd.find_element_by_name("submit").click()


def returns_to_groups_page():
    wd.find_element_by_link_text("group page").click()


def logout():
    wd.find_element_by_link_text("Logout").click()


try:
    open_home_page()
    login(username="admin", password="secret")
    open_group_page()
    create_group(Group(name="afd", header="afds", footer="asdf"))
    returns_to_groups_page()
    logout()

finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
