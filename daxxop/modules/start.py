from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop as app
from config import BOT_USERNAME, OWNER_ID 
import config
from pyrogram.types import InputMediaVideo
import random 
from pyrogram.types import Message

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


start_txt = f"""**
ʜᴇʏ ᴛʜᴇʀᴇ  ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !
━━━━━━━━━━━━━━━━━━━━━━
๏🤖 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ
━━━━━━━━━━━━━━━━━━━━━━
๏ᴛʜɪs ʙᴏᴛ sɪᴍᴘʟɪғɪᴇs ʏᴏᴜʀ   
ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ Jᴏᴜʀɴᴇʏ ʙʏ ɪɴᴛᴇɢʀᴀᴛɪɴɢ ɢɪᴛʜᴜʙ ʀᴇᴄᴇɪᴠᴇ ɪɴsᴛᴀɴᴛ ɢɪᴛʜᴜʙ ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ
━━━━━━━━━━━━━━━━━━━━━━
๏ᴅᴇᴘʟᴏʏᴍᴇɴᴛs ᴇғғᴏʀᴛʟᴇssʟʏ
ᴛʏᴘᴇ /help ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ sᴜᴘᴇʀᴄʜᴀʀɢᴇ ʏᴏᴜʀ ᴡᴏʀᴋғʟᴏᴡ. ʟᴇᴛ's ᴍᴀᴋᴇ ᴄᴏᴅɪɴɢ ᴀɴᴅ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴀ ʙʀᴇᴇᴢᴇ! 💻🔧 #ɢɪᴛʜᴜʙ #ʜᴇʀᴏᴋᴜ #ᴅᴇᴠᴛᴏᴏʟs"
━━━━━━━━━━━━━━━━━━━━━━
**"""

#---------------------

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("๏ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ๏", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("๏sᴜᴘᴘᴏʀᴛ ᴛᴇᴀᴍ๏", url="https://t.me/HEROKUFREECC"),
          InlineKeyboardButton("๏ᴍʏ ᴅᴇᴠʟᴏᴘᴇʀ๏", user_id=config.OWNER_ID)
        ],
        [
          InlineKeyboardButton("๏ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs๏", callback_data="settings_back_helper"),
          InlineKeyboardButton("๏ʙᴏᴛ ᴄᴏᴅᴇs๏", callback_data="new_callback_data")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/726169835ed7cdfd5ccf4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

@app.on_message(filters.private & filters.command('help'))
async def help_handler(_, msg):
    help_text = (
        "**๏ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.**"
        "**ᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ sᴜᴘᴘᴏʀᴛ** \n\n **ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ๏: /**"
    )
    
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
            InlineKeyboardButton("๏ᴄʟᴏsᴇ๏", callback_data="close_data")
        ]
    ]
  
    reply_markup = InlineKeyboardMarkup(buttons)
   
    await msg.reply_text(help_text, reply_markup=reply_markup)


#------------------------------------------------------------------------------------
@app.on_message(filters.command(["help"]) & filters.group)
async def help_command(_, message):
    start_button_link = f"https://t.me/{BOT_USERNAME}?start=your_start_parameter"
    caption = "๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴍʏ ʜᴇʟᴘ ᴍᴇɴᴜ ɪɴ ʏᴏᴜʀ ᴘᴍ "

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("๏ʜᴇʟᴘ๏", url=start_button_link)],
        ]
    )

    await message.reply_text(caption, reply_markup=keyboard)



#-------------------------------------------------

@app.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)

       

glink = 'https://t.me/DAXXSUPPORT'


@app.on_callback_query()
async def callback_query_handler(_, query):
    if query.data == 'close_data':
        chat_id = query.message.chat.id
        await query.message.delete()
    elif query.data == 'settings_back_helper':
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
                InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="back_help")
            ]
        ]

        help_text = (
            "**๏ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.**"
            "**ᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ sᴜᴘᴘᴏʀᴛ** \n\n **ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ๏: /**"
        )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(help_text, reply_markup=reply_markup)

    elif query.data == 'back_help':
        start_txt = (
            "**ʜᴇʏ ᴛʜᴇʀᴇ  ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "**๏🤖 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "**๏ᴛʜɪs ʙᴏᴛ sɪᴍᴘʟɪғɪᴇs ʏᴏᴜʀ**\n"
            "**ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ Jᴏᴜʀɴᴇʏ ʙʏ ɪɴᴛᴇɢʀᴀᴛɪɴɢ ɢɪᴛʜᴜʙ ʀᴇᴄᴇɪᴠᴇ ɪɴsᴛᴀɴᴛ ɢɪᴛʜᴜʙ ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ**\n"
            "━━━━━━━━━━━━━━━━━━━━━━"
            "**๏ᴅᴇᴘʟᴏʏᴍᴇɴᴛs ᴇғғᴏʀᴛʟᴇssʟʏ**\n"
            "**ᴛʏᴘᴇ /help ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ sᴜᴘᴇʀᴄʜᴀʀɢᴇ ʏᴏᴜʀ ᴡᴏʀᴋғʟᴏᴡ. ʟᴇᴛ's ᴍᴀᴋᴇ ᴄᴏᴅɪɴɢ ᴀɴᴅ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴀ ʙʀᴇᴇᴢᴇ! 💻🔧 #ɢɪᴛʜᴜʙ #ʜᴇʀᴏᴋᴜ #ᴅᴇᴠᴛᴏᴏʟs**\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
        )
        buttons = [
            [ 
              InlineKeyboardButton("๏ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ๏", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
              InlineKeyboardButton("๏sᴜᴘᴘᴏʀᴛ ᴛᴇᴀᴍ๏", url="https://t.me/HEROKUFREECC"),
              InlineKeyboardButton("๏ᴍʏ ᴅᴇᴠʟᴏᴘᴇʀ๏", user_id=config.OWNER_ID)
            ],
            [
              InlineKeyboardButton("๏ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs๏", callback_data="settings_back_helper"),
              InlineKeyboardButton("๏ʙᴏᴛ ᴄᴏᴅᴇs๏", callback_data="new_callback_data")
            ]
        ]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(caption=start_txt, reply_markup=reply_markup)


    elif query.data == 'new_callback_data':
        await query.message.edit_media(
            media=InputMediaVideo("https://graph.org/file/8926caeb4948c47b12080.mp4", has_spoiler=True),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data="back_help")]
                ]
            ),
        )
    elif query.data == 'githelp':
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
                InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="settings_back_helper")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await query.message.edit_text(ghelp_text, reply_markup=reply_markup)

    elif query.data == 'aihelp':
        aihelp_text = (
              "/assis - ChatGPT voice reply"
              "/bingsearch - Bing search functionality"
              "/chatgpt /ai /ask - Invoke ChatGPT for text-based interaction"
              
        )
        
        buttons = [
            [
                InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="settings_back_helper")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)        
        await query.message.edit_text(aihelp_text, reply_markup=reply_markup)

    elif query.data == 'herokuhelp':
        herokuhelp_text = (
                     "/restartdynos - Restart dynos"
                    "/apps - List available applications"
                   "/veriable - Variable-related operations"
                   "/herokulogs - View Heroku logs"
                  "/herokuinfo - Get Heroku application info"
                "/delheroku - Delete a Heroku application"
               "/addapp - Add a new collaboration"                   
        )
           
        buttons = [
            [
                InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="settings_back_helper")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)  
        await query.message.edit_text(herokuhelp_text, reply_markup=reply_markup)

    elif query.data == 'toolhelp':
        toolhelp_text = (
                        "/table - Generate a table"
                       "/telegraph /tgm - telegram link generate"             
        )
        
        buttons = [
            [
                InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="settings_back_helper")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(toolhelp_text, reply_markup=reply_markup)
