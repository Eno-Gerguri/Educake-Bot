import json

from web_bot_helper_functions import wait_for_element_to_appear, wait_for_elements_to_appear, find_type_of_question, get_numbers_from_string
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome

def do_test(browser: Chrome) -> None:
    take_test_again_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.ID, value_to_find_element='taketestagainbutton')
    take_test_again_button.click()
    
    start_test_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="container"]/div/div[2]/div[2]')
    start_test_button.click()

    number_of_questions_answered_element: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[1]/div[1]/div[1]/h3')
    number_of_questions: int = int(number_of_questions_answered_element.text.split(' of ')[1])  # The number of questions in this quiz

    with open('test_questions_and_answers.json', 'r') as f:
        test_questions_and_answers: dict[str, str, ...] = json.load(f)

    for i in range(number_of_questions):
        question_span: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[1]/span')
        question_text = question_span.text

        answer_text: str = test_questions_and_answers[question_text]
        
        type_of_question: str = find_type_of_question(browser=browser)
        
        if type_of_question == 'MULTIPLE CHOCIE':
            multiple_choice_field: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='/html/body/div/div/div[2]/div/div/div/div[2]/div[4]/div/div[2]/div[2]/div[1]')
            answer_options: list[WebElement, ...] = wait_for_elements_to_appear(browser=multiple_choice_field, how_to_find_element=By.CSS_SELECTOR, value_to_find_elements='button')

            for option in answer_options:
                if option.text in answer_text:
                    option.click()
                    break
            
            submit_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div[2]/button')
            submit_button.click()

        elif type_of_question == 'TEXT INPUT':
            answer_input_field: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div/div/div/input')
            answer_input_field.send_keys(answer_text)

            submit_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div/div[2]/button')
            submit_button.click()

        if i == number_of_questions-1:
            continue

        next_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/button[2]')
        next_button.click()

    view_test_results_button: WebElement = wait_for_element_to_appear(browser=browser, how_to_find_element=By.XPATH, value_to_find_element='//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/button[2]')
    view_test_results_button.click()
