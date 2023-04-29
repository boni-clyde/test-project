import pytest
from settings import *
from ui.RecoverForm import *
from general import fill_capcha
from test_temp_code import  wait_for_code

"""
Recovery-1-Number
Recovery-1-Mail
"""


@pytest.mark.positive
@pytest.mark.parametrize("tab, username, password", [(TabLocators.NUMBER_TAB, CORRECT_NUMBER, "12345aBC"),
                                                (TabLocators.EMAIL_TAB, CORRECT_EMAIL, "12345aBC")])
def test_correct_recovery(recover_view: RecoverForm, tab, username, password):
    recover_view.tabs[tab].click()
    recover_view.username_field.send_keys(username)
    fill_capcha(recover_view.selenium)
    recover_view.continue_button.click()

    if is_choose(recover_view.selenium):
        recover_view = ChooseRecoverForm(recover_view.selenium)
        if tab == TabLocators.NUMBER_TAB:
            recover_view.options[0].click()
        else:
            recover_view.options[1].click()
        recover_view.submit.click()
    assert len(recover_view.selenium.find_elements(By.ID, "form-error-message")) == 0
    view = InputRecoverForm(recover_view.selenium)
    url = view.selenium.current_url
    wait_for_code(view.selenium)
    assert url != view.selenium.current_url and len(view.selenium.find_elements(By.CLASS_NAME, "code-input-container__error")) == 0
    view = PasswordRecoverForm(view.selenium)
    view.password.send_keys(password)
    view.password_repeat.send_keys(password)
    url = view.selenium.current_url
    view.submit.click()
    assert url != view.selenium.current_url and len(view.selenium.find_elements(By.ID, "form-error-message")) == 0

