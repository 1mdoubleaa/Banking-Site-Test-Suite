# test_Customers.py
# Authors: Mark Mekhail, Muhammad Anwar, Tolihat Gbadebo
# Date: August 8th, 2023
# Description: This contains all nine test modules for the Guru99 Bank site. For each module, all of the
# all unit tests are appropriately tested according to the steps given in the Excel sheet.

# Importing the necessary modules to set up unit tests with Selenium webdriver.
import unittest
from browser_utils import get_driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Importing the WebDriverWait class and expected_conditions class to handle alerts.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing select to deal with dropdown menus.
from selenium.webdriver.support.ui import Select

# Importing NoSuchElementException to handle missing elements from webpage redirects.
from selenium.common.exceptions import NoSuchElementException

# Importing time to make use of its sleep function.
import time


class NewCustomer(unittest.TestCase):
    @classmethod

    # Setting up tests by maximizing the window, navigating to the website, and logging in as manager.
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        cls.driver.find_element("name", "uid").send_keys("mngr517721")
        cls.driver.find_element("name", "password").send_keys("EtAjeha")
        cls.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_name_field(self):
        """Test 01: Leaving the customer name field blank."""

        # For all tests, we simply need to navigate to the specific page for each module.
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        # For most tests, the "name" attribute is used to locate and send keys to the element.
        driver.find_element("name", "name").send_keys(Keys.TAB)

        # Storing the actual output text in a variable to use for assertion.
        actual_error = driver.find_element(By.XPATH, "//label[@id='message']").text
        expected_error = "Customer name must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_02_verify_name_field(self):
        """Test 02: Using numbers in the name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        # When dealing with multiple inputs, we can create a list and use a for loop to iterate over
        # this list and individually assert each piece of input data.
        inputs = ["1234", "name123"]

        for value in inputs:
            # Opening with clear() on every iteration so inputs do not stack.
            driver.find_element("name", "name").clear()
            driver.find_element("name", "name").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message']").text
            expected_error = "Numbers are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_03_verify_name_field(self):
        """Test 03: Using special characters in the name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["name!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "name").clear()
            driver.find_element("name", "name").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_04_verify_name_field(self):
        """Test 04: Using space as first character in the name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "name").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_addr_field(self):
        """Test 05: Leaving the address field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "addr").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message3']").text
        expected_error = "Address Field must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_06_verify_addr_field(self):
        """Test 06: Using space as the first character in the address field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "addr").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message3']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_07_verify_city_field(self):
        """Test 07: Leaving the city field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "city").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message4']").text
        expected_error = "City Field must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_08_verify_city_field(self):
        """Test 08: Using numbers in the city field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["1234", "city123"]

        for value in inputs:
            driver.find_element("name", "city").clear()
            driver.find_element("name", "city").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message4']").text
            expected_error = "Numbers are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_09_verify_city_field(self):
        """Test 09: Using special characters in the city field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["City!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "city").clear()
            driver.find_element("name", "city").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message4']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_10_verify_city_field(self):
        """Test 10: Using space as the first character in the city field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "city").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message4']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_11_verify_state_field(self):
        """Test 11: Leaving the state field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "state").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message5']").text
        expected_error = "State must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_12_verify_state_field(self):
        """Test 12: Using numbers in the test field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["1234", "State123"]

        for value in inputs:
            driver.find_element("name", "state").clear()
            driver.find_element("name", "state").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message5']").text
            expected_error = "Numbers are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_13_verify_state_field(self):
        """Test 13: Using special characters in the state field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["State!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "state").clear()
            driver.find_element("name", "state").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message5']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_14_verify_state_field(self):
        """Test 14: Using space as the first character in the state field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "state").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message5']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_15_verify_pin_field(self):
        """Test 15: Using characters in the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["PIN", "1234PIN"]

        for value in inputs:
            driver.find_element("name", "pinno").clear()
            driver.find_element("name", "pinno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_16_verify_pin_field(self):
        """Test 16: Leaving the PIN field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "pinno").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
        expected_error = "PIN Code must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_17_verify_pin_field(self):
        """Test 17: Entering less than 6 digits in the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["12", "123"]

        for value in inputs:
            driver.find_element("name", "pinno").clear()
            driver.find_element("name", "pinno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
            expected_error = "PIN Code must have 6 Digits"
            self.assertEqual(actual_error, expected_error)

    def test_18_verify_pin_field(self):
        """Test 18: Using special characters in the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["!@#", "123!@#"]

        for value in inputs:
            driver.find_element("name", "pinno").clear()
            driver.find_element("name", "pinno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_19_verify_pin_field(self):
        """Test 19: Using space as the first character in the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "pinno").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_20_verify_pin_field(self):
        """Test 20: Entering blank space in PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "pinno").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_21_verify_mobile_num_field(self):
        """Test 21: Leaving the mobile number field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "telephoneno").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message7']").text
        expected_error = "Mobile no must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_22_verify_mobile_num_field(self):
        """Test 22: Using space as the first character in the mobile number field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "telephoneno").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message7']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_23_verify_mobile_num_field(self):
        """Test 23: Entering blank space in between digits in the mobile number field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "telephoneno").send_keys("123 123")

        actual_error = driver.find_element(By.XPATH, "//label[@id='message7']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_24_verify_mobile_num_field(self):
        """Test 24: Using special characters in the mobile number field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = ["886636!@12", "!@88662682", "88663682!@"]

        for value in inputs:
            driver.find_element("name", "telephoneno").clear()
            driver.find_element("name", "telephoneno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message7']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_25_verify_email_field(self):
        """Test 25: Leaving the e-mail field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "emailid").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message9']").text
        expected_error = "Email-ID must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_26_verify_email_field(self):
        """Test 26: Entering invalid e-mail combinations in the e-mail field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        inputs = [
            "guru99@gmail",
            "guru99",
            "Guru99@",
            "guru99@gmail.",
            "guru99gmail.com",
        ]

        for value in inputs:
            driver.find_element("name", "emailid").clear()
            driver.find_element("name", "emailid").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message9']").text
            expected_error = "Email-ID is not valid"
            self.assertEqual(actual_error, expected_error)

    def test_27_verify_email_field(self):
        """Entering a blank space as the first character in the e-mail field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "emailid").send_keys(Keys.SPACE)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message9']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_28_verify_password_field(self):
        """Test 28: Leaving the password field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        driver.find_element("name", "password").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message18']").text
        expected_error = "Password must not be blank"
        self.assertEqual(actual_error, expected_error)


class EditCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        cls.driver.find_element("name", "uid").send_keys("mngr517721")
        cls.driver.find_element("name", "password").send_keys("EtAjeha")
        cls.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_cusid(self):
        """Test 01: Leaving the customer ID field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
        expected_error = "Customer ID is required"

        self.assertEqual(actual_error, expected_error)

    def test_02_verify_cusid(self):
        """Test 02: Entering characters in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        inputs = ["1234Acc", "Acc123"]

        for value in inputs:
            driver.find_element("name", "cusid").clear()
            driver.find_element("name", "cusid").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message14']"
            ).text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_03_verify_cusid(self):
        """Test 03: Entering special characters in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        inputs = ["123!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "cusid").clear()
            driver.find_element("name", "cusid").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message14']"
            ).text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_04_verify_cusid(self):
        """Test 04: Entering a valid customer ID in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        actual_url = self.driver.current_url
        expected_url = "https://demo.guru99.com/V4/manager/editCustomerPage.php"

        self.assertEqual(actual_url, expected_url)

    def test_05_verify_addr_field(self):
        """Test 05: Clearing and leaving address field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.find_element("name", "addr").clear()
        driver.find_element("name", "addr").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message3']").text
        expected_error = "Address Field must not be blank"

        self.assertEqual(actual_error, expected_error)

    def test_06_verify_city_field(self):
        """Test 06: Clearing and leaving the city field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.find_element("name", "city").clear()
        driver.find_element("name", "city").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message4']").text
        expected_error = "City Field must not be blank"

        self.assertEqual(actual_error, expected_error)

    def test_07_verify_city_field(self):
        """Test 07: Entering numeric values in the city field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["1234", "city123"]

        for value in inputs:
            driver.find_element("name", "city").clear()
            driver.find_element("name", "city").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message4']").text
            expected_error = "Numbers are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_08_verify_addr_field(self):
        """Test 08: Entering special characters in the city field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["City!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "city").clear()
            driver.find_element("name", "city").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message4']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_09_verify_state_field(self):
        """Test 09: Clearing and leaving the state field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.find_element("name", "state").clear()
        driver.find_element("name", "state").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message5']").text
        expected_error = "State must not be blank"

        self.assertEqual(actual_error, expected_error)

    def test_10_verify_state_field(self):
        """Test 10: Entering numeric values in the state field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["1234", "State123"]

        for value in inputs:
            driver.find_element("name", "state").clear()
            driver.find_element("name", "state").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message5']").text
            expected_error = "Numbers are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_11_verify_state_field(self):
        """Test 11: Entering special characters in the state field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["State!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "state").clear()
            driver.find_element("name", "state").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message5']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_12_verify_pin_field(self):
        """Test 12: Entering characters in the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["Pin", "1234PIN"]

        for value in inputs:
            driver.find_element("name", "pinno").clear()
            driver.find_element("name", "pinno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_13_verify_pin_field(self):
        """Test 13: Clearing and leaving the PIN field blank."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.find_element("name", "pinno").clear()
        driver.find_element("name", "pinno").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
        expected_error = "PIN Code must not be blank"

        self.assertEqual(actual_error, expected_error)

    def test_14_verify_pin_field(self):
        """Test 14: Testing an invalid amount of digits for the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["12345", "123"]

        for value in inputs:
            driver.find_element("name", "pinno").clear()
            driver.find_element("name", "pinno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
            expected_error = "PIN Code must have 6 Digits"
            self.assertEqual(actual_error, expected_error)

    def test_15_verify_pin_field(self):
        """Test 15: Testing an invalid amount of digits for the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["!@#", "123!@#"]

        for value in inputs:
            driver.find_element("name", "pinno").clear()
            driver.find_element("name", "pinno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message6']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_16_verify_mobile_num_field(self):
        """Test 16: Clearing and leaving the mobile number field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.find_element("name", "telephoneno").clear()
        driver.find_element("name", "telephoneno").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message7']").text
        expected_error = "Mobile no must not be blank"

        self.assertEqual(actual_error, expected_error)

    def test_17_verify_mobile_num_field(self):
        """Test 17: Entering special characters in the PIN field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["886636!@12", "!@88662682", "88663682!@"]

        for value in inputs:
            driver.find_element("name", "telephoneno").clear()
            driver.find_element("name", "telephoneno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message7']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_18_verify_email_field(self):
        """Test 18: Clearing and leaving the e-mail field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.find_element("name", "emailid").clear()
        driver.find_element("name", "emailid").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message9']").text
        expected_error = "Email-ID must not be blank"

        self.assertEqual(actual_error, expected_error)

    def test_19_verify_email_field(self):
        """Test 19: Entering invalid e-mail addresses in the e-mail field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        inputs = ["guru99@gmail", "guru99", "Guru99@", "gurugmail.com"]

        for value in inputs:
            driver.find_element("name", "emailid").clear()
            driver.find_element("name", "emailid").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message9']").text
            expected_error = "Email-ID is not valid"
            self.assertEqual(actual_error, expected_error)

    def test_20_verify_submit_button(self):
        """Test 20: Changing a valid customer's address and submitting."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.find_element("name", "addr").clear()
        driver.find_element("name", "addr").send_keys("Avenue Road West")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Waiting for 5 seconds until an alert appears.
        WebDriverWait(driver, 5).until(EC.alert_is_present())

        # If an alert is present, focus will be switched to the alert.
        alert = driver.switch_to.alert

        # Capturing the text within the alert to use for assertion.
        actual_text = alert.text

        expected_text = "No Changes made to Customer records"
        self.assertEqual(actual_text, expected_text)


class DeleteCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        cls.driver.find_element("name", "uid").send_keys("mngr517721")
        cls.driver.find_element("name", "password").send_keys("EtAjeha")
        cls.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_customer_id(self):
        """Test 01: Leaving the customer ID field empty."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        driver.find_element("name", "cusid").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
        expected_error = "Customer ID is required"

        self.assertEqual(actual_error, expected_error)

    def test_02_verify_customer_id(self):
        """Test 02: Entering characters in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        inputs = ["Acc", "Acc1234"]

        for value in inputs:
            driver.find_element("name", "cusid").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message14']"
            ).text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_03_verify_customer_id(self):
        """Test 03: Entering special characters in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        inputs = ["123!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "cusid").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message14']"
            ).text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_04_verify_customer_id(self):
        """Test 04: Entering blank space between digits in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        driver.find_element("name", "cusid").send_keys("123 12")

        actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
        expected_error = "Characters are not allowed"

        self.assertEqual(actual_error, expected_error)

    def test_05_verify_customer_id(self):
        """Test 05: Entering blank space as first character in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        driver.find_element("name", "cusid").send_keys(Keys.SPACE, Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
        expected_error = "First character can not have space"

        self.assertEqual(actual_error, expected_error)

    def test_06_verify_customer_id(self):
        """Test 06: Entering valid customer ID in the customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        driver.find_element("name", "cusid").click()
        driver.find_element("name", "cusid").send_keys("123456")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        confirmation_alert = driver.switch_to.alert
        confirmation_alert.accept()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        error_alert = driver.switch_to.alert

        actual_error = error_alert.text
        expected_error = "Customer does not exist!!"
        self.assertEqual(actual_error, expected_error)

        error_alert.accept()

    def test_07_verify_customer_id(self):
        """Test 07: Entering a valid customer ID in the delete customer ID field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        driver.find_element("name", "cusid").send_keys("61692")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        confirmation_alert = driver.switch_to.alert
        confirmation_alert.accept()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        error_alert = driver.switch_to.alert

        actual_error = error_alert.text
        expected_error = "Customer does not exist!!"

        self.assertEqual(actual_error, expected_error)

        error_alert.accept()

    def test_08_verify_customer_id(self):
        """Test 08: Entering a random value in the customer ID field and using the reset button."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

        time.sleep(1)
        driver.find_element("name", "cusid").send_keys("qwer")
        driver.find_element(By.XPATH, "//input[@type='reset']").click()
        time.sleep(1)

        actual_error = driver.find_element("name", "cusid").text
        expected_error = ""
        self.assertEqual(actual_error, expected_error)


class NewAccount(unittest.TestCase):
    # Class method
    @classmethod
    def setUpClass(cls):
        # open the browser
        cls.driver = get_driver()
        cls.driver.maximize_window()
        # Include a try & except for browser
        cls.driver.get("https://demo.guru99.com/V4/")  # link
        # click on userID
        cls.driver.find_element(
            By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]"
        ).send_keys("mngr517721")
        # password
        cls.driver.find_element(
            By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]"
        ).send_keys("EtAjeha")
        # click on login
        cls.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_name(self):
        """Test 01: Blank field.""" ""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")
        driver.find_element("name", "cusid").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
        expected_error = "Customer ID is required"
        self.assertEqual(expected_error, actual_error)

    def test_02_verify_name(self):
        """Test 02: Using characters in name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        inputs = ["1234Acc", "Acc123"]

        for value in inputs:
            driver.find_element("name", "cusid").clear()
            driver.find_element("name", "cusid").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message14']"
            ).text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_03_verify_name(self):
        """Test 03: Using special characters in name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        inputs = ["123!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "cusid").clear()
            driver.find_element("name", "cusid").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message14']"
            ).text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_04_verify_name(self):
        """Test 04: Using blank space in name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("123 12")

        actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_name(self):
        """Test 05: Using space as first character."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element(By.NAME, "inideposit").send_keys(Keys.SPACE, Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message19']").text

        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_06_verify_initial_deposit(self):
        """Test 06: Leaving initial deposit blank"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message19']").text

        expected_error = "Initial Deposit must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_07_verify_initial_deposit(self):
        """Test 07: Blank field."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        inputs = ["1234Acc", "Acc123"]

        for value in inputs:
            driver.find_element("name", "inideposit").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message19']"
            ).text
            expected_error = "Characters are not allowed"
            self.assertEqual(expected_error, actual_error)

    def test_08_verify_initial_deposit(self):
        """Test 09: Using special characters."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        inputs = ["123!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "inideposit").clear()
            driver.find_element("name", "inideposit").send_keys(value)
            actual_error = driver.find_element(
                By.XPATH, "//label[@id='message19']"
            ).text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_09_verify_initial_deposit(self):
        """Test 9: Using space in initial deposit."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "inideposit").send_keys("123 12")

        actual_error = driver.find_element(By.XPATH, "//label[@id='message19']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_10_verify_initial_deposit(self):
        """Test 10: Using space as first character in initial deposit."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "inideposit").send_keys(Keys.SPACE, Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message19']").text
        expected_error = "First character can not have space"
        self.assertEqual(actual_error, expected_error)

    def test_11_verify_account_dropdown(self):
        """Test 11: Selecting Savings from dropdown menu."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        dropdown = driver.find_element(By.XPATH, "//select[@name='selaccount']")

        select = Select(dropdown)
        select.select_by_visible_text("Savings")
        selected_option = select.first_selected_option.text
        self.assertEqual(selected_option, "Savings")

    def test_12_verify_account_dropdown(self):
        """Test 12: Selecting Current from dropdown menu."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        dropdown = driver.find_element(By.XPATH, "//select[@name='selaccount']")

        select = Select(dropdown)
        select.select_by_visible_text("Current")
        selected_option = select.first_selected_option.text
        self.assertEqual(selected_option, "Current")

    def test_13_reset_button(self):
        """Test 13: Entering any values in Customer ID and initial deposit fields."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("qwer")
        driver.find_element("name", "inideposit").send_keys("123456")

        driver.find_element(By.XPATH, "//input[@type='reset']").click()

        driver.find_element("name", "cusid").click()
        time.sleep(2)

        actual_result = driver.find_element("name", "cusid").text
        expected_error = ""
        self.assertEqual(actual_result, expected_error)

    def test_14_submit_button(self):
        """Test 14: Entering incorrect Customer ID."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("123456")
        driver.find_element("name", "inideposit").send_keys("1234")

        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        error_alert = driver.switch_to.alert

        actual_error = error_alert.text
        expected_error = "Customer does not exist!!"
        self.assertEqual(actual_error, expected_error)

        error_alert.accept()

    def test_15_submit_button(self):
        """Test 15: Entering correct Customer ID."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element("name", "inideposit").send_keys("1235")

        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        actual_text = driver.find_element(By.XPATH, "//p[@class='heading3']").text

        expected_text = "Account Generated Successfully!!!"

        self.assertEqual(actual_text, expected_text)

    def test_16_continue_hyperlink(self):
        """Test 16: Continuing after generating a new account."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element("name", "inideposit").send_keys("1235")

        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        time.sleep(4)

        # Asserting only a part of the URL due to various ads preventing proper continuation.
        actual_url = self.driver.current_url
        expected_url_part = "AccCreateMsg.php?aid"
        self.assertIn(expected_url_part, actual_url)


class EditAccount(unittest.TestCase):
    # Class method
    @classmethod
    def setUpClass(cls):
        # open the browser
        cls.driver = get_driver()
        cls.driver.maximize_window()
        # Include a try & except for browser
        cls.driver.get("https://demo.guru99.com/V4/")  # link
        # click on userID
        cls.driver.find_element(
            By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]"
        ).send_keys("mngr517721")
        # password
        cls.driver.find_element(
            By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]"
        ).send_keys("EtAjeha")
        # click on login
        cls.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_name(self):
        """Test 01: Blank field.""" ""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")
        driver.find_element("name", "accountno").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Account Number must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_02_verify_name(self):
        """Test 02: Using numbers."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        inputs = ["Acc", "Acc123"]

        for value in inputs:
            driver.find_element("name", "accountno").clear()
            driver.find_element("name", "accountno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_03_verify_name(self):
        """Test 03: Using special characters in name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        inputs = ["123!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "accountno").clear()
            driver.find_element("name", "accountno").send_keys(value)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Special characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_04_verify_name(self):
        """Test 04: Using space in between account number digits."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        driver.find_element("name", "accountno").send_keys("123 12")

        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_name(self):
        """Test 05: Using space as first character."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        driver.find_element("name", "accountno").send_keys(Keys.SPACE, Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_06_verify_valid_account(self):
        """Test 06: Entering a valid account number."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        valid_account_number = "125190"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(3)

        actual_url = driver.current_url
        expected_url = "https://demo.guru99.com/V4/manager/editAccountPage.php"

        self.assertEqual(actual_url, expected_url)

    def test_07_verify_invalid_account(self):
        """Test 07: Entering an invalid account number."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        invalid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(invalid_account_number)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        error_alert = driver.switch_to.alert
        actual_error = error_alert.text

        expected_result = "Account does not exist"
        self.assertEqual(actual_error, expected_result)

        error_alert.accept()

    def test_08_reset_button(self):
        """Test 08: Testing the reset button."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        valid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)
        driver.find_element(By.XPATH, "//input[@type='reset']").click()

        actual_result = driver.find_element(By.NAME, "accountno").text
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


class DeleteAccount(unittest.TestCase):
    # Class method
    @classmethod
    def setUpClass(cls):
        # open the browser
        cls.driver = get_driver()
        cls.driver.maximize_window()
        # Include a try & except for browser
        cls.driver.get("https://demo.guru99.com/V4/")  # link
        # click on userID
        cls.driver.find_element(
            By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]"
        ).send_keys("mngr517721")
        # password
        cls.driver.find_element(
            By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]"
        ).send_keys("EtAjeha")
        # click on login
        cls.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_name(self):
        """Test 01: Leaving account number field blank.""" ""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        driver.find_element("name", "accountno").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Account Number must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_02_verify_name(self):
        """Test 02: Using characters in account number field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        inputs = ["Acc", "Acc123"]

        for value in inputs:
            driver.find_element("name", "accountno").clear()
            driver.find_element("name", "accountno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_03_verify_name(self):
        """Test 03: Using special characters in name field."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        inputs = ["name!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "accountno").clear()
            driver.find_element("name", "accountno").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_04_verify_name(self):
        """Test 04: Using space in between account number digits."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        driver.find_element("name", "accountno").send_keys("123 12")

        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_name(self):
        """Test 05: Using space as first character in account number."""

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        driver.find_element("name", "accountno").send_keys(Keys.SPACE, Keys.TAB)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_06_verify_valid_account(self):
        """Test 06: Entering an valid account number for deletion."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        valid_account_number = "125190"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)
        driver.find_element(By.NAME, "AccSubmit").click()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        confirmation_alert = driver.switch_to.alert
        confirmation_alert.accept()

        time.sleep(2)
        actual_url = driver.current_url
        expected_url = "https://demo.guru99.com/V4/manager/DeleteAccount.php"
        self.assertEqual(actual_url, expected_url)

    def test_07_verify_invalid_account(self):
        """Test 06: Entering an invalid account number for deletion."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        invalid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(invalid_account_number)
        driver.find_element(By.NAME, "AccSubmit").click()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        confirmation_alert = driver.switch_to.alert
        confirmation_alert.accept()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        error_alert = driver.switch_to.alert
        actual_error = error_alert.text

        confirmation_alert.accept()
        expected_result = "Account does not exist"
        self.assertEqual(actual_error, expected_result)

    def test_08_reset_button(self):
        """Test 08: Testing the reset button."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        driver.find_element(By.NAME, "accountno").send_keys("qwer")
        driver.find_element(By.XPATH, "//input[@type='reset']").click()
        driver.find_element("name", "accountno").click()
        time.sleep(2)

        actual_result = driver.find_element(By.XPATH, "//input[@type='text']").text
        expected_result = ""
        self.assertEqual(actual_result, expected_result)


class BalanceEnquiry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        time.sleep(3)
        cls.driver.find_element("name", "uid").send_keys("mngr517721")
        cls.driver.find_element("name", "password").send_keys("EtAjeha")
        cls.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_account_number(self):
        """Account number cannot be empty"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        inputs = ["", Keys.TAB]
        for value in inputs:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(3)
        # Find the actual error message from the website
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Account Number must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_02_verify_account_number(self):
        """Account number must be numeric"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        inputs = ["1234", "Acc123"]
        for value in inputs:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_03_verify_account_number(self):
        """Account number cannot have special character"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        inputs = ["123!@#", "!@#"]
        for value in inputs:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(2)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
            expected_error = "Special characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_04_verify_account_number(self):
        """First Character cannot be space"""
        driver = self.driver
        inputs = Keys.SPACE
        driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_submit_button(self):
        """Valid Account Number"""

        driver = self.driver
        account_number = 125195
        driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")

        account_number_input = driver.find_element(By.NAME, "accountno")
        account_number_input.clear()
        account_number_input.send_keys(account_number)

        # Click the submit button
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        # Find the table showing account balance

        try:
            account_balance_table = driver.find_element(
                By.XPATH, "//table[@id='balenquiry']/tbody"
            )
            self.assertTrue(
                account_balance_table.is_displayed(),
                "Account balance table should be displayed",
            )

        except NoSuchElementException:
            pass

    def test_06_verify_submit_button(self):
        """InValid Account Number"""
        driver = self.driver
        inputs = 12345
        driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        time.sleep(3)
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        error_alert = driver.switch_to.alert

        actual_error = error_alert.text

        error_alert.accept()
        expected_error = "Account does not exist"
        self.assertEqual(actual_error, expected_error)

    def test_07_reset_button(self):
        """Testing Reset Button"""
        driver = self.driver
        inputs = ["qwer", "123456"]
        driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        for value in inputs:
            driver.find_element(By.NAME, "accountno").send_keys(value)

        time.sleep(2)

        actual_output = driver.find_element("name", "accountno").text
        expected_output = ""
        self.assertEqual(actual_output, expected_output)


class MiniStatement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        time.sleep(3)
        cls.driver.find_element("name", "uid").send_keys("mngr517721")
        cls.driver.find_element("name", "password").send_keys("EtAjeha")
        cls.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_account_number(self):
        """Account number cannot be empty"""
        driver = self.driver
        inputs = ""
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = "Account Number must not be blank"
        expected_error = "Account Number must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_02_verify_account_number(self):
        """Account number must be numeric"""
        driver = self.driver
        inputs = ["1234", "Acc123"]
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
        for value in inputs:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_03_verify_account_number(self):
        """Account number cannot have special character"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
        inputs = ["123!@#", "!@#"]
        for value in inputs:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Special characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_04_verify_account_number(self):
        """Account number cannot have blank space"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
        inputs = "123 12"
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_account_number(self):
        """First Character cannot be space"""
        driver = self.driver
        inputs = Keys.SPACE
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_06_submit_button(self):
        """Valid Account Number"""
        driver = self.driver
        account_number = 125195
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
        account_number_input = driver.find_element(By.NAME, "accountno")
        account_number_input.clear()
        account_number_input.send_keys(account_number)
        # Click the submit button
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        time.sleep(3)

        actual_url = driver.current_url
        expected_url = "https://demo.guru99.com/V4/manager/MiniStatement.php"
        self.assertEqual(actual_url, expected_url)

    def test_07_submit_button(self):
        """InValid Account Number"""
        driver = self.driver
        inputs = 12345
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        time.sleep(3)
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        actual_error = "Account does not exist"
        expected_error = "Account does not exist"
        self.assertEqual(actual_error, expected_error)

    def test_08_reset_button(self):
        """Testing Reset Button"""
        driver = self.driver
        inputs = ["qwer", "123456"]
        driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")

        for value in inputs:
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(1)
            driver.find_element(By.XPATH, "//input[@type='reset']").click()
            time.sleep(1)

        actual_output = driver.find_element(By.NAME, "accountno").text
        expected_output = ""
        self.assertEqual(actual_output, expected_output)


class CustomizedStatement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        time.sleep(3)
        cls.driver.find_element("name", "uid").send_keys("mngr517721")
        cls.driver.find_element("name", "password").send_keys("EtAjeha")
        cls.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_account_number(self):
        """Account number cannot be empty"""
        driver = self.driver
        inputs = ""
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        time.sleep(3)
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Account Number must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_02_verify_account_number(self):
        """Account number must be numeric"""
        driver = self.driver
        inputs = ["1234", "Acc123"]
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        for value in inputs:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_03_verify_account_number(self):
        """Account number cannot have special character"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        inputs = ["123!@#", "!@#"]
        for value in inputs:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Special characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_04_verify_account_number(self):
        """Account number cannot have blank space"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        inputs = "123 12"
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_account_number(self):
        """First Character cannot be space"""
        driver = self.driver
        inputs = Keys.SPACE
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(inputs)
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_06_verify_from_date_field(self):
        """click on the date field"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").clear()
        driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message26']").text
        expected_error = "From Date Field must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_07_verify_from_date_field(self):
        """click on the date field"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]").clear()
        driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]").click()
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message27']").text
        expected_error = "To Date Field must not be blank"
        self.assertEqual(actual_error, expected_error)

    def test_08_verify_minimum_transaction_value(self):
        """Minimum Transaction Value must be numeric"""
        driver = self.driver
        inputs = ["1234", "Acc123"]
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        for value in inputs:
            driver.find_element(By.NAME, "amountlowerlimit").clear()
            driver.find_element(By.NAME, "amountlowerlimit").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message12']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_09_verify_minimum_transaction_value(self):
        """Account number cannot have special character"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        inputs = ["123!@#", "!@#"]
        for value in inputs:
            driver.find_element(By.NAME, "amountlowerlimit").clear()
            driver.find_element(By.NAME, "amountlowerlimit").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message12']").text
        expected_error = "Special characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_10_verify_minimum_transaction_value(self):
        """Account number cannot have blank space"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        inputs = "123 12"
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(inputs)
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message12']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_11_verify_minimum_transaction_value(self):
        """First Character cannot be space"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.SPACE, Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message12']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_12_verify_number_of_transaction(self):
        """Number of transaction must be numeric"""
        driver = self.driver
        inputs = ["1234", "Acc123"]
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        for value in inputs:
            driver.find_element(By.NAME, "numtransaction").clear()
            driver.find_element(By.NAME, "numtransaction").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message13']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_13_verify_number_of_transaction(self):
        """Number of transaction cannot have special character"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        inputs = ["123!@#", "!@#"]
        for value in inputs:
            driver.find_element(By.NAME, "numtransaction").clear()
            driver.find_element(By.NAME, "numtransaction").send_keys(value)
            time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message13']").text
        expected_error = "Special characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_14_verify_number_of_transaction(self):
        """Number of transaction cannot have blank space"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        inputs = "123 12"
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys(inputs)
        driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message13']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_15_verify_number_of_transaction(self):
        """First Character cannot be space"""
        driver = self.driver
        inputs = Keys.SPACE
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys(inputs)
        driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
        time.sleep(3)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message13']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_16_reset_button(self):
        """Testing Reset Button"""
        driver = self.driver
        inputs = [105516, 5454, 123456]
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")
        # account number
        driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]").clear()
        driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]").send_keys(
            inputs[0]
        )
        # from date
        driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").clear()
        driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").click()
        # To date
        driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]").clear()
        driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]").click()
        # minimum transaction value
        driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]").clear()
        driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]").send_keys(
            inputs[1]
        )
        # number of transaction
        driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]").clear()
        driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]").send_keys(
            inputs[2]
        )
        time.sleep(3)
        # reset button
        driver.find_element(By.XPATH, "//tbody/tr[13]/td[2]/input[2]").click()

    def test_17_submit_button(self):
        "Testing Submit Button"
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")

        driver.find_element("name", "fdate").click()

        driver.find_element("name", "fdate").send_keys("5")
        driver.find_element("name", "fdate").send_keys("20", Keys.TAB)
        driver.find_element("name", "fdate").send_keys("30", Keys.TAB)

        driver.find_element("name", "tdate").send_keys(Keys.TAB)

        driver.find_element("name", "amountlowerlimit").send_keys("12345")

        driver.find_element("name", "numtransaction").send_keys("123")

        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        time.sleep(3)

        WebDriverWait(driver, 5).until(EC.alert_is_present())
        error_alert = driver.switch_to.alert

        actual_error = error_alert.text
        expected_error = "Please fill all fields"
        self.assertEqual(actual_error, expected_error)

        error_alert.accept()


if __name__ == "__main__":
    unittest.main()
