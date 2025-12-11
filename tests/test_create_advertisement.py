import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from locators import MainPageLocators, AuthModalLocators, AdvertisementModalLocators, ProfilePageLocators
from data import TestData


class TestCreateAdvertisement:
    """Тесты для функциональности создания объявлений"""
    
    def test_create_advertisement_unauthorized(self, driver, wait):
        """Тест 6: Попытка создания объявления неавторизованным пользователем"""
        
        # 1. Открываем главную страницу (неавторизованными)
        driver.get(TestData.BASE_URL)
        
        # 2. Нажимаем кнопку "Разместить объявление"
        place_button = driver.find_element(*MainPageLocators.PLACE_ADVERTISEMENT_BUTTON)
        place_button.click()
        
        # 3. Проверяем модальное окно с требованием авторизации
        modal_title = wait.until(
            EC.visibility_of_element_located(AdvertisementModalLocators.MODAL_TITLE)
        )
        
        assert modal_title.is_displayed(), "Должно появиться модальное окно с требованием авторизации"
        
        expected_text = "Чтобы разместить объявление, авторизуйтесь"
        assert expected_text in modal_title.text, f"Заголовок должен содержать '{expected_text}'"
    
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait):
        """Фикстура для авторизации перед тестом создания объявления"""
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
    
    
    def test_create_advertisement_authorized(self):
        """Тест 7: Создание объявления авторизованным пользователем"""
        
        # 1. Нажимаем кнопку "Разместить объявление"
        place_button = self.driver.find_element(*MainPageLocators.PLACE_ADVERTISEMENT_BUTTON)
        place_button.click()
        
        # 2. Заполняем обязательные поля
        title_input = self.wait.until(
            EC.visibility_of_element_located(AdvertisementModalLocators.TITLE_INPUT)
        )
        title_input.send_keys(TestData.ADVERTISEMENT_TITLE)
        
        description_input = self.driver.find_element(*AdvertisementModalLocators.DESCRIPTION_INPUT)
        description_input.send_keys(TestData.ADVERTISEMENT_DESCRIPTION)
        
        price_input = self.driver.find_element(*AdvertisementModalLocators.PRICE_INPUT)
        price_input.send_keys(TestData.ADVERTISEMENT_PRICE)
        
        # 3. Выбираем категорию из dropdown
        category_dropdown = Select(self.driver.find_element(*AdvertisementModalLocators.CATEGORY_DROPDOWN))
        category_dropdown.select_by_visible_text(TestData.ADVERTISEMENT_CATEGORY)
        
        # 4. Выбираем город из dropdown
        city_dropdown = Select(self.driver.find_element(*AdvertisementModalLocators.CITY_DROPDOWN))
        city_dropdown.select_by_visible_text(TestData.ADVERTISEMENT_CITY)
        
        # 5. Выбираем состояние товара (б/у)
        used_radio = self.driver.find_element(*AdvertisementModalLocators.USED_RADIO)
        used_radio.click()
        
        # 6. Нажимаем кнопку "Опубликовать"
        publish_button = self.driver.find_element(*AdvertisementModalLocators.PUBLISH_BUTTON)
        publish_button.click()
        
        # 7. Переходим в профиль пользователя
        profile_link = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.PROFILE_LINK)
        )
        profile_link.click()
        
        # 8. Проверяем созданное объявление в профиле
        self.wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.MY_ADVERTISEMENTS_TITLE)
        )
        
        advertisements = self.driver.find_elements(*ProfilePageLocators.ADVERTISEMENT_ITEM)
        assert len(advertisements) > 0, "В профиле должно быть хотя бы одно объявление"
        
        # Проверяем, что созданное объявление присутствует
        advertisement_titles = self.driver.find_elements(*ProfilePageLocators.ADVERTISEMENT_TITLE)
        found = False
        for title_element in advertisement_titles:
            if TestData.ADVERTISEMENT_TITLE in title_element.text:
                found = True
                break
        
        assert found, f"Объявление с названием '{TestData.ADVERTISEMENT_TITLE}' не найдено в профиле"