from flask import Blueprint

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__)
PATH = 'data/bookmarks.json'


@bookmarks_blueprint.route('/bookmarks/')
def index_bkmarks_page():
    return 'Страничка с закладками'
