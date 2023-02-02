import json
from typing import List


class PostsDao:
    def __int__(self, path):
        self.path = 'data/posts.json'

    def load_data(self) -> List[dict]:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def get_all(self) -> List[dict]:
        posts = self.load_data()
        return posts

    def get_posts_by_user(self, poster_name) -> dict:
        try:
            posts = self.load_data()
            for post in posts:
                if post['poster_name'] == poster_name:
                    return post
        except ValueError:
            print(f'Пользователя с именем {poster_name} нет в БД или {poster_name} еще не опубликовал пост')

    def get_post_by_pk(self, pk) -> dict:
        posts = self.load_data()
        for post in posts:
            if post['pk'] == pk:
                return post

    def search_posts_by_query(self, search_word) -> List[dict]:
        posts = self.load_data()
        found_posts = []
        for post in posts:
            if search_word in post['content']:
                found_posts.append(post)

        return found_posts
