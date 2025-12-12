import time


class TestData:
    """Тестовые данные для проекта"""
    
    
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru"
    
    
    EXISTING_USER_EMAIL = "dilyararunova@yandex.ru"
    EXISTING_USER_PASSWORD = "1234567890"
    
    
    ADVERTISEMENT_TITLE = "Ноутбук Asus ROG"
    ADVERTISEMENT_DESCRIPTION = "Мощный игровой ноутбук в отличном состоянии"
    ADVERTISEMENT_PRICE = "75000"
    ADVERTISEMENT_CATEGORY = "Технологии"
    ADVERTISEMENT_CITY = "Москва"
    
    @staticmethod
    def generate_email():
        """Генерация уникального email для регистрации"""
        timestamp = int(time.time())  
        return f"test_user_{timestamp}@example.com"