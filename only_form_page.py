
from selenium.webdriver.common.by import By
from base_page import BasePage


class OnlySearchLocators:

    CHECK_ELEM = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/h1')
    NAME_FIELD = (By.NAME, 'name')
    EMAIL_FIELD = (By.NAME, 'email')
    PHONE_FIELD = (By.NAME, 'phone')
    COMPANY_FIELD = (By.NAME, 'company')
    WRONG_NAME = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/form/div[1]/div/div[1]/p')
    ABOUT_THE_PROJECT = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/form/div[2]/div[2]/textarea')
    SEND_BUTTON = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/form/div[6]/button')


class SearchHelper(BasePage):
    def check_page(self):
        check_elem = self.find_element(OnlySearchLocators.CHECK_ELEM)
        return check_elem.text

    def enter_name(self, some):
        search_field = self.find_element(OnlySearchLocators.NAME_FIELD)
        search_field.click()
        search_field.send_keys(some)
        return search_field.text

    def check_name_field(self):
        mail_field = self.find_element(OnlySearchLocators.EMAIL_FIELD)
        mail_field.click()
        check_name = self.find_element(OnlySearchLocators.WRONG_NAME)
        return check_name.text

    def enter_email(self, some):
        email_field = self.find_element(OnlySearchLocators.EMAIL_FIELD)
        email_field.click()
        email_field.send_keys(some)
        return email_field.text

    def enter_phone(self, some):
        phone_field = self.find_element(OnlySearchLocators.PHONE_FIELD)
        phone_field.click()
        phone_field.send_keys(some)
        return phone_field.text

    def enter_company(self, some):
        company_field = self.find_element(OnlySearchLocators.COMPANY_FIELD)
        company_field.click()
        company_field.send_keys(some)
        return company_field.text

    def enter_about_project(self, some):
        project_field = self.find_element(OnlySearchLocators.ABOUT_THE_PROJECT)
        project_field.click()
        project_field.send_keys(some)
        return project_field.text

    def send_form(self):
        send_button = self.find_element(OnlySearchLocators.SEND_BUTTON)
        send_button.click()
