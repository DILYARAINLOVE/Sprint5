import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Импорты для фикстур
from data import TestData
from locators import MainPageLocators, AuthModalLocators

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    """Фикстура для явных ожиданий"""
    return WebDriverWait(driver, 15)

@pytest.fixture
def login(driver, wait):
    """Фикстура для авторизации пользователя"""
    driver.get(TestData.BASE_URL)
    
    # Явное ожидание вместо условий
    login_button = wait.until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTRATION_BUTTON)
    )
    login_button.click()
    
    email_input = wait.until(
        EC.visibility_of_element_located(AuthModalLocators.LOGIN_EMAIL_INPUT)
    )
    email_input.send_keys(TestData.EXISTING_USER_EMAIL)
    
    password_input = driver.find_element(*AuthModalLocators.LOGIN_PASSWORD_INPUT)
    password_input.send_keys(TestData.EXISTING_USER_PASSWORD)
    
    submit_button = driver.find_element(*AuthModalLocators.LOGIN_BUTTON)
    submit_button.click()
    
    # Явное ожидание завершения авторизации
    wait.until(
        EC.visibility_of_element_located(MainPageLocators.USER_AVATAR)
    )
    
    return driver