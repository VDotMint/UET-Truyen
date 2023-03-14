import json
import os


class Comic:
    list_of_comics = dict()

    def __init__(self, comic_name, comic_id, comic_type):
        self.comic_name = comic_name
        self.comic_id = comic_id
        self.comic_type = comic_type

    @classmethod
    def load_comic_list(cls):
        with open(os.path.join(os.getcwd(), "assets/data/data.json"), mode="r", encoding="utf-8") as json_file:
            cls.list_of_comics = json.load(json_file)

