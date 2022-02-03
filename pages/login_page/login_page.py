import logging

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


from models.auth import AuthData
from pages.base_page import BasePage


logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, "input[name='UserName']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='Password']")
    SUBMIT = (By.ID, "login")
    SHOPPING_CART_CONTAINER = (By.CLASS_NAME, "text-success")
    LOGIN_ERROR = (By.CLASS_NAME, "text-danger")

    def is_auth(self):
        self.find_element(LoginPage.SHOPPING_CART_CONTAINER)
        element = self.find_elements(LoginPage.SHOPPING_CART_CONTAINER)
        if element:
            return True
        return False

    def email_input(self) -> WebElement:
        return self.find_element(LoginPage.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPage.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPage.SUBMIT)

    def auth_login_error(self) -> str:
        return self.find_element(LoginPage.LOGIN_ERROR).text

    def auth(self, data: AuthData):
        logger.info(f'User email is "{data.login}, user password {data.password}"')
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())
