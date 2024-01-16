import asyncio
import logging
import time
from importlib import import_module
from os import listdir, path
from dotenv import load_dotenv
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, LOGGER_ID

loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

daxxop = Client(
    ":daxxop:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

async def daxxop_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await daxxop.start()  # Start the client to synchronize with Telegram servers
    await asyncio.sleep(2)  # Wait for a moment to ensure synchronization
    await daxxop.send_message(LOGGER_ID, text=" SUCCESSFUL STARTED ")
    getme = await daxxop.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
    await daxxop.stop()

loop.run_until_complete(daxxop_bot())
