from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопка "Вход и регистрация" 
    LOGIN_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(., 'Вход') or contains(., 'войти')]")
    
    # Кнопка "Разместить объявление"
    PLACE_ADVERTISEMENT_BUTTON = (By.XPATH, "//button[contains(., 'Разместить')]")
    
    # Элементы после авторизации
    USER_AVATAR = (By.XPATH, "//img[contains(@src, 'avatar') or contains(@alt, 'avatar')]")
    USER_NAME = (By.XPATH, "//span[contains(text(), 'User') or contains(text(), 'Пользователь')]")
    
    # Кнопка выхода 
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Выйти')]")
    
    # Ссылка/кнопка профиля
    PROFILE_LINK = (By.XPATH, "//a[contains(., 'Профиль') or contains(., 'Мои объявления')]")

class AuthModalLocators:
    """Локаторы модального окна авторизации/регистрации"""
    
    # Переключение на регистрацию
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")
    
    # Поля формы регистрации
    REG_EMAIL_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Email') or @type='email']")
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and contains(@placeholder, 'Пароль')][1]")
    REG_REPEAT_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and contains(@placeholder, 'Повторите') or contains(@placeholder, 'Пароль')][2]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")
    
    # Поля формы авторизации
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@type='text' and contains(@placeholder, 'Email')]")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and contains(@placeholder, 'Пароль')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")
    
    # Элементы ошибок
    ERROR_FIELDS = (By.CSS_SELECTOR, "input[class*='error'], input.error")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'Ошибка') or contains(@class, 'error')]")

class AdvertisementModalLocators:
    """Локаторы модального окна создания объявления"""
    
    # Заголовок для неавторизованных
    MODAL_TITLE = (By.XPATH, "//h2[contains(., 'авторизуйтесь')]")
    
    # Поля формы
    TITLE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Название')]")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[contains(@placeholder, 'Описание')]")
    PRICE_INPUT = (By.XPATH, "//input[@type='number' or contains(@placeholder, 'Стоимость')]")
    
    # Dropdown'ы
    CATEGORY_DROPDOWN = (By.XPATH, "//div[contains(., 'Категория')]")
    CITY_DROPDOWN = (By.XPATH, "//div[contains(., 'Город')]")
    
    # Радиокнопки
    USED_RADIO = (By.XPATH, "//input[@value='used' or @type='radio'][1]")
    NEW_RADIO = (By.XPATH, "//input[@value='new' or @type='radio'][2]")
    
    # Кнопка
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(., 'Опубликовать')]")

class ProfilePageLocators:
    """Локаторы страницы профиля"""
    
    MY_ADVERTISEMENTS_TITLE = (By.XPATH, "//h2[contains(., 'Мои объявления') or contains(., 'Объявления')]")
    ADVERTISEMENT_ITEM = (By.XPATH, "//div[contains(@class, 'advertisement') or contains(@class, 'card')]")
    ADVERTISEMENT_TITLE = (By.XPATH, ".//h3 | .//h4")  # Относительный поиск внутри ADVERTISEMENT_ITEM

class DropdownOptions:
    """Опции в dropdown"""
    
    CATEGORY_ELECTRONICS = (By.XPATH, "//div[text()='Электроника' or contains(text(), 'Электроника')]")
    CITY_MOSCOW = (By.XPATH, "//div[text()='Москва' or contains(text(), 'Москва')]")