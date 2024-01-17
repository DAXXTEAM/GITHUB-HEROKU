from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop as app
from config import BOT_USERNAME
from config import OWNER_ID
from pyrogram.types import Message

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


start_txt = """**
๏🤖 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ! 🚀

๏ᴛʜɪs ʙᴏᴛ sɪᴍᴘʟɪғɪᴇs ʏᴏᴜʀ   
ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ Jᴏᴜʀɴᴇʏ ʙʏ ɪɴᴛᴇɢʀᴀᴛɪɴɢ ɢɪᴛʜᴜʙ ʀᴇᴄᴇɪᴠᴇ ɪɴsᴛᴀɴᴛ ɢɪᴛʜᴜʙ ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ


๏ᴅᴇᴘʟᴏʏᴍᴇɴᴛs ᴇғғᴏʀᴛʟᴇssʟʏ
ᴛʏᴘᴇ /help ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ sᴜᴘᴇʀᴄʜᴀʀɢᴇ ʏᴏᴜʀ ᴡᴏʀᴋғʟᴏᴡ. ʟᴇᴛ's ᴍᴀᴋᴇ ᴄᴏᴅɪɴɢ ᴀɴᴅ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴀ ʙʀᴇᴇᴢᴇ! 💻🔧 #ɢɪᴛʜᴜʙ #ʜᴇʀᴏᴋᴜ #ᴅᴇᴠᴛᴏᴏʟs"
**"""




@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/HEROKUFREECC"),
          InlineKeyboardButton("ᴅᴇᴠ", url="https://t.me/iam_daxx"),
          InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/ecbeac5889f9542f32469.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )



#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪



@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'help':
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("GitHub", callback_data="git_help")],
        [InlineKeyboardButton("Heroku", url="https://dashboard.heroku.com/")]
    ])
    client.send_message(
        chat_id=message.chat.id,
        text=help_text,
        reply_markup=reply_markup
    )










@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'git_help':
       git_help_text = (
            "GitHub Control Bot Commands:\n"
            "/start - Start the bot\n"
            "/help - Display this help message\n"
            "/allrepo - List your GitHub repositories\n"
            "/create_repo - Create a new GitHub repository\n"
            "/delrepo - Delete a GitHub repository\n"
            "/add_collaborator - Add a collaborator to a GitHub repository\n"
            "/remove_collaborator - Remove a collaborator from a GitHub repository"
        )
        query.message.edit_text(git_help_text)
        
# incoming msg

@app.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
        
