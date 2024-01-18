import asyncio, config, logging, time
 
from importlib import import_module
from os import listdir, path
from dotenv import load_dotenv
from pyrogram import Client
from config import LOGGER_ID




loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)


daxxop = Client(
    name=":daxxop:",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
)


async def daxxop_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await daxxop.start()
    getme = await daxxop.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
    await daxxop.send_message(config.LOGGER_ID, "**Bot Started !**")
         

loop.run_until_complete(daxxop_bot())
