from typing import List

import pytest
from app.posts.dao import PostDAO

post_data_path = 'data/posts.json'

parametrize = [
    ('pk', 1),
    ('poster_name', 'hank'),
    ('content', 'вышел')
]


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostDAO(post_data_path)
    return posts_dao_instance


# @pytest.mark.parametrize('arg1, arg2', parametrize)
# def test_post_dao_param(arg1, arg2):
#     assert posts_dao(arg1) == arg2, "Неверный тип данных"


keys_should_be = ['poster_name',
                  'poster_avatar',
                  'pic',
                  'content',
                  'views_count',
                  'likes_count',
                  'pk']


class TestPostsDao:
    def test_get_all(self, posts_dao):
        """Проверяет вывод всех постов"""
        posts = posts_dao.get_all()
        assert type(posts) == List[dict], "Тип постов не словари в виде списка"
        assert len(posts) > 0, "Список постов пуст"
        assert set(posts[0].keys()) == keys_should_be, "Ключи постов не сходятся с ожидаемыми"

    def test_by_pk(self, posts_dao):
        """Проверяет вывод постов по пк"""
        post = posts_dao.get_by_pk(1)
        # assert post['pk'] == 1, "При поиске постов возвращается неверное значение"
        assert set(post.keys()) == keys_should_be, "Ключи поста не сходятся с ожидаемыми"

    def test_by_username(self, posts_dao):
        """Проверяет вывод постов по имени пользователя"""
        post = posts_dao.get_posts_by_user('leo')
        assert post['poster_name'] == 'leo', "При поиске постов возвращается неверное значение"

    def test_by_keyword(self, posts_dao):
        """Проверяет поиск постов по ключ-слову"""
        posts = posts_dao.search_posts_by_query('думаю')
        for post in posts:
            assert post['content'] == 'думаю', "При поиске постов возвращается неверное значение"
            assert set(post.keys()) == keys_should_be, "Ключи поста не сходятся с ожидаемыми"
