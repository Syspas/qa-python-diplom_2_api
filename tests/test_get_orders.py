import requests
import allure

from data.ingredients import Ingredients
from data.status_code import StatusCode
from data.text_response import TextResponse
from data.urls import URL, Endpoints


class TestCreateOrder:

    @allure.title('Проверка создания заказа авторизованным пользователем')
    @allure.description('''
                        1. Отправляем запрос на создание пользователя;
                        2. Отправляем запрос на создание заказа;
                        3. Отправляем запрос на получение заказа пользователя
                        4. Проверяем ответ;
                        5. Удаляем пользователя
                        ''')
    def test_get_order_whith_auth(self, create_new_user):
        # Извлечение токена авторизации из ответа на создание пользователя
        token = create_new_user[1].json()["accessToken"]

        # Проверка, что токен авторизации получен
        assert token, "Не удалось получить токен авторизации"

        # Заголовки с токеном авторизации
        headers = {'Authorization': token}

        # Отправка POST-запроса для создания заказа
        response_create_order = requests.post(
            url=f"{URL.main_url}{Endpoints.CREATE_ORDER}",
            headers=headers,
            data=Ingredients.correct_ingredients_data
        )

        # Проверка успешного создания заказа
        assert response_create_order.status_code == StatusCode.OK, (
            f"Ошибка при создании заказа: {response_create_order.status_code}"
        )

        # Отправка GET-запроса для получения списка заказов пользователя
        response_get_order = requests.get(
            url=f"{URL.main_url}{Endpoints.GET_ORDERS}",
            headers=headers
        )

        # Проверка успешного получения списка заказов
        assert response_get_order.status_code == StatusCode.OK, (
            f"Ошибка при получении заказов: {response_get_order.status_code}"
        )

        # Проверка, что номер созданного заказа совпадает с номером в списке заказов
        assert (
                response_create_order.json()["order"]["number"] == response_get_order.json()["orders"][0]["number"]
        ), "Номер созданного заказа не совпадает с номером в списке заказов"

    @allure.title('Проверка получения заказа неавторизованным пользователем')
    @allure.description('''
                        1. Отправляем запрос на получение заказа;
                        2. Проверяем ответ.
                        ''')
    def test_get_order_whithout_auth(self):
        # Отправка GET-запроса для получения списка заказов без авторизации
        response_get_order = requests.get(
            url=f"{URL.main_url}{Endpoints.GET_ORDERS}"
        )

        # Проверка, что доступ к заказам запрещен
        assert response_get_order.status_code == StatusCode.UNAUTHORIZED, (
            f"Неверный код ответа: {response_get_order.status_code}"
        )

        # Проверка текста ошибки в ответе
        assert TextResponse.UNAUTHORIZED in response_get_order.text, (
            "Текст ошибки не соответствует ожидаемому"
        )
