from src.entity.comic import Comic
from image_kit_module import *


class ComicImageModule:
    # Returns the ImageKit link to the cover image of the comic ID.
    @classmethod
    def get_comic_cover_img_link(cls, comic_id):
        img_link = "https://ik.imagekit.io/tf178401v/cover_img/" + str(comic_id) + ".jpg"
        return img_link

    # Returns a list of all the images
    @classmethod
    def get_comic_content_images(cls, comic_id, comic_chapter):
        search_path = "/" + str(comic_id) + "/" + str(comic_chapter) + "/"
        search_options = ListAndSearchFileRequestOptions(
            path=search_path
        )

        result = imagekit.list_files(options=search_options)
        sorted_list = [links.url for links in result.list]
        sorted_list.sort()
        return sorted_list
