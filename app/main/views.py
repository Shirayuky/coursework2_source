from flask import Blueprint, render_template
import pprint
from app.posts.views import posts_blueprint, posts_dao

main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='templates')


@main_blueprint.route('/')
def index_page():
    """Вьюшка главной странички"""
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)






# pprint.pprint(posts_dao.get_all())
