from selenium.webdriver.common.by import By
from ui.LoginForm import TabLocators, TabPlaceholders
from ui.Tab import TabLocators, TabPlaceholders, Tab


class RecoverLocators:
    USERNAME_FIELD = (By.ID, "username")
    CONTINUE_BUTTON = (By.ID, "reset")
    BACK_BUTTON = (By.ID, "reset-back")


class RecoverForm:
    def __init__(self, selenium, attributes):
        self.selenium = selenium
        self.attributes = attributes
        self.username_field = selenium.find_element(*RecoverLocators.USERNAME_FIELD)
        self.continue_button = selenium.find_element(*RecoverLocators.CONTINUE_BUTTON)
        self.back_button = selenium.find_element(*RecoverLocators.BACK_BUTTON)

        self.tabs = {i: Tab(selenium, i) for i in
                     [TabLocators.NUMBER_TAB, TabLocators.EMAIL_TAB, TabLocators.LOGIN_TAB]}
        if attributes.auth_attr.ls == 1:
            self.tabs[TabLocators.PERSONAL_ACCOUNT_TAB] = Tab(selenium, TabLocators.PERSONAL_ACCOUNT_TAB)
        self.initial_tab = self.tabs[TabLocators.NUMBER_TAB]

    def getActiveTab(self):
        for key, val in self.tabs.items():
            if val.isActive():
                return val
        return None


class InputRecoverLocators:
    BACK_BUTTON = (By.NAME, "cancel_reset")
    INPUT_FIELDS = (By.XPATH, '//div[@class="code-input-container"]/div/div/div')
    MESSAGE = (By.CLASS_NAME, "card-container__desc")


class InputRecoverForm:
    def __init__(self, selenium):
        self.selenium = selenium
        self.back_button = selenium.find_element(*InputRecoverLocators.BACK_BUTTON)
        self.input_fields = selenium.find_elements(*InputRecoverLocators.INPUT_FIELDS)
        self.message = selenium.find_element(*InputRecoverLocators.MESSAGE)


class PasswordRecoverLocators:
    PASSWORD = (By.CLASS_NAME, "new-password-container__password")
    PASSWORD_REPEAT = (By.CLASS_NAME, "new-password-container__confirmed-password")
    SUBMIT = (By.ID, "t-btn-reset-pass")


class PasswordRecoverForm:
    def __init__(self, selenium):
        self.selenium = selenium
        self.password = selenium.find_element(*PasswordRecoverLocators.PASSWORD)
        self.password_repeat = selenium.find_element(*PasswordRecoverLocators.PASSWORD_REPEAT)
        self.submit = selenium.find_element(*PasswordRecoverLocators.SUBMIT)


def is_choose(selenium):
    return len(selenium.find_elements(By.CLASS_NAME, "reset-form-choice-container")) != 0


class ChooseRecoverLocators:
    OPTIONS = (By.XPATH, '//*[@class="rt-radio-group reset-choice-form__radio-group"]/label')
    SUBMIT = (By.CLASS_NAME, "reset-choice-form__reset-btn")
    BACK = (By.CLASS_NAME, "reset-choice-form__back-btn")


class ChooseRecoverForm:
    def __init__(self, selenium):
        self.selenium = selenium
        self.options = selenium.find_elements(*ChooseRecoverLocators.OPTIONS)
        self.submit = selenium.find_element(*ChooseRecoverLocators.SUBMIT)
        self.back = selenium.find_element(*ChooseRecoverLocators.BACK)
