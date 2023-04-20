import math
import time
import random
from src.entity.comic import *
from src.entity.comic_modules.comic_getter import ComicGetters


class ComicRanking:
    # Return the top-n ranking for story view count in a week, including ID and shortened view count.
    # Set with_view_count parameter to true for just the ID list.
    @classmethod
    def get_view_count_ranking_by_time(cls, time_interval, top_how_many=10, with_view_count=True):
        if time_interval == "monthly":
            random_division_coefficient = 1000
            random.seed(int(time.time() / 2592000))
        elif time_interval == "weekly":
            random_division_coefficient = 10000
            random.seed(int(time.time() / 604800))
        elif time_interval == "daily":
            random_division_coefficient = 100000
            random.seed(int(time.time() / 86400))
        else:
            print("Invalid time interval chosen")
            return []

        # Establishing a list of pairs of ID and view count, randomizing how much views it had in the week
        comic_view_count_pairs = []
        for comic in Comic.list_of_comics:
            comic_view_count_pairs.append(
                [
                    comic,
                    int(ComicGetters.get_comic_view_count(comic) *
                        (random.uniform(0, 20) / random_division_coefficient))
                ]
            )

        # Sort that list in descending order of the view count
        list_sorted_by_count = sorted(comic_view_count_pairs, key=lambda listo: listo[1], reverse=True)

        if with_view_count:
            # Convert the view count to a shortened format
            for stuff in list_sorted_by_count:
                stuff[1] = convert_to_shortened_number(stuff[1])

            if len(list_sorted_by_count) > top_how_many:
                return list_sorted_by_count[:top_how_many]
            return list_sorted_by_count
        else:
            return [index[0] for index in list_sorted_by_count]


def convert_to_shortened_number(number):
    number_length = len(str(number))
    if number_length > 9:
        return "Too many views"
    elif number_length <= 3:
        return str(number)
    elif 3 < number_length < 6:
        return str(round(number / 1000, 6 - number_length)) + "K"
    elif number_length == 6:
        return str(int(math.ceil(number / 1000))) + "K"
    elif 6 < number_length < 9:
        return str(round(number / 1000000, 9 - number_length)) + "M"
    elif number_length == 9:
        return str(int(math.ceil(number / 1000000))) + "M"
