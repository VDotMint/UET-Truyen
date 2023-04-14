from src.entity.comic import *
import os

# Functions for retrieving basic comic info.
class ComicGetters:
    @classmethod
    def get_comic_name(cls, comic_id):
        return Comic.list_of_comics[str(comic_id)]["name"]

    @classmethod
    def get_comic_aliases(cls, comic_id):
        return Comic.list_of_comics[str(comic_id)]["aliases"]

    @classmethod
    def get_comic_view_count(cls, comic_id):
        return Comic.list_of_comics[str(comic_id)]["view_count"]

    @classmethod
    def get_comic_type(cls, comic_id):
        return Comic.list_of_comics[str(comic_id)]["type"]

    @classmethod
    def get_comic_follower_count(cls, comic_id):
        return Comic.list_of_comics[str(comic_id)]["follower_count"]

    @classmethod
    def get_comic_content(cls, comic_id):
        return Comic.list_of_comics[str(comic_id)]["content"]

    @classmethod
    def get_comic_chapter_count(cls, comic_id):
        return Comic.list_of_comics[str(comic_id)]["chapter_count"]

    # @classmethod
    # def get_comic_cover_img_path(cls, comic_id):
    #     return "assets/data/cover_img/" + str(comic_id) + ".jpg"
