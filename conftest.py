import pytest  # Импорт библиотеки pytest для написания и запуска тестов
import requests  # Импорт библиотеки requests для выполнения HTTP-запросов

from helpers.helpers import Person  # Импорт класса Person из модуля helpers для создания данных пользователя
from data.urls import URL, Endpoints  # Импорт базового URL и эндпоинтов из модуля data.urls

# Фикстура создания / удаления пользователя
@pytest.fixture
def create_new_user():
    payload = Person.create_data_correct_user()  # Генерация данных для нового пользователя с помощью класса Person
    response = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)  # Отправка POST-запроса для создания пользователя
    yield payload, response  # Возвращаем данные и ответ на запрос, после выполнения теста
    token = response.json()["accessToken"]  # Извлекаем токен из ответа для удаления пользователя
    requests.delete(URL.main_url + Endpoints.DELETE_USER, headers={"Authorization": token})  # Отправляем DELETE-запрос для удаления пользователя

# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    return repr(val)  # Возвращаем строковое представление аргумента для параметризированных тестов
