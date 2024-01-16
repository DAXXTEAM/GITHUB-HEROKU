from pyrogram import Client, filters
import requests
import config
from config import OWNER_ID
from daxxop import daxxop as app

GITHUB_TOKEN = config.GIT_TOKEN



def create_github_repo(repo_name):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"name": repo_name, "auto_init": True}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        repo_link = response.json().get("html_url")
        return f"Rᴇᴘᴏsɪᴛᴏʀʏ ᴄʀᴇᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!\nYᴏᴜʀ ʀᴇᴘᴏ ʟɪɴᴋ: {repo_link}"
    else:
        return f"Failed to create repository. Error: {response.text}"

@app.on_message(filters.command("create_repo", prefixes="/") & filters.user([int(OWNER_ID)]))
#@app.on_message(filters.command("create_repo", prefixes="/"))
def create_repo_command(client, message):
    command_parts = message.text.split(" ", 1)

    if len(command_parts) == 2:
        repo_name = command_parts[1].strip()
        response_text = create_github_repo(repo_name)
        message.reply_text(response_text)
    else:
        message.reply_text("Iɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴀɢᴇ. Pʟᴇᴀsᴇ ᴜsᴇ /create_repo <repository_name>")
