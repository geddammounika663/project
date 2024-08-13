# features/steps/web_steps.py

from behave import when
from selenium.webdriver.common.by import By

@when('I click the "{button_name}" button')
def step_click_button(context, button_name):
    button = context.driver.find_element(By.XPATH, f"//button[text()='{button_name}']")
    button.click()
