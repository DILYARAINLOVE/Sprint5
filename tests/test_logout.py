import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators
from data import TestData


class TestLogout:
    """Тесты для функциональности выхода пользователя"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait):
        """Фикстура для авторизации перед тестом"""
        self.driver = driver
        self.wait = wait
        
        # Авторизуемся
        self.driver.get(TestData.BASE_URL)
        
        login_button = self.driver.find_element(*MainPageLocators.LOGIN_REGISTRATION_BUTTON)
        login_button.click()
        
        email_input = self.wait.until(
            EC.visibility_of_element_located(AuthModalLocators.LOGIN_EMAIL_INPUT)
        )
        email_input.send_keys(TestData.EXISTING_USER_EMAIL)
        
        password_input = self.driver.find_element(*AuthModalLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(TestData.EXISTING_USER_PASSWORD)
        
        submit_button = self.driver.find_element(*AuthModalLocators.LOGIN_BUTTON)
        submit_button.click()
        
        # Ждем завершения авторизации
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
    
    
    def test_successful_logout(self):
        """Тест 5: Успешный выход из системы"""
        
        # 1. Нажимаем кнопку "Выйти"
        logout_button = self.driver.find_element(*MainPageLocators.LOGOUT_BUTTON)
        logout_button.click()
        
        # 2. Проверяем, что пользователь вышел
        self.wait.until(
            EC.invisibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        
        # 3. Проверяем, что появилась кнопка "Вход и регистрация"
        login_button = self.driver.find_element(*MainPageLocators.LOGIN_REGISTRATION_BUTTON)
        assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' должна появиться после выхода"