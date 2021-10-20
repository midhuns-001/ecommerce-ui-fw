import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import test_data.testData as td
import time

class CreateAccountPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.createAccountPage_locators = self.pageLocators('CreateAccountPage')
        self.myAccountPage_locators = self.pageLocators('MyAccountPage')

    def isAt(self):
        header_login = self.getElementList(*self.locator(self.registerPage_locators, 'header_login'))
        if len(header_login) > 0:
            return True
        return False

    def createAccount(self):
        self.sendKeys(td.testData("email"), *self.locator(self.createAccountPage_locators, 'input_email'))
        self.elementClick(*self.locator(self.createAccountPage_locators, 'btn_create_account'))
        self.waitForElement(*self.locator(self.createAccountPage_locators, 'header_login'))

        #self.elementClick(*self.locator(self.createAccountPage_locators, 'title'))
        #time.sleep(10)

        self.sendKeys(td.testData("first_name"), *self.locator(self.createAccountPage_locators, 'first_name'))
        self.sendKeys(td.testData("last_name"), *self.locator(self.createAccountPage_locators, 'last_name'))
        self.sendKeys(td.testData("password"), *self.locator(self.createAccountPage_locators, 'password'))

        #DOB
        self.dropdownSelectElement(*self.locator(self.createAccountPage_locators, 'day_of_birth'), selector=td.testData("day_of_birth"))
        self.dropdownSelectElement(*self.locator(self.createAccountPage_locators, 'month_of_birth'), selector=td.testData("month_of_birth"))
        self.dropdownSelectElement(*self.locator(self.createAccountPage_locators, 'year_of_birth'), selector=td.testData("year_of_birth"))

        #address
        self.sendKeys(td.testData("first_name"), *self.locator(self.createAccountPage_locators, 'address_first_name'))
        self.sendKeys(td.testData("last_name"), *self.locator(self.createAccountPage_locators, 'address_last_name'))
        self.sendKeys(td.testData("address"), *self.locator(self.createAccountPage_locators, 'address'))
        self.sendKeys(td.testData("city"), *self.locator(self.createAccountPage_locators, 'city'))

        #state & country
        time.sleep(1)
        self.dropdownSelectElement(*self.locator(self.createAccountPage_locators, 'state'), selector=td.testData("state"), selectorType = "text")
        self.dropdownSelectElement(*self.locator(self.createAccountPage_locators, 'country'), selector=td.testData("country"),selectorType = "text")
        self.sendKeys(td.testData("zip"), *self.locator(self.createAccountPage_locators, 'postcode'))
        time.sleep(1)

        self.sendKeys(td.testData("mobile"), *self.locator(self.createAccountPage_locators, 'mobile'))
        self.elementClick(*self.locator(self.createAccountPage_locators, 'register_submit_btn'))
        self.waitForElement(*self.locator(self.myAccountPage_locators, 'my_account_header'))
