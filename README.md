## Assignment - UI Automation F/W for an E-commerce store

Description
=============
Test Automation Framework using selenium and Python with the below features:

* Framework is based on page object model.
* Reporting using Allure report.
* Reading locators from JSON file.
* Reading test data from JSON file.

Install Dependency:
=====================
* Install the depended packages in ``requirements.txt`` using ``pip install -r requirements.txt``


Create new test case
=====================

In order to create a new test case using the **Framework**, you have to follow the below steps:

* In **locators module**, create a new locator for the element you would like to use, as below:


        [{
            "pageName": "HomePage",
            "name": "link_login",
            "locateUsing": "xpath",
            "locator": "//a[contains(text(),'Log In')]"
        }]

* In **test data module**, add the test data needed for your test case, as below:

        {
            "environment": "http://automationpractice.com/index.php",
            "browser": "firefox",
            "email": "test@email.com",
            "password": "passwd"
        }


* If the element exist in more than one page (**Navigation element**), use **navigation module** to create a script for that navigation bar and add your navigation action to that element, as below:

        def goToLoginPage(self):
            self.elementClick(*self.locator(self.homePage_locators, 'link_login'))

* If the element exists in only one page, go to **page module** and create a new script for that page e.g: ``login_page.py`` and add all the actions in that page, as below:

        def login(self, email, password):
            self.sendKeys(email, *self.locator(self.loginPage_locators, 'input_email'))
            self.sendKeys(password, *self.locator(self.loginPage_locators, 'input_password'))
            self.elementClick(*self.locator(self.loginPage_locators, 'btn_login'))

* Then, in **test module**, create a new script for your test case(s) e.g: ``test_login.py`` and add your test case, as below:

        @allure.story('story_1') # story of the test case
        @allure.severity(allure.severity_level.MINOR) # severity of the test case
        def test_login_successfully(self):

            with allure.step('Navigate to login page'): # name of the test step
                self.homeNavigation.goToLoginPage()
                self.ts.markFinal(self.loginPage.isAt, "navigation to login page failed") # check if the navigation to login page occurs successfully

            with allure.step('Login'): # name of the test step
                self.loginPage.login(email=td.testData("email"), password=td.testData("password"))
                self.ts.markFinal(self.dashboardPage.isAt, "login failed") # check if login successfully




Run the test case
==================

In order to run the test case after creation, use on of the below commands:

* To run the test case and create allure report on allure dashboard:

``py.test --alluredir=allure_report tests/test_login.py``

``allure serve allure_report``
# ecommerce-ui-fw
