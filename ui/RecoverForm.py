from selenium.webdriver.common.by import By
from ui.LoginForm import TabLocators, TabPlaceholders
from ui.Tab import TabLocators, TabPlaceholders, Tab

class RecoverLocators:
    USERNAME_FIELD = (By.ID, "username")
    CONTINUE_BUTTON = (By.ID, "reset")
    BACK_BUTTON = (By.ID, "reset-back")

class RecoverForm:
    def __init__(self, selenium):
        self.selenium = selenium
        self.username_field = selenium.find_element(*RecoverLocators.USERNAME_FIELD)
        self.continue_button = selenium.find_element(*RecoverLocators.CONTINUE_BUTTON)
        self.back_button = selenium.find_element(*RecoverLocators.BACK_BUTTON)

        self.tabs = {i: Tab(selenium, i) for i in [TabLocators.NUMBER_TAB, TabLocators.EMAIL_TAB, TabLocators.LOGIN_TAB, TabLocators.PERSONAL_ACCOUNT_TAB]}
        self.initial_tab = self.tabs[TabLocators.NUMBER_TAB]
        
