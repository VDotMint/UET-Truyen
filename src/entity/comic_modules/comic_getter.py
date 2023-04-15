from src.entity.comic import *
from datetime import datetime
from datetime import timedelta

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

    @classmethod
    def get_comic_last_updated_date(cls, comic_id):
        return datetime.fromisoformat(Comic.list_of_comics[str(comic_id)]["last_updated"])

    @classmethod
    def get_comic_last_updated_delta(cls, comic_id):
        comic_latest_time = datetime.fromisoformat(Comic.list_of_comics[str(comic_id)]["last_updated"])

        td_d = timedelta(days=1)
        td_h = timedelta(hours=1)
        td_m = timedelta(minutes=1)
        td = datetime.now() - comic_latest_time

        dmh_list = [td.days, (td % td_d) // td_h, (td % td_h) // td_m]

        if dmh_list[0] > 0:
            return str(dmh_list[0]) + " days ago"
        elif dmh_list[1] > 0:
            return str(dmh_list[1]) + " hours ago"
        elif dmh_list[2] > 0:
            return str(dmh_list[2]) + " minutes ago"
        else:
            return "Just now"

