import os

from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix

import asyncio
from asyncio import sleep

from utils.ytdlp import AudioFile
from utils.ytdlp import VideoFile


#{message.reply_to_message.id}
#{message.reply_to_message.from_user.id}
#{reply_to_message_id=message.reply_to_message.id}


@Client.on_message(filters.command('aud', prefixes=prefix) & filters.me)
async def soundcloud(client, message):
    module_dir = '/data/data/com.termux/files/home/zxc-team/zxc-Userbot/ytdlp_down/'
    first_path = os.getcwd()
    s = message.text.split(maxsplit=1)[1]

    n1 = 'https://soundcloud.com/'
    n2 = 'https://soundcloud.app.goo.gl/'
    n3 = 'https://youtu.be/'
    n4 = 'https://www.youtube.com/'
    n5 = 'https://deezer.page.link/'
    split_text = s.split()

    for i in split_text:
        if n5 in i:
            link = None
            x = None
            await message.edit_text(text='**such links are not supported**')
            pass

        elif n1 or n2 or n3 or n4 in i:
            link = i
            x = AudioFile(link)

        else:
            pass

    if link == i:
        await message.edit_text(text='**please wait ...**')
        x.download_file()
        thumm = x.show_thumm()

        mas_audio = []
        path = module_dir
        for root, dirs, files in os.walk(module_dir):
            for file in files:
                if(file.endswith('.mp3')):
                    mas_audio.append(os.path.join(file))

                elif(file.endswith('.m4a')):
                    mas_audio.append(os.path.join(file))

                else:
                    pass

        for data in mas_audio:
            link = None
            await client.send_audio(chat_id=message.chat.id, audio=f'{module_dir}{data}', thumb=f'{module_dir}{thumm}')
            await message.edit_text(text='**file sent successfully**')
            await asyncio.sleep(2)
            await message.delete()
            x.remove_audio_files()
            x.remove_thumb()
            x.to_main_dir()

    else:
        pass


@Client.on_message(filters.command('vid', prefixes=prefix) & filters.me)
async def youtube(client, message):
    module_dir = '/data/data/com.termux/files/home/zxc-Userbot/ytdlp_down/'
    first_path = os.getcwd()

    await asyncio.sleep(1)
    s = message.text.split(maxsplit=1)[1]
    split_text = s.split()
    n = 'https://youtu.be/'
    n2 = 'https://www.youtube.com/'

    for i in split_text:
        if n or n2 in i:
            link = i
            y = VideoFile(link)
        else:
            pass

    await message.edit_text(text='**please wait ...**')
    await message.edit_text(text='')
    y.download_file()
    thumm = y.show_thumm()

    mas_video = []
    path = module_dir
    for root, dirs, files in os.walk(module_dir):
        for file in files:
            if(file.endswith('.mp4')):
                mas_video.append(os.path.join(file))
            else:
                pass

    for data in mas_video:
        await client.send_audio(chat_id=message.chat.id, audio=f'{module_dir}{data}', thumb=f'{module_dir}{thumm}')
        await message.edit_text(text='**file sent successfully**')
        await asyncio.sleep(2)
        await message.delete()
        y.remove_video_files()
        y.remove_thumb()
        y.to_main_dir()




modules_help['ytdlp_mod'] = {
    'aud': '.aud [link from youtube/soundcloud]',
    'vid': '.vid [link from youtube]',
}
