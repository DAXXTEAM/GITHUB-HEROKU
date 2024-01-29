from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop as app
from daxxop.modules.start import *


# --------------------------------------------------------------
@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()


# -------------


# ------------------------------------------------------------




@app.on_message(filters.private & filters.command('help'))
def help_handler(client, message):
    help_text = "This is a sample bot.\n\nYou can use the following commands:"
    
    buttons = [
        [
            InlineKeyboardButton("๏ɢɪᴛʜᴜʙ๏", callback_data="githelp"),
            InlineKeyboardButton("๏ᴀɪ๏", callback_data="aihelp"),
            InlineKeyboardButton("๏ʜᴇʀᴏᴋᴜ๏", callback_data="herokuhelp")
        ],
        [
            InlineKeyboardButton("๏ᴛᴏᴏʟs๏", callback_data="toolhelp"),
            InlineKeyboardButton("๏ɪɴғᴏ๏", callback_data="infohelp"),
            InlineKeyboardButton("๏ᴅᴇᴠ ᴛᴏᴏʟs๏", callback_data="devhelp")
        ],
        
        [
            InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="backhelp")
        ]
    ]
  
    reply_markup = InlineKeyboardMarkup(buttons)
   
    message.reply_text(help_text, reply_markup=reply_markup)



@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'githelp':
        ghelp_text = (
            "๏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ๏\n"
            "➪/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ \n"
            "➪/help -  Dɪsᴘʟᴀʏ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ\n"
            "➪/allrepo - Lɪsᴛ ʏᴏᴜʀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs ᴜsᴇ /allrepo daxxteam\n\n"
            "➪/create_repo - Cʀᴇᴀᴛᴇ ᴀ ɴᴇᴡ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/delrepo - Dᴇʟᴇᴛᴇ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/add_collaborator - Aᴅᴅ ᴀ ᴄᴏʟʟᴀʙᴏʀᴀᴛᴏʀ ᴛᴏ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/remove_collaborator - Rᴇᴍᴏᴠᴇ ᴀ ᴄᴏʟʟᴀʙᴏʀᴀᴛᴏʀ ғʀᴏᴍ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ "
        )

        
        buttons = [
            [
                InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="help")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        
        query.message.edit_text(ghelp_text, reply_markup=reply_markup)
        
