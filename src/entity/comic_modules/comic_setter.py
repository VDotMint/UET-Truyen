from src.entity.comic import *
from pyre_base import *


# Functions for setting basic comic info
class ComicSetters:
    @classmethod
    def increment_chapter_view_count(cls, comic_id, chapter_no):
        updated_view_count = Comic.list_of_comics[str(comic_id)]["chapters"][str(chapter_no)]["view_count"] + 1
        pyre_base.firebase.database().child("comics").child(str(comic_id)).child("chapters").child(
            str(chapter_no)).child("view_count").set(updated_view_count)
        Comic.update_local_comic_list()

    @classmethod
    def increment_comic_follower_count(cls, comic_id):
        updated_follower_count = Comic.list_of_comics[str(comic_id)]["follower_count"] + 1
        pyre_base.firebase.database().child("comics").child(str(comic_id)).child("follower_count").set(
            updated_follower_count)
        Comic.update_local_comic_list()
