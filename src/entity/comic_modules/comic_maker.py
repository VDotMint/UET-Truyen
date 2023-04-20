from src.entity.comic import Comic
from src.entity.comic_modules.comic_getter import ComicGetters
from datetime import datetime
from image_kit_module import *
import base64
import pyre_base


class ComicMaker:
    @classmethod
    def create_new_comic(cls,
                         comic_name,
                         comic_cover_img_path,
                         comic_author="Đang cập nhật",
                         comic_aliases=None,
                         comic_content="(rỗng)",
                         comic_type=None):
        if comic_aliases is None:
            comic_aliases = ["Không có"]
        if comic_type is None:
            comic_type = ["Không có"]

        # Finding the largest comic ID:
        comic_key_list = [int(comic_key) for comic_key in list(Comic.list_of_comics.keys())]
        new_comic_key = max(comic_key_list) + 1

        # Creating a new entry for the Comics database
        new_comic = {
            "name": comic_name,
            "aliases": comic_aliases,
            "status": "Đang tiến hành",
            "type": comic_type,
            "content": comic_content,
            "view_count": 0,
            "last_updated": datetime.now().isoformat()[:-7],
            "follower_count": 0,
            "chapter_count": 0
        }

        # Uploading the Comic cover image
        with(open(file=comic_cover_img_path, mode="rb")) as cover_img:
            cover_img_str = base64.b64encode(cover_img.read())

        if comic_cover_img_path[-3:] == "jpg":
            new_cover_image_filename = str(new_comic_key) + ".jpg"
        elif comic_cover_img_path[-3:] == "png":
            new_cover_image_filename = str(new_comic_key) + ".png"
        else:
            return "Unsupported image type for the comic cover!"

        imagekit.upload(
            file=cover_img_str,
            file_name=new_cover_image_filename,
            options=UploadFileRequestOptions(
                folder='cover_img',
                use_unique_file_name=False
            )
        )
        print("Uploaded comic cover!")

        # Establishing the new entry on Firebase
        admin = pyre_base.sign_in("21020649@vnu.edu.vn", "DummyPassword169!")
        pyre_base.firebase.database().child("comics").child(str(new_comic_key)).set(new_comic, admin['idToken'])
        print("Comic id " + str(new_comic_key) + " is on Firebase")

        Comic.update_local_comic_list()

        return "Comic id " + str(new_comic_key) + ": " + comic_name + " successfully uploaded!"

    @classmethod
    def upload_new_comic_chapter(cls, comic_id, list_of_chapter_pic_links):
        current_newest_chapter = ComicGetters.get_comic_chapter_count(str(comic_id))
        new_chapter_count = current_newest_chapter + 1

        # Check to see if any files are not JPEG or PNG
        for link in list_of_chapter_pic_links:
            if link[-3:] not in [".png", ".jpg"]:
                return "Unsupported image type!"

        index = 1
        # Upload the images to ImageKit.IO
        for link in list_of_chapter_pic_links:
            with open(file=link, mode="rb") as img:
                imgstr = base64.b64encode(img.read())
            destination_folder = str(comic_id) + "/" + str(new_chapter_count) + "/"

            if link[-3:] == "jpg":
                upload_filename_name = str(index).zfill(3) + ".jpg"
            else:
                upload_filename_name = str(index).zfill(3) + ".png"

            imagekit.upload(
                file=imgstr,
                file_name=upload_filename_name,
                options=UploadFileRequestOptions(
                    folder=destination_folder,
                    use_unique_file_name=False
                )
            )

            print("Picture", index)
            index += 1

        # Update the chapter data on Firebase
        admin = pyre_base.sign_in("21020649@vnu.edu.vn", "DummyPassword169!")
        pyre_base.firebase.database().child("comics").child(str(comic_id)).child("chapters").child(
            str(new_chapter_count)).child("view_count").set(0, admin['idToken'])
        pyre_base.firebase.database().child("comics").child(str(comic_id)).child("chapters").child(
            str(new_chapter_count)).child("publish_date").set(datetime.now().isoformat()[:-7], admin['idToken'])

        return "Upload success!"
