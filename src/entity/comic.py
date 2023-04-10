"""_summary_
    """
import json
import os


class Comic:
    """
    Functions for interacting with the JSON file.
    """
    list_of_comics = dict()  # Static dictionary of the comics.

    # Loads the contents from the comic's JSON into memory.
    # YOU MUST ENSURE THAT THE FUNCTION HAS BEEN CALLED WHEN THE APP RUNS!
    @classmethod
    def load_comic_list(cls):
        with open(os.path.join(os.getcwd(), "assets/data/data.json"), mode="r", encoding="utf-8") as json_file:
            cls.list_of_comics = json.load(json_file)

    # Saving the comics list.
    @classmethod
    def save_comic_list(cls):
        with open(os.path.join(os.getcwd(), "assets/data/data.json"), mode="w", encoding="utf-8") as json_file:
            json.dump(cls.list_of_comics, json_file, indent=4, ensure_ascii=False)

    """
    Functions for retrieving basic comic info.
    """
    @classmethod
    def get_comic_name(cls, comic_id):
        return cls.list_of_comics[str(comic_id)]["name"]

    @classmethod
    def get_comic_aliases(cls, comic_id):
        return cls.list_of_comics[str(comic_id)]["aliases"]

    @classmethod
    def get_comic_view_count(cls, comic_id):
        return cls.list_of_comics[str(comic_id)]["view_count"]

    @classmethod
    def get_comic_type(cls, comic_id):
        return cls.list_of_comics[str(comic_id)]["type"]

    @classmethod
    def get_comic_follower_count(cls, comic_id):
        return cls.list_of_comics[str(comic_id)]["follower_count"]

    @classmethod
    def get_comic_content(cls, comic_id):
        content_file_path = "assets/data/" + str(comic_id) + "/content.txt"
        content_file = open(content_file_path, "r", encoding="utf-8")
        return content_file.read()

    @classmethod
    def get_comic_cover_img_path(cls, comic_id):
        return "assets/data/cover_img/" + str(comic_id) + ".jpg"

    @classmethod
    def get_comic_no_of_chapters(cls, comic_id):
        comic_path = os.path.join(os.getcwd(), "assets/data/" + str(comic_id))
        chapter_count = 0
        for chapters in os.listdir(comic_path):
            chapter_count += 1
        return chapter_count - 1

    """
    Functions for setting comic info.
    """
    @classmethod
    def increment_comic_view_count(cls, comic_id):
        cls.list_of_comics[str(comic_id)]["view_count"] += 1
        cls.save_comic_list()

    @classmethod
    def increment_comic_follower_count(cls, comic_id):
        cls.list_of_comics[str(comic_id)]["follower_count"] += 1
        cls.save_comic_list()

    """
    Functions for querying the stories in the JSON, matching certain criterias.
    """
    # Returning a list of Comic IDs whose types have an entry matching with that of the parameter.
    @classmethod
    def query_comics_of_category(cls, category_name):
        return [comic_id for comic_id in cls.list_of_comics if category_name in cls.list_of_comics[comic_id]["type"]]

    # Returning a list of Comic IDs whose names matches the search query.
    @classmethod
    def query_comics_of_author_name(cls, author_name):
        return [comic_id for comic_id in cls.list_of_comics if cls.list_of_comics[comic_id]["name"] == author_name]
