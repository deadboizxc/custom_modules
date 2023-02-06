from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix
import asyncio
import os
import requests
import json
import jmespath

@Client.on_message(filters.command('map', prefixes=prefix) & filters.me)
async def sample(client, message):
    url2 = "https://api.alerts.in.ua/v2/alerts/active.json"
    res = requests.get(url2)
    alerts = res.json()
    text  = ""

    for loc in alerts["alerts"]:
        text += "\n"
        text += "🔴 "+loc["n"]

    await message.edit_text(
f"""<b>‼Повітряна тривога в таких місцях:</b>
<b>{text}</b>
""")


modules_help["map"] = {
    "map": "send an air alert map",
}
