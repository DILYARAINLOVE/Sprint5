import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
   
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    

    driver.implicitly_wait(15)
    driver.set_page_load_timeout(30)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def wait(driver):
    """Фикстура для явных ожиданий"""
    return WebDriverWait(driver, 20)


@pytest.fixture
def login(driver, wait):
    """Фикстура для авторизации пользователя"""
    from data import TestData
    from locators import MainPageLocators, AuthModalLocators
    
    try:
        driver.get(TestData.BASE_URL)
        time.sleep(3)  
        
        
        login_buttons = driver.find_elements(*MainPageLocators.LOGIN_REGISTRATION_BUTTON)
        if login_buttons:
            login_buttons[0].click()
        else:
            
            all_buttons = driver.find_elements(By.TAG_NAME, "button")
            for button in all_buttons:
                if "Вход" in button.text or "войти" in button.text.lower():
                    button.click()
                    break
        
        time.sleep(2)
        
        # Заполняем форму авторизации
        email_inputs = driver.find_elements(*AuthModalLocators.LOGIN_EMAIL_INPUT)
        if email_inputs:
            email_inputs[0].send_keys(TestData.EXISTING_USER_EMAIL)
        else:
            
            inputs = driver.find_elements(By.TAG_NAME, "input")
            for input_elem in inputs:
                placeholder = input_elem.get_attribute("placeholder") or ""
                if "email" in placeholder.lower() or "почта" in placeholder.lower():
                    input_elem.send_keys(TestData.EXISTING_USER_EMAIL)
                    break
        
        password_inputs = driver.find_elements(*AuthModalLocators.LOGIN_PASSWORD_INPUT)
        if password_inputs:
            password_inputs[0].send_keys(TestData.EXISTING_USER_PASSWORD)
        else:
            
            password_fields = driver.find_elements(By.XPATH, "//input[@type='password']")
            if password_fields:
                password_fields[0].send_keys(TestData.EXISTING_USER_PASSWORD)
        
        # Нажимаем кнопку входа
        login_buttons_in_modal = driver.find_elements(*AuthModalLocators.LOGIN_BUTTON)
        if login_buttons_in_modal:
            login_buttons_in_modal[0].click()
        else:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if "Войти" in button.text:
                    button.click()
                    break
        
        time.sleep(3)  
        
    except Exception as e:
        print(f"Ошибка при авторизации: {e}")
    
    return driver