import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators
from data import TestData


class TestLogin:
    """Тесты для функциональности авторизации пользователя"""
    
    def test_successful_login(self, driver, wait):
        """Тест 4: Успешная авторизация существующего пользователя"""
        
        # 1. Открываем главную страницу
        driver.get(TestData.BASE_URL)
        
        # 2. Нажимаем кнопку "Вход и регистрация"
        login_button = driver.find_element(*MainPageLocators.LOGIN_REGISTRATION_BUTTON)
        login_button.click()
        
        # 3. Заполняем форму авторизации
        email_input = wait.until(
            EC.visibility_of_element_located(AuthModalLocators.LOGIN_EMAIL_INPUT)
        )
        email_input.send_keys(TestData.EXISTING_USER_EMAIL)
        
        password_input = driver.find_element(*AuthModalLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(TestData.EXISTING_USER_PASSWORD)
        
        # 4. Нажимаем кнопку "Войти"
        submit_button = driver.find_element(*AuthModalLocators.LOGIN_BUTTON)
        submit_button.click()
        
        # 5. Проверяем успешную авторизацию
        wait.until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        
        user_name = driver.find_element(*MainPageLocators.USER_NAME)
        assert user_name.is_displayed(), "Имя пользователя должно отображаться после входа"