"""
import asyncio
import importlib
from pyrogram import idle
from daxxop import daxxop
from daxxop.modules import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("daxxop.modules." + all_module)
    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ. ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())


"""

import asyncio
import importlib
from daxxop import daxxop
from pyrogram import Client, idle
from config import LOGGER_ID
from daxxop.modules import ALL_MODULES

loop = asyncio.get_event_loop()

async def send_startup_message(Client, logger_id):
    
    startup_message = "Bot has successfully started!"
    await Client.send_message(logger_id, startup_message)

async def daxxpapa_boot(Client, start_in_logger_groups=False):
    for all_module in ALL_MODULES:
        importlib.import_module("daxxop.modules." + all_module)

    if start_in_logger_groups:
        await send_startup_message(Client, LOGGER_ID)

    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ. ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

if __name__ == "__main__":
    loop.run_until_complete(daxxop.start())
    loop.run_until_complete(daxxpapa_boot(Client, start_in_logger_groups=True))
    loop.run_until_complete(daxxop.stop())
    
