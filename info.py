from pyrogram import *
from pyrogram.types import Message
from utils.misc import prefix
import asyncio

@Client.on_message(filters.command('me', prefixes=prefix) & filters.me)
async def info_me(client, message):
    me = await client.get_me()
#   await message.edit_text(me)
    await message.edit(

f"""
┌─**INFO**
├**First Name:** `{me.first_name}`
├**Last Name:** `{me.last_name}`
├**Username:** `@{me.username}`
├**ID:** `{me.id}`
├**Next Offline Date:**
│   `{me.next_offline_date}`
│
└**Photo ID:**
     `{me.photo.small_file_id}`


     `{me.photo.big_photo_unique_id}`

"""
)


@Client.on_message(filters.command('chat', prefixes=prefix) & filters.me)
async def info_chat(client, message):
    chat = await client.get_chat(chat_id=message.chat.id)
    await message.edit(

f"""
┌─**INFO**
├**First Name:** `{chat.first_name}`
├**Last Name:** `{chat.last_name}`
├**Username:** `@{chat.username}`
├**Type:** {chat.type}
├**Title:** `{chat.title}`
├**Invite Link**: `{chat.invite_link}`
├**Description**: {chat.description}
├**ID:** `{chat.id}`
├**Bio:** {chat.bio}
└**Photo ID:**
    `{chat.photo.small_file_id}`


    `{chat.photo.big_photo_unique_id}`

"""
)

#`{chat.photo.small_file_id}`
#`{chat.photo.big_photo_unique_id}`


@Client.on_message(filters.command('user', prefixes=prefix))
async def info_user(client, message):
    chat = await client.get_chat(chat_id=message.reply_to_message.from_user.id)
    if message.reply_to_message:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌─**INFO**
├**First Name:** `{chat.first_name}`
├**Last Name:** `{chat.last_name}`
├**Username:** `@{chat.username}`
├**Type:** {chat.type}
├**Title:** {chat.title}
├**Invite Link**: {chat.invite_link}
├**Description**: {chat.description}
├**ID:** `{chat.id}`
├**Bio:** {chat.bio}
└**Photo ID:**
    `{chat.photo.small_file_id}`


    `{chat.photo.big_photo_unique_id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.photo:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌─**INFO**
├**First Name:** `{chat.first_name}`
├**Last Name:** `{chat.last_name}`
├**Username:** `@{chat.username}`
├**Type:** {chat.type}
├**Title:** {chat.title}
├**Invite Link**: {chat.invite_link}
├**Description**: {chat.description}
├**ID:** `{chat.id}`
├**Bio:** `{chat.bio}
└**Photo ID:**
    `{chat.photo.small_file_id}`


    `{chat.photo.big_photo_unique_id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.sticker:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌─**INFO**
├**First Name:** `{chat.first_name}`
├**Last Name:** `{chat.last_name}`
├**Username:** `@{chat.username}`
├**Type:** {chat.type}
├**Title:** {chat.title}
├**Invite Link**: {chat.invite_link}
├**Description**: {chat.description}
├**ID:** `{chat.id}`
├**Bio:** {chat.bio}
└**Photo ID:**
    `{chat.photo.small_file_id}`


    `{chat.photo.big_photo_unique_id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.audio:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌─**INFO**
├**First Name:** `{chat.first_name}`
├**Last Name:** `{chat.last_name}`
├**Username:** `@{chat.username}`
├**Type:** {chat.type}
├**Title:** {chat.title}
├**Invite Link**: {chat.invite_link}
├**Description**: {chat.description}
├**ID:** `{chat.id}`
├**Bio:** {chat.bio}
└**Photo ID:**
    `{chat.photo.small_file_id}`


    `{chat.photo.big_photo_unique_id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.video:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌─**INFO**
├**First Name:** `{chat.first_name}`
├**Last Name:** `{chat.last_name}`
├**Username:** `@{chat.username}`
├**Type:** {chat.type}
├**Title:** {chat.title}
├**Invite Link**: {chat.invite_link}
├**Description**: {chat.description}
├**ID:** `{chat.id}`
├**Bio:** {chat.bio}
└**Photo ID:**
    `{chat.photo.small_file_id}`


    `{chat.photo.big_photo_unique_id}`


"""
, reply_to_message_id=message.reply_to_message_id)

    else:
        pass



@Client.on_message(filters.command('id', prefixes=prefix))
async def info_id(client, message):
    await message.delete()


    if message.reply_to_message.sticker:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌**Message ID is:**\n`{message.reply_to_message_id}`\n
├**Sticker ID is:**\n`{message.reply_to_message.sticker.file_id}`\n
├**Unique ID is:**\n`{message.reply_to_message.sticker.file_unique_id}`\n
└─┬**send by:**
  ├─**Username:** `@{message.reply_to_message.from_user.username}`
  └─**ID:** `{message.reply_to_message.from_user.id}`
"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.document:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌**Message ID is:**\n`{message.reply_to_message_id}`\n
├**Document ID is:**\n`{message.reply_to_message.document.file_id}`\n
├**Unique ID is:**\n`{message.reply_to_message.document.file_unique_id}`\n
└┬**send by:**
 ├─**Username:** `@{message.reply_to_message.from_user.username}`
 └─**ID:** `{message.reply_to_message.from_user.id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.video:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌**Message ID is:**\n`{message.reply_to_message_id}`\n
├**Video ID is:**\n`{message.reply_to_message.video.file_id}`\n
├**Unique ID is:**\n`{message.reply_to_message.video.file_unique_id}`\n
└┬**send by:**
 ├─**Username:** `@{message.reply_to_message.from_user.username}`
 └─**ID:** `{message.reply_to_message.from_user.id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.photo:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌**Message ID is:**\n`{message.reply_to_message_id}`\n
├**Photo ID is:**\n`{message.reply_to_message.photo.file_id}`\n
├**Unique ID is:**\n`{message.reply_to_message.photo.file_unique_id}`\n
└┬**send by:**
 ├─**Username:** `@{message.reply_to_message.from_user.username}`
 └─**ID:** `{message.reply_to_message.from_user.id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    elif message.reply_to_message.audio:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌**Message ID is:**\n`{message.reply_to_message_id}`\n
├**Audio ID is:**\n`{message.reply_to_message.audio.file_id}`\n
└─┬**send by:**
  ├─**Username:** `@{message.reply_to_message.from_user.username}`
  └─**ID:** `{message.reply_to_message.from_user.id}`

""")

    elif message.reply_to_message:
        await client.send_message(chat_id=message.chat.id, text=
f"""
┌**Message ID is:**\n`{message.reply_to_message_id}`\n
└┬**send by:**
 ├─**Username:** `@{message.reply_to_message.from_user.username}`
 └─**ID:** `{message.reply_to_message.from_user.id}`

"""
, reply_to_message_id=message.reply_to_message_id)


    else:
        pass
