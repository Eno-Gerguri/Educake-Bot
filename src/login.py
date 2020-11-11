from web_bot_helper_functions import wait_for_element_to_appear
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome

def login(browser: Chrome, username: str, password: str) -> None:
    student_login_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='/html/body/div[2]/div[1]/div/div/div[2]/a[2]')
    student_login_button.click()

    username_input_field: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.ID, value_to_find_element='username')
    username_input_field.send_keys(username)

    password_input_field: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.ID, value_to_find_element='password')
    password_input_field.send_keys(password)

    sign_in_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.ID, value_to_find_element='loginSubmit')
    sign_in_button.click()
