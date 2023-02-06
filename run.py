from typing import List

from flask import Flask, render_template
from app.bookmarks.views import bookmarks_blueprint
from app.posts.comments.views import comments_blueprint
from app.posts.views import posts_blueprint

app = Flask(__name__,
            template_folder='templates')
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(comments_blueprint)
app.register_blueprint(posts_blueprint)


@app.route('/')
def index_page():
    posts: List[dict] = posts_blueprint.get_all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run()
