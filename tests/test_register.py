from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure

sys.path.insert(0, '../..')


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterUserTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.createAccountPage = CreateAccountPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

    # @pytest.mark.run(order=1)
    @allure.story('epic_2') # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR) # severity of the test case
    def test_create_account_successfully(self):
        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "navigation to login page failed")

        with allure.step('Create an account'):
            self.createAccountPage.createAccount()
            self.ts.markFinal(self.createAccountPage.isAt, "Create account failed")
        with allure.step('Logout'):
            self.loggedInPage.logout()
