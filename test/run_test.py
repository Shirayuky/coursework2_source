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