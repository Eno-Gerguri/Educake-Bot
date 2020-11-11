from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome


def wait_for_element_to_appear(browser: Chrome, how_to_find_element: str, value_to_find_element: str) -> WebElement:
    while True:
        try:
            element_to_find: WebElement = WebDriverWait(browser, 5).until(ec.presence_of_element_located((how_to_find_element, value_to_find_element)))
            # element_to_find: WebElement = browser.find_element(by=how_to_find_element, value=value_to_find_element)
            return element_to_find
        except:
            continue


def wait_for_elements_to_appear(browser: Chrome or WebElement, how_to_find_element: str, value_to_find_elements: str) -> list[WebElement, ...]:
    while True:
        try:
            elements_to_find: list[WebElement, ...] = WebDriverWait(browser, 5).until(ec.presence_of_all_elements_located((how_to_find_element, value_to_find_elements)))
            # browser.find_elements(by=how_to_find_element, value=value_to_find_elements)
            return elements_to_find
        except Exception as e:
            print(e)
            continue


def find_type_of_question(browser: Chrome) -> str:
    while True:
        try:
            multiple_choice_field: WebElement = browser.find_element_by_xpath('//*[@class="ui multiple-choice field"]')
            if multiple_choice_field:
                return 'MULTIPLE CHOICE'
        except:
            pass

        try:
            answer_input_field: WebElement = browser.find_element_by_xpath('//*[@id="scroll-top"]/div[4]/div/div[2]/div[2]/div/div/div/input')
            if answer_input_field:
                return 'TEXT INPUT'
        except:
            pass


def get_numbers_from_string(input_string: str) -> list[str, ...]:
    output_numbers: list[str, ...] = []
    output_string: str = ''

    for i, char in enumerate(input_string):

        if char.isalpha() or char == ' ':
            if output_string != '':
                output_numbers.append(output_string)
            output_string: str = ''

        elif char == '-':
            if len(output_string) == 0:
                try:
                    if input_string[i + 1].isdigit():
                        output_string += char
                except IndexError:
                    if output_string != '':
                        output_numbers.append(output_string)
                    output_string: str = ''

        elif char == '.':
            if output_string[-1].isdigit():
                try:
                    if input_string[i + 1].isdigit():
                        output_string += char
                except IndexError:
                    if output_string != '':
                        output_numbers.append(output_string)
                    output_string: str = ''

            try:
                if input_string[i + 1]:
                    pass
            except IndexError:
                if output_string != '':
                    output_numbers.append(output_string)
                output_string: str = ''

        elif char.isdigit():
            output_string += char

            try:
                if input_string[i + 1]:
                    pass
            except IndexError:
                if output_string != '':
                    output_numbers.append(output_string)
                output_string: str = ''

        else:
            if output_string != '':
                output_numbers.append(output_string)
            output_string: str = ''

    return output_numbers
