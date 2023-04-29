import uuid
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.TemporaryCodeForm import TemporaryCodeForm
from ui.LoginForm import LoginForm
from enum import Enum
from ui.RedisterForm import RegisterForm
from tests.attributes import *

def pytest_addoption(parser):
    parser.addoption(
        "--test_object",
        action="store",
        help="ELK : ЕЛК Web\nONLINE: Онлайм Web\nSTART : Старт Web\nSMART : Умный дом Web\nKEY : Ключ Web",
        choices=('ELK', 'ONLINE', 'START', 'SMART', 'KEY')
    )


@pytest.fixture
def web_browser(request, selenium, attributes):
    browser = selenium
    browser.get(attributes.link)
    WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    
    yield browser

@pytest.fixture
def attributes(pytestconfig):
    testObject =  testObjectMapper[pytestconfig.getoption("test_object")]
    yield testObject

@pytest.fixture
def temp_code_view(web_browser, attributes):
    yield TemporaryCodeForm(web_browser, attributes)

@pytest.fixture
def login_view(temp_code_view, attributes):
    temp_code_view.login_button.click()
    WebDriverWait(temp_code_view.selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    
    yield LoginForm(temp_code_view.selenium, attributes)

@pytest.fixture
def register_view(login_page, attributes):
    login_page.register_link.click()
    yield RegisterForm(login_page.selenium, attributes)
