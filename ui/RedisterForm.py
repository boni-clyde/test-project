from selenium.webdriver.common.by import By


class RegisterLocators:
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    REGION = (By.CLASS_NAME, "rt-select rt-select--search register-form__dropdown")
    USERNAME = (By.ID, "address")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRM = (By.ID, "password-confirm")

class RegisterForm:
    def __init__(self, selenium):
        self.selenium = selenium
        self.first_name = selenium.find_element(*RegisterLocators.FIRST_NAME)
        self.last_name = selenium.find_element(*RegisterLocators.LAST_NAME)
        self.region = selenium.find_element(*RegisterLocators.REGION)
        self.username = selenium.find_element(*RegisterLocators.USERNAME)
        self.password = selenium.find_element(*RegisterLocators.PASSWORD)
        self.password_confirm = selenium.find_element(*RegisterLocators.PASSWORD_CONFIRM)
    