from src.entity.comic import *


# Functions for querying and searching the comic database
class ComicQuery:
    # Returning a list of Comic IDs whose types have an entry matching with that of the parameter.
    @classmethod
    def query_comics_of_category(cls, category_name):
        return [comic_id for comic_id in Comic.list_of_comics
                if category_name in Comic.list_of_comics[comic_id]["type"]]

    # Returning a list of Comic IDs whose names matches the search query.
    @classmethod
    def query_comics_of_author_name(cls, author_name):
        return [comic_id for comic_id in Comic.list_of_comics
                if Comic.list_of_comics[comic_id]["name"] == author_name]
