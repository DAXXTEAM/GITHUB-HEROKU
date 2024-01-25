from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from pyrogram.types import Message
import asyncio, os, time, aiohttp
from telegraph import upload_file
import random
import requests
from config import OWNER_ID
import config
from datetime import datetime
from pyrogram import filters, Client, enums
from daxxop import daxxop as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

# --------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------


def download_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session = requests.Session()
    session.mount('http://', HTTPAdapter(max_retries=retries))

    try:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to download source code. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
@app.on_message(filters.command("html"))
def web_download(client, message):
    # Check if the command has a URL attached
    if len(message.command) == 1:
        message.reply_text("Please enter a URL along with the /html command.")
        return

    url = message.command[1]

    source_code = download_website(url)
    if source_code.startswith('An error occurred') or source_code.startswith('Failed to download'):
        message.reply_text(source_code)
    else:
        # Save the source code to a file
        with open('website.txt', 'w', encoding='utf-8') as file:
            file.write(source_code)

        # Reply with the file
        message.reply_document(document='website.txt', caption=f"Source code of {url}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
def get_pypi_info(package_name):
    try:
        
        api_url = f"https://pypi.org/pypi/{package_name}/json"
        
        response = requests.get(api_url)
        pypi_info = response.json()
        
        return pypi_info
    
    except Exception as e:
        print(f"Eʀʀᴏʀ ғᴇᴛᴄʜɪɴɢ PʏPɪɴғᴏʀᴍᴀᴛɪᴏɴ: {e}")
        return None
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
@app.on_message(filters.command("pypi", prefixes="/"))
def pypi_info_command(client, message):
    try:
       
        package_name = message.command[1]
        
        
        pypi_info = get_pypi_info(package_name)
        
        if pypi_info:
            
            info_message = f"๏ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ➪ {pypi_info['info']['name']}\n━━━━━━━━━━━━━━━━━━━━━" \
                           f"๏ Lᴀᴛᴇsᴛ ᴠɪʀsɪᴏɴ➪ {pypi_info['info']['version']}\n━━━━━━━━━━━━━━━━━━━━━" \
                           f"๏ Dᴇsᴄʀɪᴘᴛɪᴏɴ➪ {pypi_info['info']['summary']}\n━━━━━━━━━━━━━━━━━━━━━" \
                           f"๏ ᴘʀᴏJᴇᴄᴛ ᴜʀʟ➪ {pypi_info['info']['project_urls']['Homepage']}"
            
            
            client.send_message(message.chat.id, info_message)
        
        else:
            
            client.send_message(message.chat.id, "Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ PʏPI")
    
    except IndexError:

        client.send_message(message.chat.id, "Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ /pypi ᴄᴏᴍᴍᴀɴᴅ.")
       
# -------------------------------------------------------------------------------------
"""
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("**ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ🎤**")
# --------------------------------------------------------------------------------- #
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ📴**")
"""

# _-----------

async def send_notification(client, chat_id, text):
    try:
        await client.send_message(chat_id, text)
    except Exception as e:
        print(f"Error sending notification: {e}")

@app.on_chat_member_updated(filters.group)
async def voice_chat_notification(client, update: ChatMemberUpdated):
    chat_id = update.chat.id
    user_id = update.new_chat_member.user.id

    if update.new_chat_member.voice_chat:
        text = f"🎙️ Voice chat started! @{update.new_chat_member.user.username} is speaking."
    elif update.old_chat_member and update.old_chat_member.voice_chat:
        text = f"🔇 Voice chat ended. Thanks for joining, @{update.old_chat_member.user.username}!"
    else:
        return

    # Notify all group members about the voice chat status change
    members = await client.get_chat_members(chat_id)
    for member in members:
        if member.user.id != user_id:  # Avoid notifying the user who triggered the event
            await send_notification(client, member.user.id, text)
            



# --------------------------------------------------------------------------------- #
@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ☄️")
           except:
             pass

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("leavegroup")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"ɢᴏᴏᴅ ʙʏᴇ ʙᴀʙʏ🫡"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)
    
# --------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------
@app.on_message(filters.command(["tgm" , "telegraph"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("ᴍᴀᴋɪɴɢ ᴀ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴡᴀɪᴛ ᴀ sᴇᴄ.")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}')
#--------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_message(filters.command("table"))
def multiplication_table(_, message: Message):
    try:
        
        number = int(message.text.split()[1])

        table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 11)])

        
        message.reply_text(f"Multiplication table of {number}:\n\n{table}")
    except IndexError:
        message.reply_text("Please enter a valid number after the command /table.")
    except ValueError:
        message.reply_text("Invalid input. Please enter a valid number.")
# --------------------------------------------------------------------------------- #
#--------------------------------------------------------------------------
@app.on_message(filters.command("id"))
def get_user_chat_id(_: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    response_text = (
        f"ʏᴏᴜʀ ɪᴅ: `{user_id}`\n"
        f"ᴄʜᴀᴛ ɪᴅ: `{chat_id}`"
    )

    message.reply_text(response_text)
# --------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()

# --------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git DAXXTEAM")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']

                caption = f"""ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}
                
ᴜsᴇʀɴᴀᴍᴇ: {username}
ʙɪᴏ: {bio}
ʟɪɴᴋ: [Here]({url})
ᴄᴏᴍᴩᴀɴʏ: {company}
ᴄʀᴇᴀᴛᴇᴅ ᴏɴ: {created_at}
ʀᴇᴩᴏsɪᴛᴏʀɪᴇs: {repositories}
ʙʟᴏɢ: {blog}
ʟᴏᴄᴀᴛɪᴏɴ: {location}
ғᴏʟʟᴏᴡᴇʀs: {followers}
ғᴏʟʟᴏᴡɪɴɢ: {following}"""

            except Exception as e:
                print(str(e))
                pass
# --------------------------------------------------------------------------------- #
    
    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("๏ ᴄʟᴏsᴇ ๏", callback_data="close_data")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])
# --------------------------------------------------------------------------------- #
    
    # Send the message with the inline keyboard
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=inline_keyboard)
# --------------------------------------------------------------------------------- #
