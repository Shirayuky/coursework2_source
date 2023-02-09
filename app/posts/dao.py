import json
import pprint
from json import JSONDecodeError
from exceptions import DataErrorHandler
from typing import List


class Posts:
    """
    Абстракция постов для DAO
    """

    def __init__(self,
                 poster_name='',
                 poster_avatar='',
                 pic='',
                 content='',
                 views_count=0,
                 likes_count=0,
                 pk=0):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

        self.post_path = ''

    def __repr__(self):
        return f"Post()\n" \
               f"pk: {self.pk}" \
               f"Name: {self.poster_name}\n"


class PostDAO(Posts):
    """
    Менеджер постов:
    1. загрузка
    2. get_all()
    3. get_by_pk(pk)
    4. search_by_query(search_word)
    5. get_posts_by_user(user_name)
    """

    def __init__(self, post_path):
        Posts.__init__(self, post_path)
        self.post_path = post_path

    def load_data(self) -> List[dict]:
        """Загружает данные из JSON"""
        try:
            with open(self.post_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataErrorHandler(f"Не удается получить данные постов из файла {self.post_path}")
        return data

    def _load_post_of_list(self) -> List:
        """
        Загружает все посты в список
        return: Список экземпляров класса Post
        """
        posts_data = self.load_data()
        list_of_posts = [Posts(**posts) for posts in posts_data]  # '**posts' - аргументы в словарь (без форматирования)
        return list_of_posts

    def load_data_for_jsonfy(self) -> List[dict]:
        """Загружает данные из JSON"""
        with open(self.post_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all(self) -> List[dict]:
        """Получает все посты"""
        posts = self.load_data()
        return posts

    def get_by_pk(self, pk: int) -> dict:
        """Получает пост по его pk"""
        try:
            posts = self.load_data()
            for post in posts:
                if post['pk'] == pk:
                    return post
        except ValueError:
            print(f"Ошибки (и/или):\n"
                  f"1) {pk} - не число\n"
                  f"2) ПК со значением: {pk} отсутствует в БД")

    def get_by_pk_for_jsonfy(self, pk: int) -> dict:
        """Получает пост по его pk"""
        try:
            posts = self.load_data_for_jsonfy()
            for post in posts:
                if post['pk'] == pk:
                    return post
        except ValueError:
            print(f"Ошибки (и/или):\n"
                  f"1) {pk} - не число\n"
                  f"2) ПК со значением: {pk} отсутствует в БД")

    def search_by_query(self, search_word: str) -> List[dict]:
        """Ищет и получает посты по ключевому слову в контенте"""
        try:
            posts = self.load_data()
            found_posts = []
            for post in posts:
                if search_word.lower() in post['content'].lower():
                    found_posts.append(post)
            return found_posts
        except ValueError:
            print(f"Ошибки (и/или):\n"
                  f"1) В ключевом слове {search_word} ошибка\n"
                  f"2) Ключевого слова {search_word} нет ни в одном из контекстов")

    def get_posts_by_user(self, user_name: str) -> List[dict]:
        """Ищет и получает все посты искомого автора"""
        try:
            posts = self.load_data()
            author_posts = []
            for post in posts:
                if post['poster_name'].lower() == user_name.lower():
                    author_posts.append(post)
            return author_posts
        except ValueError:
            print(f"Ошибки (и/или):\n"
                  f"1) Пользователя с именем {user_name} нет в БД\n"
                  f"2) {user_name} еще не опубликовал пост")

# p = PostDAO("../../data/posts.json")
# pprint.pprint(p.get_all())
