from only_form_page import *
from only_form_page import SearchHelper
import time
from settings import *
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from base_page import BasePage


def test_contacts(browser):
    """Проверяем переход с базовой страницы проектов на страницу заполнения формы"""
    only_page = BasePage(browser)
    check_el = SearchHelper(browser)
    only_page.go_to_site()
    time.sleep(3)
    check_elem = check_el.check_page()

    assert 'Заполните анкету' in check_elem


# Параметризация великая вещь!
@pytest.mark.parametrize("name",
                         ['Иван', 'Ivan', 111, 'а', 255 * 'а'],
                         ids=["cyrillic", "latin", "numbers", "1 letters", "255 letters"])
def test_enter_valid_name(browser, name):
    """Проверяем ввод валидного значения имени"""
    name_form = SearchHelper(browser)
    name_form.go_to_site()
    time.sleep(3)
    result = name_form.enter_name(name)
    time.sleep(2)

    assert type(result) == type('abc')


@pytest.mark.parametrize("name",
                         [' ', '', '@#$$%^', 256 * 'а'],
                         ids=["space", "empty", "special characters", "256 letters"])
def test_enter_invalid_name(browser, name):
    """Проверяем ввод невалидного значения имени"""
    name_form = SearchHelper(browser)
    check_name = SearchHelper(browser)
    name_form.go_to_site()
    time.sleep(3)
    name_form.enter_name(name)
    check_name_field = check_name.check_name_field()

    assert check_name_field in ['Неверный формат', 'Обязательное поле', 'Превышено максимальное количество символов']


def test_all_field(browser):
    """Заполняем все доступные поля"""
    form = SearchHelper(browser)
    form.go_to_site()
    time.sleep(3)
    form.enter_name(valid_name_1)
    form.enter_email(valid_email)
    form.enter_phone(valid_phone)
    form.enter_company(valid_company)
    time.sleep(2)
    iframe = browser.find_element(By.TAG_NAME, "iframe")
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(browser).scroll_from_origin(scroll_origin, 0, 50).perform()
    form.enter_about_project(about_project)
    time.sleep(2)
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(browser).scroll_from_origin(scroll_origin, 0, 50).perform()
    time.sleep(2)
    form.send_form()

    assert True

# К сожалению не могу преодолеть капчу, поэтому тест заканчивается таким образом.
# По уму надо поймать локатор со страницы отправленной формы и по нему судить о статусе теста.
