import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIES = (By.XPATH, '// *[ @ id = "__next"] / div[5] / div / div / button')
    BEGIN_PROJECT = (By.XPATH, '//*[@id="__next"]/div[5]/main/div[1]/footer/div[1]/div[1]/div')


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://only.digital/projects'

    def go_to_site(self):
        self.driver.get(self.base_url)
        time.sleep(10)
        iframe = self.driver.find_element(By.TAG_NAME, "iframe")
        scroll_origin = ScrollOrigin.from_element(iframe)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 5000).perform()
        time.sleep(5)

        search_n_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(BasePageLocators.BEGIN_PROJECT),
                                                          message=f'Не найден {BasePageLocators.BEGIN_PROJECT}')
        return search_n_button.click()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Не найден {locator}')

    def scroll_down(self, offset=0):
        """ Scroll the page down. """
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        print('OK я отработал')
