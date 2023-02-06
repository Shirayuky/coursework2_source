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

        self.path = ''

    def __repr__(self):
        return f"Post(" \
               f"{self.pk}; " \
               f"{self.poster_name}; " \
               f"{self.poster_avatar}; " \
               f"{self.pic}; " \
               f"{self.content}; " \
               f"{self.views_count}; " \
               f"{self.likes_count}; " \
               f")"


class PostDAO(Posts):
    """
    Класс доступа к данным постов
    """

    def __init__(self, path):
        Posts.__init__(self, path)
        self.path = path

    def _load(self) -> List[dict]:
        """Загружает данные из JSON"""
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataErrorHandler(f"Не удается получить данные постов из файла {self.path}")
        return data

    def _load_post_of_list(self) -> List:
        """
        Загружает все посты в список
        return: Список экземпляров класса Post
        """
        posts_data = self._load()
        list_of_posts = [Posts(**posts) for posts in posts_data]  # '**posts' - аргументы в словарь
        return list_of_posts

    def get_all(self) -> List[dict]:
        """Получает все посты"""
        posts = self._load()
        return posts

    def get_by_pk(self, pk: int) -> dict:
        """Получает пост по его pk"""
        posts = self._load()
        for post in posts:
            if post['pk'] == pk:
                return post

    def search_by_query(self, search_word: str) -> List[dict]:
        """Ищет и получает посты по ключевому слову в контенте"""
        posts = self._load()
        found_posts = []
        for post in posts:
            if search_word.lower() in post['content'].lower():
                found_posts.append(post)
        return found_posts

    def get_posts_by_user(self, user_name: str) -> List[dict]:
        """Ищет и получает все посты искомого автора"""
        try:
            posts = self._load()
            author_posts = []
            for post in posts:
                if post['poster_name'].lower() == user_name.lower():
                    author_posts.append(post)
            return author_posts
        except ValueError:
            print(f"Пользователя с именем {user_name} нет в БД",
                  f"или {user_name} еще не опубликовал пост")


pd = PostDAO('../../data/posts.json')
pprint.pprint(pd.get_posts_by_user('leo'))
