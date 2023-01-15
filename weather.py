from io import BytesIO

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.db import db
from utils.misc import modules_help, prefix
from utils.scripts import format_exc


@Client.on_message(filters.command(["weather", "w"], prefix) & filters.me)
async def weather(client: Client, message: Message):
    if len(message.command) == 1:
        city = db.get("custom.weather", "city", "Kherson")
    else:
        city = message.command[1]

    await message.edit(f"<b>Processing city {city}...</b>")

    try:
        text_resp = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=en")
        text_resp.raise_for_status()
        caption = f"```City: {text_resp.text}```"

        pic_resp = requests.get(f"http://wttr.in/{city}_2&lang=en.png")
        pic_resp.raise_for_status()
        pic = BytesIO(pic_resp.content)
        pic.name = f"{city}.png"

        await client.send_document(
            chat_id=message.chat.id, document=pic, caption=caption
        )
        await message.delete()
    except Exception as e:
        await message.edit(format_exc(e))


@Client.on_message(filters.command(["set_weather_city", "swcity"], prefix) & filters.me)
async def set_weather_city(_, message: Message):
    if len(message.command) == 1:
        return await message.edit("<b>City name isn't provided</b>")

    db.set("custom.weather", "city", message.command[1])
    await message.edit(f"<b>City {message.command[1]} set!</b>")


modules_help["weather"] = {
    "weather [city]*": "Get weather for selected city or chosen in set_weather_city",
    "set_weather_city [city]*": f"Set city for {prefix}weather command, Moscow by default",
}
