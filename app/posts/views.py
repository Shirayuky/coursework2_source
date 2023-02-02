from flask import Blueprint, render_template
from .dao import PostsDao
from typing import List

posts_dao = PostsDao()
posts_blueprint = Blueprint('posts_blueprint',
                            __name__,
                            template_folder='templates')


@posts_blueprint.route('/posts/')
def post_all_page():
    """Вьюшка для всех постов"""
    posts: List[dict] = posts_dao.get_all()
    return render_template('')
