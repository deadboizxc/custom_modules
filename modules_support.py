from pyrogram import Client, filters
from pyrogram.types import Message
import random
import datetime
from git import Repo

from utils.misc import (
    modules_help,
    prefix,
    userbot_version,
    python_version,
    gitrepo,
)

mod_version = f"4.1.4-RE-beta"
modrepo = Repo("/data/data/com.termux/files/home/zxc-team/custom_modules/")


@Client.on_message(filters.command(["modules_support", "mod_repo"], prefix) & filters.me)
async def support(_, message: Message):
    devs = ["@deadboizxc"]
    random.shuffle(devs)

    commands_count = float(
        len([cmd for module in modules_help for cmd in module])
    )

    await message.edit(
        f"<b>💜 custom_modules 💜</b>\n\n"
#       "<b>License:</b> <a href=https://github.com/deadboizxc/zxc-Userbot/blob/deadboizxc/LICENSE>GNU GPL v3</a>\n\n"
        "<b>GitHub:</b> <a href=https://github.com/deadboizxc/custom_modules>"
        "deadboizxc/custom_modules</a>\n"
        f"<b>Main developers:</b> {', '.join(devs)}\n\n"
        f"<b>Python version:<b/> {python_version}\n"
        f"<b>Modules count:</b> {len(modules_help) / 1}\n"
        f"<b>Commands count:</b> {commands_count}</b>",
        disable_web_page_preview=True,
    )

@Client.on_message(filters.command(["modules_version", "mod_ver"], prefix) & filters.me)
async def version(client: Client, message: Message):
    changelog = ""
    await message.delete()

    remote_url = list(modrepo.remote().urls)[0]
    commit_time = (
        datetime.datetime.fromtimestamp(modrepo.head.commit.committed_date)
        .astimezone(datetime.timezone.utc)
        .strftime("%Y-%m-%d %H:%M:%S %Z")
    )

    await message.reply(
        f"<b>💜 <a href = https://github.com/deadboizxc/custom_modules>custom_modules</a> 💜</b>\n"
        f"<b>Version: </b><code>{mod_version}</code>\n"
        + (
            f"<b>Branch:</b> <code><a href={remote_url}/tree/{modrepo.active_branch}>{modrepo.active_branch}</a></code>\n"
            if modrepo.active_branch != "master"
            else ""
        )
        + f"<b>Commit:</b> <code><a href={remote_url}/commit/{modrepo.head.commit.hexsha}>"
        f"{modrepo.head.commit.hexsha[:7]}</a></code> by <b>{modrepo.head.commit.author.name}</b>\n"
        f"<b>Commit time:</b> <code>{commit_time}</code>",
    disable_web_page_preview=True)


modules_help["modules_support"] = {
    "modules_support": "Information about modules",
    "modules_version": "Check modules version",
}
