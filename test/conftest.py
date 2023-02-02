import pytest
import run


# Создаем ФИКСТУРУ для тестирования всех вьюшек
@pytest.fixture()
def test_client():
    app = main.app
    return app.test_client()
