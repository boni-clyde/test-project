from selenium.webdriver.common.by import By


class TabLocators:
    EMAIL_TAB = (By.ID, "t-btn-tab-mail")
    LOGIN_TAB = (By.ID, "t-btn-tab-login")
    PERSONAL_ACCOUNT_TAB = (By.ID, "t-btn-tab-ls")
    NUMBER_TAB = (By.ID, "t-btn-tab-phone")

class TabPlaceholders:
    NUMBER = "Мобильный телефон"
    EMAIL = "Электронная почта"
    LOGIN = "Логин"
    PERSONAL_ACCOUNT = "Лицевой счёт"

    PLACEHOLDER_MAPPER = {
        TabLocators.EMAIL_TAB[1] : EMAIL,
        TabLocators.NUMBER_TAB[1] : NUMBER,
        TabLocators.PERSONAL_ACCOUNT_TAB[1] : PERSONAL_ACCOUNT, 
        TabLocators.LOGIN_TAB[1] : LOGIN
    }


class Tab:
    def __init__(self, selenium, id):
        self.id = id
        self.element = selenium.find_element(*id)
        self.name = self.element.text
        self.placeholder_text = TabPlaceholders.PLACEHOLDER_MAPPER[id[1]]

    def isActive(self):
        return "active" in self.element.get_attribute("class")
    
    def click(self):
        self.element.click()
        