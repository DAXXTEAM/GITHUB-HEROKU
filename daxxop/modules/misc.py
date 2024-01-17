from pyrogram.types import Message
import asyncio, os, time, aiohttp
import aiohttp
import random 
from datetime import datetime
from pyrogram import filters, Client, enums
from pyrogram import filters
from daxxop import daxxop as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# --------------------------------------------------------------------------------- #

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



WEL_GIFS = [
    "https://telegra.ph/file/bd77135692ad077d34d64.mp4",
    "https://telegra.ph/file/df6e25fd22b0562309640.mp4"
]

def create_close_button():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("๏ ᴄʟᴏsᴇ ๏", callback_data="close_data")]]
    )

@app.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    random_wel_gif = random.choice(WEL_GIFS)
    join_date = datetime.utcfromtimestamp(m.date.timestamp()).strftime('%Y-%m-%d')
    
    welcome_message = await m.reply_animation(
        random_wel_gif,
        caption=f"Hɪɪ ᴅᴇᴀʀ {m.from_user.mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {m.chat.title}!\n• Jᴏɪɴᴇᴅ ᴀᴛ: {join_date}\n┏━━━━━━━━━━━━━━━━━━━━┓\n• ꜰᴏʟʟᴏᴡ ᴏᴜʀ ʀᴜʟᴇꜱ ᴘʟᴇᴀꜱᴇ✨\n\n╚»『ᴅᴏɴ'ᴛ ᴜᴘʟᴏᴀᴅ 18+ ᴍᴀᴛᴇʀɪᴀʟ\n╚»『 ꜱᴘᴀᴍᴍɪɴɢ & ꜰɪɪɢʜᴛ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ✨\n╚»『 ᴏᴡɴᴇʀ - ꜱᴇᴄʀᴇᴛ\n╚»『 ɢɪʀʟꜱ ᴅᴍ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ\n╚» ᴏᴛʜᴇʀᴇ ᴡɪsᴇ ʏᴏᴜ ᴡɪʟʟ ɴᴇ ʙᴀɴᴇᴅ\n╚»『 ᴇɴᴊᴏʏ ᴏᴜʀ ɢʀᴏᴜᴘ\n┗━━━━━━━━━━━━━━━━━━━━",
    )

    # Use the message ID of the welcome message for replies in the future
    app.set_my_commands(welcome_message.message_id)

@app.on_message(filters.left_chat_member)
async def member_has_left(_, m: Message):
    left_gif = "https://telegra.ph/file/d28047520fad932521368.mp4"
    await m.reply_animation(
        animation=left_gif,
        caption=f"Sᴀᴅ Tᴏ Sᴇᴇ Yᴏᴜ Lᴇᴀᴠɪɴɢ {m.from_user.mention}\nTᴀᴋᴇ Cᴀʀᴇ!\n",
        reply_markup=create_close_button()
    )
