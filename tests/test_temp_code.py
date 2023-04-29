from selenium.webdriver.common.by import By
from ui.TemporaryCodeForm import TemporaryCodeForm, InputTemporatyCodeForm
from general import fill_capcha
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from settings import *
from selenium.webdriver.support import expected_conditions as EC


"""
TEMP-CODE-1-NUMBER
"""
@pytest.mark.skip
@pytest.mark.positive
@pytest.mark.parametrize("input,id", [(CORRECT_NUMBER, "number"), (CORRECT_EMAIL, "email")])
def test_correct_temp_code(temp_code_view, attributes, input, id):
    if id == "number" and attributes.auth_attr.temp_number == 0 or id == "email" and attributes.auth_attr.temp_email == 0:
        pytest.skip("Test is not supported by test object")
    WebDriverWait(temp_code_view.selenium, 130).until(lambda driver : len(driver.find_elements(By.CLASS_NAME, "otp-form__timeout")) == 0)
    temp_code_view.input_field.send_keys(input)
    fill_capcha(temp_code_view.selenium)
    temp_code_view.submit_button.click()
    WebDriverWait(temp_code_view.selenium, 10).until(EC.presence_of_element_located((By.ID, "app-container")))
    view = InputTemporatyCodeForm(temp_code_view.selenium)
    url = view.selenium.current_url
    #wait_for_code_input(view.selenium)
    #open('bf', 'w').write(str(len(view.input_fields)))
    WebDriverWait(view.selenium, 100).until(
        lambda driver: ((driver.current_url != url) or all([(view.input_fields[i].text() != '') for i in range(6)])))
    assert url != view.selenium.current_url
    # assert logged


"""
TEMP-CODE-2
"""   
@pytest.mark.skip
@pytest.mark.parametrize("number1, number2", [("81112223344", "82223334455")])
@pytest.mark.positive
def test_change_number(temp_code_view, input, number1, number2, attributes):
    if attributes.auth_attr.temp_number == 0:
        pytest.skip("Test is not supported by test object")
    temp_code_view.input_field.send_keys(input)
    fill_capcha(temp_code_view.selenium)
    temp_code_view.input_field.send_keys(number1)
    temp_code_view.submit_button.click()
    view = InputTemporatyCodeForm(temp_code_view.selenium)
    assert ''.join([i for i in view.message.text() if i.isDigit()][1:]) == number1[1:]
    view.back_buttom.click()
    view = TemporaryCodeForm(view.selenium)
    view.input_field.send_keys(number2)
    view.submit_button.click()
    view = InputTemporatyCodeForm(view.selenium)
    assert ''.join([i for i in view.message.text() if i.isDigit()][1:]) == number2[1:]
    


"""
TEMP-CODE-3
"""
@pytest.mark.skip
@pytest.mark.parametrize("number", ["81112223344"])
@pytest.mark.positive
def test_auto_switch(temp_code_view, number, attributes):
    if attributes.auth_attr.temp_number == 0:
        pytest.skip("Test is not supported by test object")
    temp_code_view.input_field.send_keys(number)
    fill_capcha(temp_code_view.selenium)
    temp_code_view.submit_button.click()
    view = InputTemporatyCodeForm(temp_code_view.selenium)
    view.input_fields[0].click()
    for i in range(0, 5):
        view.selenium.switch_to.active_element.send_keys("1")
        assert view.selenium.switch_to.active_element == view.input_fields[i + 1]
    url = view.selenium.current_url
    view.selenium.switch_to.active_element.send_keys("1")
    assert url != view.selenium.current_url
