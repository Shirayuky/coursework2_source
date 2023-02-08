import json
from app.main.views import post_data_path

class PostsAPI:
    def __init__(self, post_data_path):
        self.post_data_path = post_data_path

