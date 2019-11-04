from project2.locators.locators import Locators
class Firstpage():

    def __init__(self,driver):
        self.driver=driver
        #type 1 of taking locators from diff file
        self.account_dropdown_xpath=Locators.account_dropdown_xpath
        self.login_button_link_text=Locators.login_button_link_text

    def click_account(self):
        self.driver.find_element_by_xpath(self.account_dropdown_xpath).click()

    def click_login(self):
        self.driver.find_element_by_link_text(self.login_button_link_text).click()