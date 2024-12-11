from faker import Faker  # Импорт библиотеки Faker для генерации фиктивных данных

class Person:
    """Методы генерации данных для регистрации пользователей в системе"""

    @staticmethod
    def create_data_correct_user():
        """Генерация данных для корректного пользователя"""
        faker = Faker('ru_RU')  # Инициализация Faker с русской локализацией
        data = {
            "email": faker.email(),  # Генерация случайного email
            "password": faker.password(),  # Генерация случайного пароля
            "name": faker.first_name()  # Генерация случайного имени
        }
        return data  # Возвращаем сгенерированные данные

    @staticmethod
    def create_data_incorrect_user_without_email():
        """Генерация данных для некорректного пользователя без email"""
        faker = Faker('ru_RU')  # Инициализация Faker с русской локализацией
        data = {
            "password": faker.password(),  # Генерация случайного пароля
            "name": faker.first_name()  # Генерация случайного имени
        }
        return data  # Возвращаем сгенерированные данные без email

    @staticmethod
    def create_data_incorrect_user_without_password():
        """Генерация данных для некорректного пользователя без пароля"""
        faker = Faker('ru_RU')  # Инициализация Faker с русской локализацией
        data = {
            "email": faker.email(),  # Генерация случайного email
            "name": faker.first_name()  # Генерация случайного имени
        }
        return data  # Возвращаем сгенерированные данные без пароля

    @staticmethod
    def create_data_incorrect_user_without_name():
        """Генерация данных для некорректного пользователя без имени"""
        faker = Faker('ru_RU')  # Инициализация Faker с русской локализацией
        data = {
            "email": faker.email(),  # Генерация случайного email
            "password": faker.password(),  # Генерация случайного пароля
        }
        return data  # Возвращаем сгенерированные данные без имени
