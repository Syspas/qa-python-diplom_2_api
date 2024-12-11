class URL:
    """URL сервиса"""

    # Основной URL для взаимодействия с сервисом
    main_url = 'https://stellarburgers.nomoreparties.site'


class Endpoints:
    """Ручки (endpoints) для работы с API"""

    # Эндпоинт для создания нового пользователя
    CREATE_USER = '/api/auth/register'

    # Эндпоинт для авторизации пользователя
    LOGIN = '/api/auth/login'

    # Эндпоинт для удаления пользователя
    DELETE_USER = '/api/auth/user'

    # Эндпоинт для создания нового заказа
    CREATE_ORDER = '/api/orders'

    # Эндпоинт для получения списка заказов
    GET_ORDERS = '/api/orders'

    # Эндпоинт для изменения данных пользователя
    DATA_CHANGE = '/api/auth/user'
