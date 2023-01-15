from pyrogram import *
from pyrogram.types import Message
from utils.misc import prefix
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
from time import *
import random
import asyncio

@Client.on_message(filters.command('hack', prefixes=prefix) & filters.me)
async def hack(client, message):
        perc = 0
        while(perc < 100):
                try:
                        text = "👮 Взлом пентагона в процессе ..." + str(perc) + "%"
                        await message.edit_text(text)
                        perc += random.randint(1, 3)
                        sleep(0.1)
                except FloodWait as e:
                        sleep(e.x)
        await message.edit_text("🟢 Пентагон успешно взломан!")
        sleep(3)
        message.edit("👽 Поиск секретных данных об НЛО ...")
        perc = 0

        while(perc < 100):
                try:
                        text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
                        await message.edit_text(text)
                        perc += random.randint(1, 5)
                        sleep(0.15)
                except FloodWait as e:
                        sleep(e.x)
        await message.edit_text("🦖 Найдены данные о существовании динозавров на земле!")
