from flask import Flask
from app.bookmarks.views import bookmarks_blueprint
from app.comments.views import comments_blueprint
from app.posts.views import posts_blueprint

app = Flask(__name__)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(comments_blueprint)
app.register_blueprint(posts_blueprint)


@app.route('/')
def index_page():
    return 'Это главная страничка'


if __name__ == '__main__':
    app.run()
