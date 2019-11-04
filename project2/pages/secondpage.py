from project2.locators.locators import Locators
class Secondpage():

    def __init__(self,driver):
        self.driver=driver
        # type 2 of taking locators from diff file

    def enter_username(self,username):
        self.driver.find_element_by_name(Locators.username_textbox_name).clear()
        self.driver.find_element_by_name(Locators.username_textbox_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_name(Locators.password_textbox_name).clear()
        self.driver.find_element_by_name(Locators.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button_xpath).click()