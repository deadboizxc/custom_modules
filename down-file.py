from pyrogram import *
from pyrogram.types import Message
from utils.misc import prefix
import asyncio
import os

@Client.on_message(filters.command('down', prefixes=prefix) & filters.me)
async def down_file(client, message):
    MAIN_BOT_DIR = '/data/data/com.termux/files/home/zxc-Userbot'
    if message.reply_to_message.document:
        if len(message.command) == 1:
            await message.delete()
            start_path = os.getcwd()
            os.chdir(os.path.expanduser(bot_dir))
            file = message.reply_to_message.document.file_id
            await client.download_media(file)
            await message.reply_text(f"**File saved to: `{MAIN_BOT_DIR}downloads`**")
            os.chdir(start_path)
        else:
            data = " ".join(message.command[1:])
            await message.delete()
            start_path = os.getcwd()
            path = data.replace("/", "")
            if os.path.exists(path):
                os.chdir(os.path.expanduser(f"{path}"))
                file = message.reply_to_message.document.file_id
                await client.download_media(file)
                await message.reply_text(f"**File saved to: `{path}`**")
                os.chdir(start_path)
            else:
                pass

    elif message.reply_to_message.audio:
        if len(message.command) == 1:
            await message.delete()
            start_path = os.getcwd()
            os.chdir(os.path.expanduser(bot_dir))
            file = message.reply_to_message.audio.file_id
            await client.download_media(file)
            await message.reply_text(f"**File saved to: `{MAIN_BOT_DIR}downloads`**")
            os.chdir(start_path)
        else:
            data = " ".join(message.command[1:])
            await message.delete()
            start_path = os.getcwd()
            path = data.replace("/", "")
            if os.path.exists(path):
                os.chdir(os.path.expanduser(f"{path}"))
                file = message.reply_to_message.audio.file_id
                await client.download_media(file)
                await message.reply_text(f"**File saved to: `{path}`**")
                os.chdir(start_path)
            else:
                pass

    elif message.reply_to_message.video:
        if len(message.command) == 1:
            await message.delete()
            start_path = os.getcwd()
            os.chdir(os.path.expanduser(bot_dir))
            file = message.reply_to_message.video.file_id
            await client.download_media(file)
            await message.reply_text(f"**File saved to: `{MAIN_BOT_DIR}downloads`**")
            os.chdir(start_path)
        else:
            data = " ".join(message.command[1:])
            await message.delete()
            start_path = os.getcwd()
            path = data.replace("/", "")
            if os.path.exists(path):
                os.chdir(os.path.expanduser(f"{path}"))
                file = message.reply_to_message.video.file_id
                await client.download_media(file)
                await message.reply_text(f"**File saved to: `{path}`**")
                os.chdir(start_path)
            else:
                pass

    elif message.reply_to_message.photo:
        if len(message.command) == 1:
            await message.delete()
            start_path = os.getcwd()
            os.chdir(os.path.expanduser(bot_dir))
            file = message.reply_to_message.photo.file_id
            await client.download_media(file)
            await message.reply_text(f"**File saved to: `{MAIN_BOT_DIR}downloads`**")
            os.chdir(start_path)
        else:
            data = " ".join(message.command[1:])
            await message.delete()
            start_path = os.getcwd()
            path = data.replace("/", "")
            if os.path.exists(path):
                os.chdir(os.path.expanduser(f"{path}"))
                file = message.reply_to_message.photo.file_id
                await client.download_media(file)
                await message.reply_text(f"**File saved to: `{path}`**")
                os.chdir(start_path)
            else:
                pass

    else:
        pass
