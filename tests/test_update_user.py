import pytest
import requests
import allure

from data.text_response import TextResponse
from helpers.helpers import Person
from data.status_code import StatusCode
from data.urls import URL, Endpoints


class TestChangeUserData:

    @allure.title('Проверка изменения данных с авторизацией')
    @allure.description('''
                        1. Отправляем запрос на создание пользователя;
                        2. Отправляем запрос на изменение параметров пользователя;
                        3. Проверяем ответ;
                        4. Удаляем пользователя.
                        ''')
    @pytest.mark.parametrize('data', [
        # Используем корректные данные для изменения: имя, пароль и email
        Person.create_data_correct_user()["name"],
        Person.create_data_correct_user()["password"],
        Person.create_data_correct_user()["email"]
    ])
    def test_change_person_data(self, create_new_user, data):
        # Получение токена авторизации из ответа на создание пользователя
        token = create_new_user[1].json()["accessToken"]
        assert token, "Не удалось получить токен авторизации"

        # Установка заголовков авторизации
        headers = {'Authorization': token}

        # Отправка запроса на изменение данных пользователя
        response = requests.patch(
            url=URL.main_url + Endpoints.DATA_CHANGE,
            headers=headers,
            data=data
        )

        # Проверка успешного ответа сервера
        assert response.status_code == StatusCode.OK, f"Неверный статус код: {response.status_code}"
        assert response.json().get("success") == True, "Ответ сервера не содержит success=True"

    @allure.title('Проверка изменения данных пользователя без авторизации')
    @allure.description('''
                        1. Отправляем запрос на изменение параметров пользователя;
                        2. Проверяем ответ.
                        ''')
    @pytest.mark.parametrize('data', [
        # Используем корректные данные для изменения: имя, пароль и email
        Person.create_data_correct_user()["name"],
        Person.create_data_correct_user()["password"],
        Person.create_data_correct_user()["email"]
    ])
    def test_change_person_data_whithout_auth(self, data):
        # Отправка запроса на изменение данных без передачи заголовка авторизации
        response = requests.patch(
            url=URL.main_url + Endpoints.DATA_CHANGE,
            data=data
        )

        # Проверка, что сервер возвращает ошибку авторизации
        assert response.status_code == StatusCode.UNAUTHORIZED, (
            f"Неверный статус код: {response.status_code}"
        )
        assert response.json().get("message") == TextResponse.UNAUTHORIZED, (
            "Ответ сервера не содержит ожидаемое сообщение об ошибке авторизации"
        )
