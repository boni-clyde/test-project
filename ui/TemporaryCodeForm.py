from selenium.webdriver.common.by import By

class TemporaryCodeLocators:
    INPUT_FIELD = (By.ID, "address")
    SUBMIT_BUTTON = (By.ID, "otp_get_code")
    TO_LOGIN_BUTTON = (By.ID, "standard_auth_btn")

class TemporaryCodeForm:
    def __init__(self, selenium, attributes):
        self.attributes = attributes
        self.selenium = selenium
        self.input_field = selenium.find_element(*TemporaryCodeLocators.INPUT_FIELD)
        self.submit_button = selenium.find_element(*TemporaryCodeLocators.SUBMIT_BUTTON)
        self.login_button = selenium.find_element(*TemporaryCodeLocators.TO_LOGIN_BUTTON)
    
class InputTemporaryCodeLocators:
    DESCRIPTION = (By.CLASS_NAME, "otp-code-form-container__desc")
    BACK_BUTTON = (By.NAME, "otp_back_phone")
    INPUT_FIELDS = (By.XPATH, '//div[@class="code-input-container"]/div/div/div')
    MESSAGE = (By.CLASS_NAME, "otp-code-form-container__desc")


class InputTemporatyCodeForm:
    def __init__(self, selenium):
        self.selenium = selenium
        self.desc = selenium.find_element(*InputTemporaryCodeLocators.DESCRIPTION)
        self.back_buttom = selenium.find_element(*InputTemporaryCodeLocators.BACK_BUTTON)
        self.input_fields = selenium.find_elements(*InputTemporaryCodeLocators.INPUT_FIELDS)
        self.message = selenium.find_element(*InputTemporaryCodeLocators.MESSAGE)

