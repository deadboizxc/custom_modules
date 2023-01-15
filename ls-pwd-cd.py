import os
import shutil
import asyncio
from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix

@Client.on_message(filters.command('ls', prefixes=prefix) & filters.me)
async def list_file(client, message):
    path = os.getcwd()
    if os.path.exists(path):
        list = os.listdir()
        my_list  = ""
        for loc in list:
            if os.path.isdir(loc):
                my_list += "\n"
                my_list += "`"+loc+"/"+"`"
            else:
                my_list += "\n"
                my_list += "`"+loc+"`"
    await message.edit_text(
    f"""
    **File list for: {path}**
    {my_list}
    """)


# print('ФАЙЛ')
# print('Размер:', os.path.getsize(test_path) // 1024, 'Кб')
# print('Дата создания:',
#     datetime.datetime.fromtimestamp(
#         int(os.path.getctime(test_path))))
# print('Дата последнего открытия:',
#     datetime.datetime.fromtimestamp(
#         int(os.path.getatime(test_path))))
# print('Дата последнего изменения:',
#     datetime.datetime.fromtimestamp(
#         int(os.path.getmtime(test_path))))
# elif os.path.isdir(test_path):
#        print('КАТАЛОГ')
#        print('Список объектов в нем: ', os.listdir(test_path))
# else:
#    print('Объект не найден')



@Client.on_message(filters.command('pwd', prefixes=prefix) & filters.me)
async def pwd_to_file(client, message):
    path = os.getcwd()
    await message.edit_text(f"`{path}`")


@Client.on_message(filters.command('cd', prefixes=prefix) & filters.me)
async def cd_to_folder(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'

    if len(message.command) == 1:
        os.chdir("..")
        path = os.getcwd()
        if os.path.exists(path):
            os.chdir(os.path.expanduser(f"{path}"))
            list = os.listdir()
            my_list  = ""
            for loc in list:
                if os.path.isdir(loc):
                    my_list += "\n"
                    my_list += "`"+loc+"/"+"`"
                else:
                    my_list += "\n"
                    my_list += "`"+loc+"`"
    else:
        data = " ".join(message.command[1:])
        path = data.replace("/", "")
        if os.path.exists(path):
           os.chdir(os.path.expanduser(f"{path}"))
           path1 = os.getcwd()
           list = os.listdir()
           my_list  = ""
           for loc in list:
              if os.path.isdir(loc):
                  my_list += "\n"
                  my_list += "`"+loc+"/"+"`"
              else:
                  my_list += "\n"
                  my_list += "`"+loc+"`"

    await message.edit_text(
    f"""
    **File list for: {path1}\n**
    {my_list}
    """)


@Client.on_message(filters.command('home', prefixes=prefix) & filters.me)
async def cd_to_home(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    path = os.getcwd()
    data = "/data/data/com.termux/files/home"
    os.chdir(os.path.expanduser(f"{data}"))

    if os.path.exists(data):
        list = os.listdir()
        my_list  = ""
        for loc in list:
            if os.path.isdir(loc):
                my_list += "\n"
                my_list += "`"+loc+"/"+"`"
            else:
                my_list += "\n"
                my_list += "`"+loc+"`"

    await message.edit_text(
    f"""
    **File list for: {path}\n**
    {my_list}
    """)


@Client.on_message(filters.command('home0', prefixes=prefix) & filters.me)
async def cd_to_home(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    path = os.getcwd()
    data = "/storage/emulated/0/"
    os.chdir(os.path.expanduser(f"{data}"))

    if os.path.exists(data):
        list = os.listdir()
        my_list  = ""
        for loc in list:
            if os.path.isdir(loc):
                my_list += "\n"
                my_list += "`"+loc+"/"+"`"
            else:
                my_list += "\n"
                my_list += "`"+loc+"`"

    await message.edit_text(
    f"""
    **File list for: {path}\n**
    {my_list}
    """)


@Client.on_message(filters.command('touch', prefixes=prefix) & filters.me)
async def create_file(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    filename = " ".join(message.command[1:])
    path = os.getcwd()
    with open(filename, 'w') as f:
        pass
    await message.edit_text(
    f"""
    **Create new file: `{filename}\n`**
    """)


@Client.on_message(filters.command('rm', prefixes=prefix) & filters.me)
async def removed_file(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    name = " ".join(message.command[1:])
    path = os.getcwd()
    if os.path.isdir(name):
        shutil.rmtree(name, ignore_errors=True)
        await message.edit_text(
        f"""
        **Directory removed**
        """)
    else:
        os.remove(name)
        await message.edit_text(
        f"""
        **File removed**
        """)


@Client.on_message(filters.command('echo', prefixes=prefix) & filters.me)
async def echo_file(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    filename = message.text.split()[1]
    name = ""
    for loc1 in filename:
        name += loc1
    filedata = message.text.split()[2:]

    data = ""
    for loc2 in filedata:
      data += loc2
      data += " "

    path = os.getcwd()
    with open(name, 'w') as f:
       f.write(data)
    await message.edit_text(
    f"""
    **File `{name}` edited\n**
    """)


@Client.on_message(filters.command('cat', prefixes=prefix) & filters.me)
async def show_file(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    filename = " ".join(message.command[1:])
    path = os.getcwd()
    with open(filename, 'r') as f:
        data = f.read()
    await message.edit_text(
    f"""
    **File {filename}:\n**
    {data}
    """)


@Client.on_message(filters.command('mkdir', prefixes=prefix) & filters.me)
async def create_dir(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    path = os.getcwd()
    dirname = " ".join(message.command[1:])
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    await message.edit_text(
    f"""
    **Create new dir: `{path+"/"+dirname}\n`**
    """)


modules_help["ls-pwd-cd"] = {
    "ls": "[path] show contents in folder ",
    "pwd": "show path to dir",
    "cd": "[path] change dir",
    "home": "change dir to home directory",
    "home0": "change dir to .../storage/emulated/0/",
    "touch": "[file name] create empty file",
    "rm": "[file/dir name] remove file/dir",
    "echo": "[file name] edit file",
    "cat": "[file name] print file",
    "mkdir": "[dir name] make dir",
}
