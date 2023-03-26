import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AdrishXMusic import LOGGER, app, userbot
from AdrishXMusic.core.call import Adrish
from AdrishXMusic.plugins import ALL_MODULES
from AdrishXMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AdrishXMusic").error("Add Pyrogram string session and then try...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AdrishXMusic.plugins" + all_module)
    LOGGER("AdrishXMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Adrish.start()
    try:
        await Adrish.stream_call("https://telegra.ph/file/e33f6fc7c4824982b136b.mp4")
    except NoActiveGroupCall:
        LOGGER("AdrishXMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await Adrish.decorators()
    LOGGER("AdrishXMusic").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AdrishXMusic").info("Stopping Music Bot")
