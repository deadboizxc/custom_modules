from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix
import datetime
import asyncio
import os

#@Client.on_message(filters.command('sample', prefixes=prefix) & filters.me)
#async def sample(client, message):


@Client.on_message(filters.command('time', prefixes=prefix) & filters.me)
async def info(client, message):
    data = datetime.datetime.now().strftime("%Y-%m-%d"+" "+"%H:%M:%S")
    await message.edit_text(data)

@Client.on_message(filters.command('nud', prefixes=prefix) & filters.me)
async def nudes(client, message):
    await message.delete()
    DIR = "/data/data/com.termux/files/home/project/python/data/nudes"
    ff = os.path.join(DIR, random.choice(os.listdir(DIR)))
    photo = open(ff, 'rb')
    await client.send_photo(chat_id=message.chat.id, photo=photo)


@Client.on_message(filters.command("share_bot", prefixes=prefix) & filters.me)
async def share_bot(client, message):
    await message.delete()
    start_path = os.getcwd()
    os.chdir(os.path.expanduser('~/zxc-team/'))
    os.system("tar -cvf zxc-Userbot.tar.gz zxc-Userbot")
    await client.send_document(chat_id=message.chat.id, document="zxc-Userbot.tar.gz")
    os.remove("zxc-Userbot.tar.gz")
    os.chdir(start_path)

#### Coments ####

#@app.on_message(filters.command('spam_photo', prefixes=prefix) & filters.photo | filters.me)
   #async def spam(client, message):
   #await message.delete()
   #photo = message.photo.file_id
   #await client.send_photo(chat_id=message.chat.id, photo=photo)
   #for i in range(10):
       #await client.send_photo(chat_id=message.chat.id, photo=photo)

modules_help["other"] = {
    "time": "send time",
    "nud": "send nudes",
    "share_bot": "share bot .tar.gz archive",
}
