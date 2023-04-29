from selenium.webdriver.common.by import By

from ui.Tab import TabLocators, TabPlaceholders, Tab

class LoginLocators:
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    RECOVERY_LINK = (By.ID, "forgot_password")
    REGISTER_LINK = (By.ID, "kc-register")
    USERNAME_PLACEHOLDER = (By.CLASS_NAME, "rt-input__placeholder")
    SUBMIT_BUTTON = (By.ID, "kc-login")
    ERROR_MESSAGE = (By.ID, "form-error-message")
    INPUT_TEXT = (By.NAME, "username")
    TEMP_CODE_BUTTON = (By.NAME, "back_to_otp_btn")


class LoginForm:
    def __init__(self, selenium, attributes):
        self.attributes = attributes
        self.selenium = selenium
        self.username_field = selenium.find_element(*LoginLocators.USERNAME_FIELD)
        self.password_field = selenium.find_element(*LoginLocators.PASSWORD_FIELD)

        self.recovery_link = selenium.find_element(*LoginLocators.RECOVERY_LINK)
        self.register_link = selenium.find_element(*LoginLocators.REGISTER_LINK)
        self.username_placeholder = selenium.find_element(*LoginLocators.USERNAME_PLACEHOLDER)
        self.submit_button = selenium.find_element(*LoginLocators.SUBMIT_BUTTON)


        self.tabs = {i: Tab(selenium, i) for i in [TabLocators.NUMBER_TAB, TabLocators.EMAIL_TAB, TabLocators.LOGIN_TAB]}
        if attributes.auth_attr.ls == 1:
            self.tabs[TabLocators.PERSONAL_ACCOUNT_TAB] = Tab(selenium, TabLocators.PERSONAL_ACCOUNT_TAB)
        self.initial_tab = self.tabs[TabLocators.NUMBER_TAB]
        self.input_text = selenium.find_element(*LoginLocators.INPUT_TEXT)

    def getActiveTab(self):
        for key, val in self.tabs.items():
            if val.isActive():
                return val
        return None
    
    def getUsernamePlaceholder(self):
        return self.username_placeholder.text