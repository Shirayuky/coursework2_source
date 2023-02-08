from flask import jsonify, Blueprint
from app.main.views import posts_dao

# from .utils import

api_blueprint = Blueprint('api_blueprint',
                          __name__)


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    return jsonify(posts_dao.pretty_print_json())  # Загрузка в формате json


@api_blueprint.route('/api/posts/<int:pk>', methods=['GET'])
def get_post_by_pk(pk):
    return jsonify(posts_dao.pretty_print_json_by_pk(pk))  # Вернет в формате json по пк
