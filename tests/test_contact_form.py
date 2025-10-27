import pytest
from pages.contact_page import ContactPage

URL = "http://localhost:8000/form.html" 

@pytest.mark.usefixtures("driver")
class TestContactForm:

    # --- Позитивные ---
    def test_positive_valid_data(self, driver):
        """Все поля валидные"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("Пуся", "test@example.com", "Привет, ты тоже пуся")
        page.submit()
        assert "успешно" in page.get_text(ContactPage.SUCCESS_MSG).lower()

    def test_positive_message_with_cyrillic(self, driver):
        """Проверка кириллицы в сообщении"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("Хейтер", "test@example.com", "Только на русском языке можно описать тебя полностью")
        page.submit()
        assert "успешно" in page.get_text(ContactPage.SUCCESS_MSG).lower()

    def test_positive_email_format(self, driver):
        """Корректный формат email"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("Даша", "test@example.com", "моя почта ок или нет?")
        page.submit()
        assert "успешно" in page.get_text(ContactPage.SUCCESS_MSG).lower()

    # --- Негативные ---
    def test_negative_empty_name(self, driver):
        """Пустое имя"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("", "test@example.com", "аноним")
        page.submit()
        assert "имя" in page.get_text(ContactPage.ERROR_MSG).lower()

    def test_negative_empty_message(self, driver):
        """Пустое сообщение"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("незнайка", "test@example.com", "")
        page.submit()
        assert "сообщение" in page.get_text(ContactPage.ERROR_MSG).lower()
