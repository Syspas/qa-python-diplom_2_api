class TextResponse:
    """Класс для хранения стандартных текстовых сообщений ответа сервера."""

    # Сообщение о попытке создания уже существующего пользователя
    CREATE_DOUBLE_USER = 'User already exists'

    # Сообщение об ошибке на стороне сервера
    SERVER_ERROR = 'Internal Server Error'

    # Сообщение об ошибке авторизации
    UNAUTHORIZED = 'You should be authorised'
