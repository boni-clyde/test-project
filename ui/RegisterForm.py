from selenium.webdriver.common.by import By


class RegisterLocators:
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    REGION = (By.CLASS_NAME, "register-form__dropdown")
    USERNAME = (By.ID, "address")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRM = (By.ID, "password-confirm")
    SUBMIT = (By.NAME, "register")

class RegisterForm:
    def __init__(self, selenium, attributes):
        self.selenium = selenium
        self.attributes = attributes
        self.first_name = selenium.find_element(*RegisterLocators.FIRST_NAME)
        self.last_name = selenium.find_element(*RegisterLocators.LAST_NAME)
        self.region = selenium.find_element(*RegisterLocators.REGION)
        self.username = selenium.find_element(*RegisterLocators.USERNAME)
        self.password = selenium.find_element(*RegisterLocators.PASSWORD)
        self.password_confirm = selenium.find_element(*RegisterLocators.PASSWORD_CONFIRM)
        self.submit_button = selenium.find_element(*RegisterLocators.SUBMIT)

class InputRegisterLocators:
    BACK_BUTTON = (By.NAME, "otp_back_phone")
    INPUT_FIELDS = (By.XPATH, '//div[@class="code-input-container"]/div/div/div')
    MESSAGE = (By.CLASS_NAME, "register-confirm-form-container__desc")


class InputRegisterForm:
    def __init__(self, selenium):
        self.selenium = selenium
        self.back_button = selenium.find_element(*InputRegisterLocators.BACK_BUTTON)
        self.input_fields = selenium.find_elements(*InputRegisterLocators.INPUT_FIELDS)
        self.message = selenium.find_element(*InputRegisterLocators.MESSAGE)

