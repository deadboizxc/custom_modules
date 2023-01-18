from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix
import pathlib
import asyncio
import os


@Client.on_message(filters.command("send", prefixes=prefix) & filters.me)
async def cmd_(client, message):
    await message.delete()

    files = message.text.split(maxsplit=2)[2]
    types = message.text.split(maxsplit=2)[1]

    documents = [".py", ".txt", ".sh"]
    audios =[".mp3", ".m4a", ".opus", ".aac"]
    photos = [".jpg", "jpeg", ".png"]
    videos = [".mp4", ".avi"]
    suff = pathlib.Path(files).suffix

    for document in documents:
        if suff == document:
            await client.send_document(chat_id=message.chat.id, document=files)
        else:
            pass

    for audio in audios:
        if suff == audio:
            await client.send_audio(chat_id=message.chat.id, audio=files)
        else:
            pass

    for photo in photos:
        if suff == photo:
            await client.send_photo(chat_id=message.chat.id, photo=files)
        else:
            pass

    for video in videos:
        if suff == photo:
            await client.send_video(chat_id=message.chat.id, video=files)
        else:
            pass


@Client.on_message(filters.command("send", prefixes=prefix) & filters.me)
async def cmd_(client, message):
    await message.delete()

    files = message.text.split(maxsplit=2)[2]
    types = message.text.split(maxsplit=2)[1]


    if types == "aud":
        await client.send_audio(chat_id=message.chat.id, audio=files)
    else:
        pass

    if types == "doc":
        await client.send_document(chat_id=message.chat.id, document=files)
    else:
        pass

    if types == "photo":
        await client.send_photo(chat_id=message.chat.id, photo=files)
    else:
        pass

    if types == "vid":
         await client.send_video(chat_id=message.chat.id, video=files)
    else:
         pass


modules_help["send"] = {
    "send": ".send [local file name] or .send [types] [file id]",
}
