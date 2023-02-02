from flask import Blueprint

comments_blueprint = Blueprint('comments_blueprint', __name__)
PATH = 'data/comments.json'


@comments_blueprint.route('/comments/')
def index_comm_page():
    return 'Это страничка с комментариями'
