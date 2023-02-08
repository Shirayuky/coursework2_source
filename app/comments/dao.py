import json
import pprint
from json import JSONDecodeError
from exceptions import DataErrorHandler
from typing import List


class Comments:
    """
    Абстракция комментариев для DAO
    """

    def __init__(self,
                 post_id=0,
                 commenter_name='',
                 comment='',
                 pk=0):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk

        self.comment_path = ''

    def __repr__(self):
        return f"Post()\n" \
               f"pk: {self.pk}" \
               f"Name: {self.commenter_name}\n"


class CommentsDAO(Comments):
    """
    Менеджер комментариев:
    1. загрузка
    2. get_by_post_pk()
    """

    def __init__(self, comments_path):
        Comments.__init__(self, comments_path)
        self.comments_path = comments_path

    def _load(self) -> List[dict]:
        """Загружает данные из JSON"""
        try:
            with open(self.comments_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataErrorHandler(f"Не удается получить комментарии  из файла {self.comment_path}")
        return data

    def get_by_post_pk(self, post_id: int):
        """Получает комментарий по его post_id"""
        try:
            comments = self._load()
            comments_list = []
            for comment in comments:
                if comment['post_id'] == post_id:
                    comments_list.append(comment)
            return comments_list
        except ValueError:
            print(f"Ошибки (и/или):\n"
                  f"1) {post_id} - не число\n"
                  f"2) ПК со значением: {post_id} отсутствует в БД")



# c = CommentsDAO('../../data/comments.json')
# pprint.pprint(c.get_by_post_pk(1))
