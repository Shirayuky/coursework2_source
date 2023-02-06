from flask import Blueprint, render_template
from app.posts.dao import PostDAO
from typing import List

POST_DATA_PATH = '../../data/posts.json'
COMMENTS_DATA_PATH = '../../data/comments.json'

posts_blueprint = Blueprint('main_blueprint',
                            __name__,
                            template_folder='./templates')
posts_dao = PostDAO(POST_DATA_PATH, COMMENTS_DATA_PATH)


# @posts_blueprint.route('/posts/<pk>')
# def post_all_page():
#     """Вьюшка для всех постов"""
#     posts: List[dict] = posts_dao.get_all()
#     return render_template('post.html', posts=posts)
