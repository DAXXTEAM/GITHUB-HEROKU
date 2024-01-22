"""
from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "6065719968:AAHtBO5sKY-Y5UxT1fMquJ0ghROoy2rYibE")
BOT_USERNAME = getenv("BOT_USERNAME", "DEVLOPERROBOT")
OWNER_ID = int(getenv("OWNER_ID", "6664582540"))
GIT_TOKEN = getenv("GIT_TOKEN", "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")
LOGGER_ID = getenv("LOGGER_ID", "-1001802990747")

"""
# ------------------------------------------------

import os
from os import getenv

API_ID = int(os.environ.get("YOUR_API_ID"))
API_HASH = os.environ.get("YOUR_API_HASH")
BOT_TOKEN = os.environ.get("YOUR_BOT_TOKEN")
BOT_USERNAME = os.environ.get("YOUR_BOT_USERNAME")
OWNER_ID = int(os.environ.get("YOUR_OWNER_ID"))
GIT_TOKEN = os.environ.get("YOUR_GIT_TOKEN")
LOGGER_ID = int(os.environ.get("YOUR_LOGGER_ID"))
