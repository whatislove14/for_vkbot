import json
import os


@bl.message(text=["!reg"])
async def register(message: Message):
    if message.from_id in ignore_user:
        pass
    else:
        # Пустой список участников
        empty_members = {'5': [],
                         '4': [], '3': [],
                         '2': [], '1': [],
                         '0': []}
        # создание пустого json
        my_dir = "D:\\Desktop"  # путь до папки со всеми json
        if str(message.chat_id)+".json" not in os.listdir(my_dir):
            with open(str(message.chat_id)+".json", "w") as f:
                json.dump(empty_members, f)


@bl.message(text=["!main_admin"])
async def set_me_main_admin(message: Message):
    if message.from_id in ignore_user:
        pass
    else:
        # добавление автора сообщения в создатели
        with open(str(message.chat_id)+".json", "r") as f:
            data = json.load(f)
            data["5"].append(message.from_id)

        my_dir = "D:\\Desktop"  # путь до папки со всеми json
        if str(message.chat_id)+".json" in os.listdir(my_dir):
            with open(str(message.chat_id)+".json", "w") as f:
                json.dump(data, f)


@bl.message(text=["!sec_main_admin"])
async def set_me_sec_main_admin(message: Message):
    if message.from_id in ignore_user:
        pass
    else:
        # добавление автора сообщения в заместителя создателя
        with open(str(message.chat_id)+".json", "r") as f:
            data = json.load(f)
            data["4"].append(message.from_id)

        my_dir = "D:\\Desktop"  # путь до папки со всеми json
        if str(message.chat_id)+".json" in os.listdir(my_dir):
            with open(str(message.chat_id)+".json", "w") as f:
                json.dump(data, f)


@bl.message(text=["!moder"])
async def set_me_moderator(message: Message):
    if message.from_id in ignore_user:
        pass
    else:
        # добавление автора сообщения в заместителя создателя
        with open(str(message.chat_id)+".json", "r") as f:
            data = json.load(f)
            data["3"].append(message.from_id)

        my_dir = "D:\\Desktop"  # путь до папки со всеми json
        if str(message.chat_id)+".json" in os.listdir(my_dir):
            with open(str(message.chat_id)+".json", "w") as f:
                json.dump(data, f)


@bl.message(text=["!main_helper"])
async def set_me_sejor_helper(message: Message):
    if message.from_id in ignore_user:
        pass
    else:
        # добавление автора сообщения в заместителя создателя
        with open(str(message.chat_id)+".json", "r") as f:
            data = json.load(f)
            data["2"].append(message.from_id)

        my_dir = "D:\\Desktop"  # путь до папки со всеми json
        if str(message.chat_id)+".json" in os.listdir(my_dir):
            with open(str(message.chat_id)+".json", "w") as f:
                json.dump(data, f)


@bl.message(text=["!helper"])
async def set_me_helper(message: Message):
    if message.from_id in ignore_user:
        pass
    else:
        # добавление автора сообщения в заместителя создателя
        with open(str(message.chat_id)+".json", "r") as f:
            data = json.load(f)
            data["1"].append(message.from_id)

        my_dir = "D:\\Desktop"  # путь до папки со всеми json
        if str(message.chat_id)+".json" in os.listdir(my_dir):
            with open(str(message.chat_id)+".json", "w") as f:
                json.dump(data, f)
