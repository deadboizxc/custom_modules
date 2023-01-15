import asyncio

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix
from utils.scripts import format_exc
import nekos
from nekos import ENDPOINTS

@Client.on_message(filters.command("neko", prefix) & filters.me)
async def neko(client, message: Message):
    if len(message.command) == 1:
        await message.edit(
            "<b>neko type isn't provided\n"
            f"You can get available neko types with <code>{prefix}neko_types</code></b>"
        )

    query = message.command[1]
    type = message.command[2]

    await message.edit("<b>Loading...</b>")
    try:
        if type == "pic":
            await client.send_photo(chat_id=message.chat.id, photo=f"{nekos.get_neko(query)}")
        elif type == "doc":
            await client.send_document(chat_id=message.chat.id, document=f"{nekos.get_neko(query)}")
    except Exception as e:
        await message.edit(format_exc(e))


@Client.on_message(filters.command(["nekotypes", "neko_types"], prefix) & filters.me)
async def neko_types_func(client, message: Message):
    n = [el[0] for el in ENDPOINTS]
    dil = ' '
    single_str = dil.join(n)
    nekos_types = '{0}'.format(single_str)

    await message.edit(" ".join(f"<code>{n}</code>" for n in nekos_types.split()))


@Client.on_message(filters.command(["nekospam", "neko_spam"], prefix) & filters.me)
async def neko_spam(client: Client, message: Message):
    query = message.command[1]
    amount = int(message.command[2])
    type = message.command[3]

    await message.delete()

    for _ in range(amount):
        if message.reply_to_message:
            await message.reply_to_message.reply(nekos.get_neko(query))
        else:
            if type == "pic":
                await client.send_photo(chat_id=message.chat.id, photo=f"{nekos.get_neko(query)}")
            elif type == "doc":
                await client.send_document(chat_id=message.chat.id, document=f"{nekos.get_neko(query)}")


modules_help["neko"] = {
    "neko [type]*": "Get neko media",
    "neko_types": "Available neko types",
    "neko_spam [type]* [amount]*": "Start spam with neko media",
}
