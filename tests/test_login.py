import allure
import requests

from helpers.helpers import Person
from data.status_code import StatusCode
from data.urls import URL, Endpoints


class TestCreateUser:

    @allure.title('Проверка логина под существующим пользователем')
    @allure.description('''
                        1. Отправляем запрос на создание пользователя;
                        2. Отправляем запрос на логин в системе;
                        3. Проверяем ответ;
                        4. Удаляем пользователя.
                        ''')
    def test_login_user(self, create_new_user):
        # Получение данных для создания пользователя и самого ответа на запрос
        response = create_new_user

        # Отправка запроса на логин с данными созданного пользователя
        login = requests.post(URL.main_url + Endpoints.LOGIN, data=response[0])

        # Проверка успешного статуса ответа и успешного логина
        assert login.status_code == StatusCode.OK, f"Неверный статус код: {login.status_code}"
        assert login.json().get("success") is True, "Авторизация не удалась, success=False"

    @allure.title('Проверка логина под несуществующим пользователем')
    @allure.description('''
                        1. Отправляем запрос на логин в системе без регистрации;
                        2. Проверяем ответ.
                        ''')
    def test_login_under_none_user(self):
        # Создание данных для несуществующего пользователя без имени
        incorrect_user_data = Person.create_data_incorrect_user_without_name()

        # Отправка запроса на логин с некорректными данными
        login = requests.post(URL.main_url + Endpoints.LOGIN, data=incorrect_user_data)

        # Проверка статуса ответа и подтверждение, что логин не удался
        assert login.status_code == StatusCode.UNAUTHORIZED, f"Неверный статус код: {login.status_code}"
        assert login.json().get("success") is False, "Логин прошел успешно для несуществующего пользователя"
