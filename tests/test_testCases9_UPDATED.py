# Test Automation of Banking Project 
# Muhammad Anwar/100759431 
# Tolihat Gbabebo/100881446
# Mark Mekhail/ 
# INFT1207-02 Software Testing & Automatn
# Fabian Mauricio Narvaez Goyes
# August 1, 2023
# This assignment is to create a program that will open a link to a banking site and  run test on several options for customers, accounts, balances, and statements.

# import the selenium web driver 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

# import time 
import time 

# Create class 
class NewAccount(unittest.TestCase):
    # Class method
    @classmethod    
    def setUpClass(cls):
        # open the browser
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        # Include a try & except for browser
        cls.driver.get("https://demo.guru99.com/V4/") # link 
        # click on userID
        cls.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys('mngr517721')
        # password 
        cls.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").send_keys('EtAjeha')
        # click on login 
        cls.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_name(self):
        """Test 01: Blank field."""""
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
            actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
            expected_error = "Characters are not allowed"
            self.assertEqual(actual_error, expected_error)

    def test_03_verify_name(self):
        """Test 03: Using Special Characters in name field."""
        
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        inputs = ["123!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "cusid").clear()
            driver.find_element("name", "cusid").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
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

        driver.find_element(By.NAME, "inideposit").send_keys(Keys.SPACE)

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
            actual_error = driver.find_element(By.XPATH, "//label[@id='message19']").text
            expected_error = "Characters are not allowed"
            self.assertEqual(expected_error, actual_error)


    def test_08_verify_initial_deposit(self):
        """Test 09: Using Special Characters."""
        
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        inputs = ["123!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "inideposit").clear()
            driver.find_element("name", "inideposit").send_keys(value)
            actual_error = driver.find_element(By.XPATH, "//label[@id='message19']").text
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
        """Test 10: Using space as First Character in initial deposit."""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "inideposit").send_keys(Keys.SPACE)
        
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
        """Test 13: Entering any values in Customer ID and initial deposit fields. """
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("qwer")
        driver.find_element("name", "inideposit").send_keys("123456")

        driver.find_element(By.XPATH, "//input[@type='reset']").click()

        driver.find_element("name", "cusid").click()
        time.sleep(2)

        actual_error = driver.find_element(By.XPATH, "//label[@id='message14']").text
        expected_error =  "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)



    def test_14_submit_button(self):
        """Test 14: Entering incorrect Customer ID. """
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
        """Test 15: Entering correct Customer ID. """
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element("name", "inideposit").send_keys("1235")
        
        driver.find_element(By.XPATH, "//tbody/tr[5]/td[2]/input[1]").click()

        actual_text = driver.find_element(By.XPATH, "//p[contains(text(),'Account Generated Successfully!!!')]").text
        expected_text = "Account Generated Successfully!!!"
        
        self.assertEqual(expected_text, actual_text)


    def test_16_continue_hyperlink(self):
        """Test 16: Continuing after generating a new account. """
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

        driver.find_element("name", "cusid").send_keys("78138")
        driver.find_element("name", "inideposit").send_keys("1235")
        
        driver.find_element(By.XPATH, "//tbody/tr[5]/td[2]/input[1]").click()
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        time.sleep(4)

class EditAccount(unittest.TestCase):
# Class method
    @classmethod    
    def setUpClass(cls):
        # open the browser
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        # Include a try & except for browser
        cls.driver.get("https://demo.guru99.com/V4/") # link 
        # click on userID
        cls.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys('mngr517721')
        # password 
        cls.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").send_keys('EtAjeha')
        # click on login 
        cls.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_name(self):
        """Test 01: Blank field."""""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")
        driver.find_element("name", "accountno").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Account Number must not be blank"
        self.assertEqual(expected_error, actual_error)

    def test_02_verify_name(self):
        """Test 02: Using numbers."""
        
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        inputs = ["name123"]

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

        inputs = ["name!@#", "!@#"]

        for value in inputs:
            driver.find_element("name", "accountno").clear()
            driver.find_element("name", "accountno").send_keys(value)
        
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Special Characters not allowed"
        self.assertEqual(actual_error, expected_error)


    def test_04_verify_name(self):
        """Test 04: Using space as characters in name field."""
        
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        driver.find_element("name", "accountno").send_keys(Keys.SPACE)
        
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_valid_account(self):
        """Test 05: Valid Account Number"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        valid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)

        # Click Submit
        driver.find_element(By.NAME, "AccSubmit").click()

        # Handle alert
        WebDriverWait(driver, 10).until(Alert(driver).is_present())
        alert = Alert(driver)
        alert_text = alert.text
        expected_alert_text = "demo.guru99.com says Account does not exist"
        self.assertEqual(expected_alert_text, alert_text)
        alert.accept()

        # Verify if the page has loaded successfully
        page_title = driver.title
        expected_title = "Guru99 Bank Edit Account Entry Page"
        self.assertEqual(expected_title, page_title)

    def test_06_verify_invalid_account(self):
        """Test 06: Invalid Account Number"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        invalid_account_numbers = ["abc", "123 456"]

        for value in invalid_account_numbers:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)

            # Click Submit
            driver.find_element(By.NAME, "AccSubmit").click()

            # Handle alert
            WebDriverWait(driver, 10).until(Alert(driver).is_present())
            alert = Alert(driver)
            alert_text = alert.text
            expected_alert_text = "Please fill all fields"
            self.assertEqual(expected_alert_text, alert_text)
            alert.accept()

            # Verify error message
            actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
            expected_error = "Characters are not allowed"
            self.assertEqual(expected_error, actual_error)

    def test_07_verify_successful_account_edit(self):
        """Test 07: Successful Account Edit"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        valid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)

        # Click Submit
        driver.find_element(By.NAME, "AccSubmit").click()

        # Edit Account Type
        account_type_dropdown = driver.find_element(By.NAME, "a_type").click()
        account_type_dropdown.select_by_visible_text("Savings")

        # Click Submit
        driver.find_element(By.NAME, "AccSubmit").click()

        # Verify success message
        success_message = driver.find_element(By.XPATH, "//p[text()='Account details updated Successfully!!!']").text
        expected_success_message = "Account details updated Successfully!!!"
        self.assertEqual(expected_success_message, success_message)

    def test_08_verify_cancel_account_edit(self):
        """Test 08: Cancel Account Edit"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

        valid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)

        # Click Submit
        driver.find_element(By.NAME, "AccSubmit").click()

        # Click Reset
        driver.find_element(By.NAME, "res").click()

        # Verify that fields are reset
        account_type_value = driver.find_element(By.NAME, "a_type").get_attribute("value")
        self.assertEqual("", account_type_value)


class DeleteAccount(unittest.TestCase):
# Class method
    @classmethod    
    def setUpClass(cls):
        # open the browser
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        # Include a try & except for browser
        cls.driver.get("https://demo.guru99.com/V4/") # link 
        # click on userID
        cls.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys('mngr517721')
        # password 
        cls.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]").send_keys('EtAjeha')
        # click on login 
        cls.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_verify_name(self):
        """Test 01: Blank field."""""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        driver.find_element("name", "accountno").send_keys(Keys.TAB)
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Account Number must not be blank"
        self.assertEqual(expected_error, actual_error)

    def test_02_verify_name(self):
        """Test 02: Using numbers."""
        
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        inputs = ["1357", "name123"]

        for value in inputs:
            driver.find_element("name", "accountno").clear()
            driver.find_element("name", "accountno").send_keys(value)
        
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_03_verify_name(self):
        """Test 03: Using Special Characters in name field."""
        
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
        """Test 04: Using space as First Character in name field."""
        
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        driver.find_element("name", "accountno").send_keys(Keys.SPACE)
        
        actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
        expected_error = "Characters are not allowed"
        self.assertEqual(actual_error, expected_error)

    def test_05_verify_valid_account(self):
        """Test 05: Valid Account Number"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        valid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)

        # Click Submit
        driver.find_element(By.NAME, "AccSubmit").click()

        # Handle alert
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert_text = alert.text
        expected_alert_text = "Do you really want to delete this Account?"
        self.assertEqual(expected_alert_text, alert_text)
        alert.accept()

        # Verify if the page has loaded successfully
        page_title = driver.title
        expected_title = "Guru99 Bank Delete Account Entry Page"
        self.assertEqual(expected_title, page_title)

    def test_06_verify_invalid_account(self):
        """Test 06: Invalid Account Number"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        invalid_account_numbers = ["abc","123 456"]

        for value in invalid_account_numbers:
            driver.find_element(By.NAME, "accountno").clear()
            driver.find_element(By.NAME, "accountno").send_keys(value)

            # Click Submit
            driver.find_element(By.NAME, "AccSubmit").click()

            # Verify error message
            actual_error = driver.find_element(By.XPATH, "//label[@id='message2']").text
            expected_error = "Please fill all fields"
            self.assertEqual(expected_error, actual_error)

    def test_07_verify_successful_account_delete(self):
        """Test 07: Successful Account Delete"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        valid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)

        # Click Submit
        driver.find_element(By.NAME, "AccSubmit").click()

        # Handle alert
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()

        # Verify success message
        success_message = driver.find_element(By.XPATH, "//p[text()='Account Deleted Sucessfully!!!']").text
        expected_success_message = "Account Deleted Sucessfully!!!"
        self.assertEqual(expected_success_message, success_message)

    def test_08_verify_cancel_account_delete(self):
        """Test 08: Cancel Account Delete"""
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

        valid_account_number = "12345"
        driver.find_element(By.NAME, "accountno").send_keys(valid_account_number)

        # Click Reset
        driver.find_element(By.NAME, "res").click()

        # Verify that fields are reset
        account_number_value = driver.find_element(By.NAME, "accountno").get_attribute("value")
        self.assertEqual("", account_number_value)