from selenium import webdriver
import time
import unittest
from project2.pages.firstpage import Firstpage
from project2.pages.secondpage import Secondpage
import HtmlTestRunner

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:/Users/kchir/PycharmProjects/Selenium/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('https://www.phptravels.net/')

        firstpage=Firstpage(driver)
        firstpage.click_account()
        firstpage.click_login()

        secondpage=Secondpage(driver)
        secondpage.enter_username('user@phptravels.com')
        secondpage.enter_password('demouser')
        secondpage.click_login()

        # driver.find_element_by_xpath('/html/body/div/header/div[1]/div/div/div[2]/div/ul/li[3]/div/a').click()
        # driver.find_element_by_link_text('Login').click()
        # driver.find_element_by_name('username').send_keys('user@phptravels.com')
        # driver.find_element_by_name('password').send_keys('demouser')
        # driver.find_element_by_xpath('//*[@id="loginfrm"]/button').click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test complete')


if __name__ == 'main':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/kchir/PycharmProjects/Selenium/Reports'))
