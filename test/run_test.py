keys_should_be = {
    'poster_name',
    'poster_avatar',
    'pic',
    'content',
    'views_count',
    'likes_count',
    'pk',
}


class TestRun:
    """Тестирует run.py"""

    def test_root_status(self, test_client):
        """Проверяет статус_код всех постов"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"

    def test_content(self, test_client):
        """Проверяет кодировку контента"""
        response = test_client.get('/', follow_redirects=True)
        assert response.data.decode('utf=8'), "Неверная кодировка всех постов (ну или тест на кодировку)"

    def test_api_all_posts(self, test_client):
        response = test_client().get('/api/posts', follow_redirects=True)
        api_response = response.json()
        assert response.status_code == 200, 'Кидай ноут в окно: статус-код неверный!'
        assert type(api_response) == list, 'Данные не в формате листа'
        assert set(api_response[0].keys()) == keys_should_be, 'Ключи не совпадают с ожидаемыми'
        assert response.data.decode('utf=8'), "Неверная кодировка всех постов (ну или тест на кодировку)"

    def test_api_post(self, test_client):
        response = test_client().get('/api/posts/1')
        api_response = response.json()
        assert response.status_code == 200, 'Кидай ноут в окно: статус-код неверный!'
        assert type(api_response) == dict, 'Данные не в формате листа'
        assert set(api_response[0].keys()) == keys_should_be, 'Ключи не совпадают с ожидаемыми'
