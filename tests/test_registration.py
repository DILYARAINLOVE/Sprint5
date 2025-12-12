import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators
from data import TestData

class TestRegistration:
    
    def test_successful_registration(self, driver, wait):
        """Тест успешной регистрации"""
        
        # 1. Открываем главную страницу
        driver.get(TestData.BASE_URL)
        
        # 2. Ожидаем загрузки страницы
        wait.until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_REGISTRATION_BUTTON)
        )
        
        # 3. Нажимаем кнопку "Вход и регистрация"
        login_button = driver.find_element(*MainPageLocators.LOGIN_REGISTRATION_BUTTON)
        login_button.click()
        
        # 4. Ожидаем появления кнопки "Нет аккаунта"
        no_account_button = wait.until(
            EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)
        )
        no_account_button.click()
        
        # 5. Заполняем форму регистрации
        email_input = wait.until(
            EC.visibility_of_element_located(AuthModalLocators.REG_EMAIL_INPUT)
        )
        email_input.send_keys(TestData.generate_email())
        
        password_input = driver.find_element(*AuthModalLocators.REG_PASSWORD_INPUT)
        password_input.send_keys("TestPassword123!")
        
        repeat_password_input = driver.find_element(*AuthModalLocators.REG_REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys("TestPassword123!")
        
        # 6. Нажимаем кнопку "Создать аккаунт"
        create_button = driver.find_element(*AuthModalLocators.CREATE_ACCOUNT_BUTTON)
        create_button.click()
        
        # 7. Ожидаем успешной регистрации (проверяем аватар)
        wait.until(
            EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
        )
        
        # 8. Проверяем, что отображается имя пользователя
        user_name = driver.find_element(*MainPageLocators.USER_NAME)
        assert user_name.is_displayed(), "Имя пользователя должно отображаться после регистрации"