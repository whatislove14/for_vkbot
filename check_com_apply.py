import json
import os

com_main_admin = ["!ban"]
com_sec_main_admin = ["!ban"]
com_moder = ["!ban"]
com_senjor_helper = ["!ban"]
com_helper = []


def check_apply(com, user_id, chat_id):
    if com.from_id in ignore_user:
        pass
    else:
        my_dir = "D:\\Desktop"  # путь до папки со всеми json
        if str(chat_id)+".json" in os.listdir(my_dir):
            with open(str(chat_id)+".json", "r") as f:
                data = json.load(f)
            if user_id in data["5"]:
                return com in com_main_admin
            if user_id in data["4"]:
                return com in com_sec_main_admin
            if user_id in data["3"]:
                return com in com_moder
            if user_id in data["2"]:
                return com in com_senjor_helper
            if user_id in data["1"]:
                return com in com_helper
