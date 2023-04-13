import pyre_base


class Comic:
    # Function for interacting with JSON files.

    list_of_comics = dict()  # Static dictionary of the comics.

    # Loads the contents from the comic's JSON into memory.
    # YOU MUST ENSURE THAT THIS FUNCTION HAS BEEN CALLED WHEN THE APP RUNS!
    @classmethod
    def load_comic_list(cls):
        pyre_base.sign_in("21020649@vnu.edu.vn", "DummyPassword169!")
        cls.update_local_comic_list()

    @classmethod
    def update_local_comic_list(cls):
        cls.list_of_comics = dict(pyre_base.firebase.database().child("comics").get().val())

    # Saving the comics list.
    # @classmethod
    # def save_comic_list(cls):
    #     with open(os.path.join(os.getcwd(), "assets/data/data.json"), mode="w", encoding="utf-8") as json_file:
    #         json.dump(cls.list_of_comics, json_file, indent=4, ensure_ascii=False)
