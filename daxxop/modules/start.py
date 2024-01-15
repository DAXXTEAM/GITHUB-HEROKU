from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop
from config import BOT_USERNAME

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

logger_group_chat_id = -100180299074

# Function to send a start message to the logger group
def send_start_message():
    bot_info = app.get_me()
    start_message = (
        f"ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :\n"
        f"ɪᴅ : {bot_info.id}\n"
        f"ɴᴀᴍᴇ : {bot_info.first_name}\n"
        f"ᴜsᴇʀɴᴀᴍᴇ : {bot_info.username}"
    )
    app.send_message(logger_group_chat_id, start_message)

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


start_txt = """**
🤖 Wᴇʟᴄᴏᴍᴇ ᴛᴏ GɪᴛHᴜʙ Cᴏɴᴛʀᴏʟ Bᴏᴛ! 🚀

Tʜɪs ʙᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs ʀɪɢʜᴛ ғʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ. Usᴇ ᴄᴏᴍᴍᴀɴᴅs ʟɪᴋᴇ /gitprivate ᴀɴᴅ /gitpublic ᴛᴏ ᴄʜᴀɴɢᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴠɪsɪʙɪʟɪᴛʏ. Eɴsᴜʀᴇ ᴛᴏ ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛᴇ ᴡɪᴛʜ ʏᴏᴜʀ GɪᴛHᴜʙ ᴛᴏᴋᴇɴ ғᴏʀ sᴇᴄᴜʀᴇ ᴀᴄᴄᴇss. Fᴏʀ ᴀssɪsᴛᴀɴᴄᴇ, ᴜsᴇ /help.

🔗 GɪᴛHᴜʙ Cᴏɴᴛʀᴏʟ Bᴏᴛ ɪs ʜᴇʀᴇ ᴛᴏ sɪᴍᴘʟɪғʏ ʏᴏᴜʀ GɪᴛHᴜʙ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ. Hᴀᴘᴘʏ ᴄᴏᴅɪɴɢ!
**"""




@daxxop.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/iam_daxx"),
          InlineKeyboardButton("ᴅᴇᴠ", url="https://t.me/iam_daxx"),
          InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/ecbeac5889f9542f32469.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )





