from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix
import asyncio
import os
import requests


@Client.on_message(filters.command('ip', prefixes=prefix) & filters.me)
async def my_ip(client, message):
    ip = requests.get('http://ifconfig.me').text
    await message.edit_text(
f"""
<b>My Ip is: </b>
{ip}
"""
)


modules_help["my_id"] = {
    "ip": "send my ip",
}
