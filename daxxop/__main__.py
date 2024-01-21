import asyncio
import importlib
from pyrogram import idle
from daxxop import daxxop
from daxxop.modules import ALL_MODULES

class Bot:
    def __init__(self, mention, id, name, username):
        self.mention = mention
        self.id = id
        self.name = name
        self.username = username

LOGGER_ID = -1001802990747

loop = asyncio.get_event_loop()

async def daxxpapa_boot(bot_instance):
    for all_module in ALL_MODULES:
        importlib.import_module("daxxop.modules." + all_module)
    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ. ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")
    await daxxop.send_message(LOGGER_ID, f"**<u><b>» {bot_instance.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{bot_instance.id}</code>\nɴᴀᴍᴇ : {bot_instance.name}\nᴜsᴇʀɴᴀᴍᴇ : @{bot_instance.username}**")

if __name__ == "__main__":
    bot_instance = Bot(mention="BotMention", id=123, name="BotName", username="bot_username")
    loop.run_until_complete(daxxpapa_boot(bot_instance))
    
