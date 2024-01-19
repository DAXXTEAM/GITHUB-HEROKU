from pyrogram.types import Message
import asyncio, os, time, aiohttp
from telegraph import upload_file
import random 
from config import OWNER_ID
import config
from datetime import datetime
from pyrogram import filters, Client, enums
from daxxop import daxxop as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto




#--------------
# -------------------------------------------------------------------------------
def get_pypi_info(package_name):
    try:
        
        api_url = f"https://pypi.org/pypi/{package_name}/json"
        
        response = requests.get(api_url)
        pypi_info = response.json()
        
        return pypi_info
    
    except Exception as e:
        print(f"Eʀʀᴏʀ ғᴇᴛᴄʜɪɴɢ PʏPI ɪɴғᴏʀᴍᴀᴛɪᴏɴ: {e}")
        return None
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
@app.on_message(filters.command("pypi", prefixes="/"))
def pypi_info_command(client, message):
    try:
       
        package_name = message.command[1]
        
        
        pypi_info = get_pypi_info(package_name)
        
        if pypi_info:
            
            info_message = f"ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ➪ {pypi_info['info']['name']}\n" \
                           f"Lᴀᴛᴇsᴛ ᴠɪʀsɪᴏɴ➪ {pypi_info['info']['version']}\n" \
                           f"Dᴇsᴄʀɪᴘᴛɪᴏɴ➪ {pypi_info['info']['summary']}\n" \
                           f"ᴘʀᴏJᴇᴄᴛ ᴜʀʟ➪ {pypi_info['info']['project_urls']['Homepage']}"
            
            
            client.send_message(message.chat.id, info_message)
        
        else:
            
            client.send_message(message.chat.id, "Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ PʏPI")
    
    except IndexError:

        client.send_message(message.chat.id, "Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ /pypi ᴄᴏᴍᴍᴀɴᴅ.")
       
# -------------------------------------------------------------------------------------

@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("**ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ🎤**")
# --------------------------------------------------------------------------------- #
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ📴**")

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
