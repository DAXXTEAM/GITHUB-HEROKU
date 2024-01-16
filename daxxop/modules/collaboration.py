from pyrogram import Client, filters
from github import Github
from config import OWNER_ID
import config
from daxxop import daxxop as app

github_token = config.GIT_TOKEN


@app.on_message(filters.command("add_collaborator", prefixes="/") & filters.user([int(OWNER_ID)]))
async def add_collaborator_command(client, message):
    try:
        _, repo_url, github_username = message.text.split(" ", 2)
        if repo_url.startswith("https://github.com/"):
            g = Github(github_token)
            repo_name = repo_url.split("/")[-1]
            repo_owner = repo_url.split("/")[-2]
            repo = g.get_repo(f"{repo_owner}/{repo_name}")
            collaborator = g.get_user(github_username)
            repo.add_to_collaborators(collaborator.login, "push")
            await message.reply(f"{github_username} ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴀs ᴀ ᴄᴏʟʟᴀʙᴏʀᴀᴛᴏʀ ᴛᴏ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ.")
        else:
            await message.reply("Iɴᴠᴀʟɪᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ URL. Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ URL.")
    except Exception as e:
        await message.reply(f"Tᴜ Pɪʀᴏ ʜᴀɪ Bʀᴏ")



@app.on_message(filters.command("remove_collaborator", prefixes="/") & filters.user([int(OWNER_ID)]))
async def remove_collaborator_command(client, message):
    try:
        _, repo_url, github_username = message.text.split(" ", 2)
        if repo_url.startswith("https://github.com/"):
            g = Github(github_token)
            repo_name = repo_url.split("/")[-1]
            repo_owner = repo_url.split("/")[-2]
            repo = g.get_repo(f"{repo_owner}/{repo_name}")
            collaborator = g.get_user(github_username)
            repo.remove_from_collaborators(collaborator.login)
            await message.reply(f"{github_username} Invalid GitHub repository URL. Please provide a valid URL.")
        else:
            await message.reply("Iɴᴠᴀʟɪᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ URL. Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ URL")
    except Exception as e:
        await message.reply(f"Tᴜ Pɪʀᴏ ʜᴀɪ Bʀᴏ")
