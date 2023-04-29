from selenium.webdriver.common.by import By
from ui.TemporaryCodeForm import TemporaryCodeForm, InputTemporaryCodeForm
from general import fill_capcha
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from settings import *
from selenium.webdriver.support import expected_conditions as EC


def wait_for_timeout(selenium):
    WebDriverWait(selenium, 130).until(lambda driver : len(driver.find_elements(By.CLASS_NAME, "otp-form__timeout")) == 0)

def wait_for_code(selenium):
    url = selenium.current_url
    WebDriverWait(selenium, 100).until(
        lambda driver: (
            (driver.current_url != url) or len(driver.find_elements(By.CLASS_NAME, "code-input-container__error")) != 0 
        )
    )
"""
TEMP-CODE-1-NUMBER
"""
@pytest.mark.positive
@pytest.mark.parametrize("input,id", [(CORRECT_NUMBER, "number"), (CORRECT_EMAIL, "email")])
def test_correct_temp_code(temp_code_view, attributes, input, id):
    if id == "number" and attributes.auth_attr.temp_number == 0 or id == "email" and attributes.auth_attr.temp_email == 0:
        pytest.skip("Test is not supported by test object")
    wait_for_timeout(temp_code_view.selenium)
    temp_code_view.input_field.send_keys(input)
    fill_capcha(temp_code_view.selenium)
    temp_code_view.submit_button.click()
    WebDriverWait(temp_code_view.selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    view = InputTemporaryCodeForm(temp_code_view.selenium)
    url = view.selenium.current_url
    wait_for_code(view.selenium)
    
    assert url != view.selenium.current_url
    assert len(view.selenium.find_elements(By.ID, "app-container")) == 0
    # assert logged


"""
TEMP-CODE-2
"""   
@pytest.mark.parametrize("number1, number2", [("+71112223344", "+72223334455")])
@pytest.mark.positive
def test_change_number(temp_code_view, number1, number2, attributes):
    if attributes.auth_attr.temp_number == 0:
        pytest.skip("Test is not supported by test object")
    wait_for_timeout(temp_code_view.selenium)
    fill_capcha(temp_code_view.selenium)
    temp_code_view.input_field.send_keys(number1)
    temp_code_view.submit_button.click()
    WebDriverWait(temp_code_view.selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    temp_view = InputTemporaryCodeForm(temp_code_view.selenium)
    assert ''.join([i for i in temp_view.message.text if i.isdigit()][1:]) == ''.join([i for i in number1 if i.isdigit()])[1:]
    temp_view.back_button.click()
    wait_for_timeout(temp_code_view.selenium)
    temp_view = TemporaryCodeForm(temp_view.selenium, attributes)
    temp_view.input_field.send_keys(number2)
    temp_view.submit_button.click()
    WebDriverWait(temp_code_view.selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    temp_view = InputTemporaryCodeForm(temp_view.selenium)
    assert ''.join([i for i in temp_view.message.text if i.isdigit()][1:]) == ''.join([i for i in number2 if i.isdigit()])[1:]
    


"""
TEMP-CODE-3
"""
@pytest.mark.parametrize("number", ["+71112223344"])
@pytest.mark.positive
def test_auto_switch(temp_code_view, number, attributes):
    if attributes.auth_attr.temp_number == 0:
        pytest.skip("Test is not supported by test object")
    wait_for_timeout(temp_code_view.selenium)
    temp_code_view.input_field.send_keys(number)
    fill_capcha(temp_code_view.selenium)
    temp_code_view.submit_button.click()
    view = InputTemporaryCodeForm(temp_code_view.selenium)
    view.input_fields[0].click()
    for i in range(0, 5):
        view.selenium.switch_to.active_element.send_keys("1")
        assert view.selenium.switch_to.active_element == view.input_fields[i + 1]
    url = view.selenium.current_url
    view.selenium.switch_to.active_element.send_keys("1")
    assert url != view.selenium.current_url or len(view.selenium.find_elements(By.CLASS_NAME, "code-input-container__error")) != 0
