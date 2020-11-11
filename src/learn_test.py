import json
from random import choice

from web_bot_helper_functions import wait_for_element_to_appear, wait_for_elements_to_appear, find_type_of_question, get_numbers_from_string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome
from selenium.common.exceptions import StaleElementReferenceException


def learn_test(browser: Chrome) -> None:
    test_questions_and_answers: dict[str, str, ...] = {}

    number_of_questions_answered_element: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[1]/div[1]/div[1]/h3')
    number_of_questions: int = int(number_of_questions_answered_element.text.split(' of ')[1])  # The number of questions in this quiz
    
    for i in range(number_of_questions):
        type_of_question: str = find_type_of_question(browser=browser)

        if type_of_question == 'MULTIPLE CHOICE':
            multiple_choice_field: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='/html/body/div/div/div[2]/div/div/div/div[2]/div[4]/div/div[2]/div[2]/div[1]')
            answer_options: list[WebElement, ...] = wait_for_elements_to_appear(browser=multiple_choice_field, how_to_find_element=By.XPATH, value_to_find_elements='//button')
            (choice(seq=answer_options)).click()

            submit_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div[2]/button')
            submit_button.click()

            answer: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div[1]/p/span')
            answer_text: str = answer.text

        elif type_of_question == 'TEXT INPUT':
            answer_input_field: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div/div/div/input')
            answer_input_field.send_keys('69')  # Sends an incorrect answer in order to obtain the correct one for the future

            submit_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div/div[2]/button')
            submit_button.click()

            answer: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div[1]/p/span')
            answer_text: str = answer.text

            answer_text: str = answer_text.split(' or ')[0]
            if any(char.isdigit() for char in answer_text):
                answer_text = get_numbers_from_string(answer_text)[0]

        question_span: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[1]/span')
        question_text: str = question_span.text

        question_and_answer: dict[str, str] = {question_text: answer_text}
        test_questions_and_answers |= question_and_answer

        if i == number_of_questions-1:
            continue

        next_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/button[2]')
        next_button.click()

    view_test_results_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/button[2]')
    view_test_results_button.click()

    with open('test_questions_and_answers.json', 'w') as f:
        json.dump(test_questions_and_answers, f)
