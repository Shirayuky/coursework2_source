from flask import jsonify, Blueprint
from app.main.views import posts_dao
import logging

api_blueprint = Blueprint('api_blueprint',
                          __name__)
logging.basicConfig(filename='./logs/basic.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info(f"Запрос /api/posts/")
    return jsonify(posts_dao.load_data_for_jsonfy())  # Загрузка в формате json


@api_blueprint.route('/api/posts/<int:pk>', methods=['GET'])
def get_post_by_pk(pk):
    return jsonify(posts_dao.get_by_pk_for_jsonfy(pk))  # Вернет в формате json по пк
