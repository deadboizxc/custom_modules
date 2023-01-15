import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix


@Client.on_message(filters.command("manul", prefix) & filters.me)
async def manul(client: Client, message: Message):
    count = int(message.command[1])
    await message.delete()

    for i in range(1, count + 1):
        await client.send_message(message.chat.id, f"{i} манула(ов)")
        await asyncio.sleep(0.2)


modules_help["manul"] = {
    "manul [amount]*": "Release manuls",
}
