import pytest
from settings import *
from test_temp_code import wait_for_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.RegisterForm import InputRegisterForm

"""
Registration-1-Number
Registration-1-Email
"""

@pytest.mark.positive
@pytest.mark.parametrize("name,lastname,username,id,password",
                         [('Полиграф', 'Шариков', REGISTRATION_NUMBER, 'number', '12345ABc'),
                          ('Полиграф', 'Шариков', REGISTRATION_EMAIL, 'email', '12345ABc')])
def test_correct_registration(register_view, name, lastname, username, id, password):
    if id == 'number' and register_view.attributes.reg_attr.number == 0:
        pytest.skip('Test is not supported by test object')
    if id == 'email' and register_view.attributes.reg_attr.email == 0:
        pytest.skip('Test is not supported by test object')
    register_view.first_name.send_keys(name)
    register_view.last_name.send_keys(lastname)
    register_view.username.send_keys(username)
    register_view.password.send_keys(password)
    register_view.password_confirm.send_keys(password)
    url = register_view.selenium.current_url
    register_view.submit_button.click()
    assert url != register_view.selenium.current_url
    WebDriverWait(register_view.selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    view = InputRegisterForm(register_view.selenium)
    url = view.selenium.current_url
    wait_for_code(view.selenium)
    assert url != view.selenium.current_url
    assert len(view.selenium.find_elements(By.ID, "app-container")) == 0


"""
Registration-2
"""

@pytest.mark.positive
@pytest.mark.parametrize("name,lastname,username,password", [('Иван', 'Иванов', "+71231232343", '12345ABc')])
def test_number_masked(register_view, name, lastname, username, password):
    if id == 'number' and register_view.attributes.reg_attr.number == 0:
        pytest.skip('Test is not supported by test object')
    register_view.first_name.send_keys(name)
    register_view.last_name.send_keys(lastname)
    register_view.username.send_keys(username)
    register_view.password.send_keys(password)
    register_view.password_confirm.send_keys(password)
    url = register_view.selenium.current_url
    register_view.submit_button.click()
    assert url != register_view.selenium.current_url
    WebDriverWait(register_view.selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    view = InputRegisterForm(register_view.selenium)
    assert '*' in view.message.text


"""
Registration-3
"""
@pytest.mark.negative
@pytest.mark.parametrize("name,lastname,username,password,reppassword",
                         [('И', '--', "123@321.23", '12345a', '12345678')])
def test_input_format(register_view, name, lastname, username, password, reppassword):
    if id == 'number' and register_view.attributes.reg_attr.number == 0:
        pytest.skip('Test is not supported by test object')
    register_view.first_name.send_keys(name)

    def count_errors():
        return len(register_view.selenium.find_elements(By.XPATH,
                                                        "//*[@class=\"rt-input-container__meta rt-input-container__meta--error\"]"))

    register_view.last_name.click()
    assert count_errors() == 1
    register_view.last_name.send_keys(lastname)
    register_view.username.click()
    assert count_errors() == 2
    register_view.username.send_keys(username)
    register_view.password.click()
    assert count_errors() == 3
    register_view.password.send_keys(password)
    register_view.password_confirm.click()
    assert count_errors() == 4
    register_view.password_confirm.send_keys(reppassword)
    url = register_view.selenium.current_url
    register_view.submit_button.click()
    assert count_errors() == 5
    assert url == register_view.selenium.current_url
