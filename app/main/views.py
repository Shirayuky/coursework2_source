from typing import List

from flask import Blueprint, render_template, request
import pprint
from app.posts.dao import PostDAO
from app.comments.dao import CommentsDAO

post_data_path = 'data/posts.json'
comments_data_path = 'data/comments.json'

main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='templates',
                           static_folder='/static',
                           static_url_path='/static')
posts_dao = PostDAO(post_data_path)
comments_dao = CommentsDAO(comments_data_path)


@main_blueprint.route('/')
def index_page():
    """Вьюшка главной странички"""
    posts: List[dict] = posts_dao.get_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/post/<int:pk>/')
def post_and_comments_page(pk):
    """Вьюшка для постов и комментов с поиском по пк"""
    post: dict = posts_dao.get_by_pk(pk)
    comments: List[dict] = comments_dao.get_by_post_pk(pk)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    """Вьюшка для поиска по ключевому слову"""
    query = request.args.get('s')
    print(query)
    posts: List[dict] = posts_dao.search_by_query(query)
    # pprint.pprint(posts)
    return render_template('search.html', posts=posts, substr=query)


@main_blueprint.route('/users/<username>', methods=['GET'])
def search_username_page(username):
    """Вьюшка для поиска пользователей"""
    user_posts: List[dict] = posts_dao.get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts, username=username)

# search_page('leo')
