from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Checks if page contains capcha and waits for user to fill it.
Change to empty function in real testing. Used only as workaround for capcha.
"""

class capcha_filled:
  def __init__(self, input_field, text_field):
    self.input_field = input_field
    self.text_field = text_field

  def __call__(self, driver):
    if len(self.text_field.get_attribute("innerText")) != 0 and self.input_field != driver.switch_to.active_element:
       return True
    return False
       
    
def fill_capcha(selenium):
    capcha = selenium.find_elements(By.ID, "captcha")   
    if len(capcha) != 1:
        return
    capcha = capcha[0]
    text_field = selenium.find_element(By.XPATH, "//*[@id='captcha']/..//*[@class='rt-input__mask-start']")
    WebDriverWait(selenium, 100).until(capcha_filled(capcha, text_field))   

