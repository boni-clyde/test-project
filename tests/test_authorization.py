from selenium.webdriver.common.by import By
from ui.LoginForm import LoginForm, TabLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import pytest
from selenium.webdriver.common.keys import Keys
from ui.LoginForm import LoginLocators
from tests.general import fill_capcha
from ui.Tab import TabLocators, TabPlaceholders
from settings import *

"""
Тест-кейс: Authorization-2
"""
@pytest.mark.positive
def test_switch_login_mode(login_view):
    assert login_view.getUsernamePlaceholder() == login_view.initial_tab.placeholder_text
    for i in list(login_view.tabs.values())[1:]:
        i.click()
        assert login_view.getUsernamePlaceholder() == i.placeholder_text
    list(login_view.tabs.values())[0].click()
    assert login_view.getUsernamePlaceholder() == login_view.initial_tab.placeholder_text
    


"""
Тест-кейс Authorization-3-Mail.
Тест-кейс Authorization-3-LS.
Тест-кейс Authorization-3-Number.
Тест-кейс Authorization-3-Login.
"""
@pytest.mark.positive
@pytest.mark.parametrize("value,expected", [("Bob", TabLocators.LOGIN_TAB), 
                                            ("89991112233", TabLocators.NUMBER_TAB), 
                                            ("123@mail.ru", TabLocators.EMAIL_TAB), 
                                            ("123456789012", TabLocators.PERSONAL_ACCOUNT_TAB)])
def test_auto_switch_mode(value, expected, login_view, attributes):
    if expected == TabLocators.PERSONAL_ACCOUNT_TAB and attributes.auth_attr.ls == 0:
        pytest.skip("Test is not supported by test object")
    for i in login_view.tabs.values():
        if i.id == TabLocators.NUMBER_TAB and expected == TabLocators.PERSONAL_ACCOUNT_TAB:
            # skipped because of input format
            continue
        if i.id == TabLocators.PERSONAL_ACCOUNT_TAB and attributes.auth_attr.ls == 0:
            continue # not supported by test_object
        i.click()
        login_view.username_field.send_keys(value)
        login_view.password_field.click() # unfocus username field
        login_view.username_field.click()
        while(len(login_view.input_text.get_attribute("value")) > 0):
            login_view.username_field.send_keys(Keys.BACK_SPACE)
        cur_tab = login_view.getActiveTab()
        assert cur_tab != None
        assert cur_tab.id == expected


"""
Тест-кейс: Authorization-1-Login
Тест-кейс: Authorization-1-Email
Тест-кейс: Authorization-1-Number
Тест-кейс: Authorization-1-LS
"""
@pytest.mark.positive
@pytest.mark.parametrize("tab,login,password", [
    (TabLocators.LOGIN_TAB, CORRECT_LOGIN, CORRECT_PASSWORD),
    (TabLocators.EMAIL_TAB, CORRECT_EMAIL, CORRECT_PASSWORD),
    (TabLocators.NUMBER_TAB, CORRECT_NUMBER, CORRECT_PASSWORD),
    (TabLocators.PERSONAL_ACCOUNT_TAB, CORRECT_LS, CORRECT_PASSWORD)
])
def test_correct_login(login_view, tab, login, password, attributes):
    if tab == TabLocators.PERSONAL_ACCOUNT_TAB and attributes.auth_attr.ls == 0:
        pytest.skip("Test is not supported by test object")
    login_view.tabs[tab].click()
    login_view.username_field.send_keys(login)
    login_view.password_field.send_keys(password)
    fill_capcha(login_view.selenium)
    login_view.submit_button.click()
    assert len(login_view.selenium.find_elements(By.ID, "app-container")) == 0
    #assert len(login_view.selenium.find_elements(By.XPATH, "//*[text()='Неверный логин или пароль']")) == 0 


"""
Тест-кейс: Authorization-4-Number
Тест-кейс: Authorization-4-Email
"""
@pytest.mark.negative
@pytest.mark.parametrize("tab,login,password", [
    (TabLocators.LOGIN_TAB, '1' * 1000, '異體字康熙字典體'),
    (TabLocators.EMAIL_TAB, '123@321.23@', '123 OR 1=1') # sql
])
def test_extremal_login(login_view, tab, login, password, attributes):
    if tab == TabLocators.PERSONAL_ACCOUNT_TAB and attributes.auth_attr.ls == 0:
        pytest.skip("Test is not supported by test object")
    login_view.tabs[tab].click()
    login_view.username_field.send_keys(login)
    login_view.password_field.send_keys(password)
    fill_capcha(login_view.selenium)
    login_view.submit_button.click()
    #assert len(login_view.selenium.find_elements(By.ID, "app-container")) == 0
    assert len(login_view.selenium.find_elements(By.XPATH, "//*[text()='Неверный логин или пароль']")) != 0
