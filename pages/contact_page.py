from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    NAME_FIELD = (By.ID, "name")
    EMAIL_FIELD = (By.ID, "email")
    MESSAGE_FIELD = (By.ID, "message")
    SUBMIT_BUTTON = (By.ID, "submit")
    SUCCESS_MSG = (By.ID, "success")
    ERROR_MSG = (By.ID, "error")

    def fill_form(self, name, email, message):
        self.fill(self.NAME_FIELD, name)
        self.fill(self.EMAIL_FIELD, email)
        self.fill(self.MESSAGE_FIELD, message)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)
