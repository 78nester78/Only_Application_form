# import time
#
# from selenium.webdriver.common.by import By
# from base_page import BasePage
# from selenium.webdriver import ActionChains
#
#
# class OnlyProjectsLocators:
#     COOKIES = (By.XPATH, '// *[ @ id = "__next"] / div[5] / div / div / button')
#     BEGIN_PROJECT = (By.CLASS_NAME, 'sc-8907ce56-1 eNKOTy')
#
#
# class ProjectPage(BasePage):
#     def open_form(self):
#         search_el_cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located(COOKIES),
#                                                            message=f'Не найден {COOKIES}')
#         ActionChains(driver).move_to_element(search_el_cookie).click().perform()
#
#         iframe = driver.find_element(By.TAG_NAME, "iframe")
#         scroll_origin = ScrollOrigin.from_element(iframe)
#         ActionChains(driver).scroll_from_origin(scroll_origin, 0, 3500).perform()
#         time.sleep(5)
#
#         search_n_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(BEGIN_PROJECT),
#                                                           message=f'Не найден {BEGIN_PROJECT}')
#         return search_n_button.click()



