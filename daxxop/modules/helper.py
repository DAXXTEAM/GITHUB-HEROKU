from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop as app

@app.on_message(filters.private & filters.command('help'))
def help_handler(client, message):
    help_text = "This is a sample bot.\n\nYou can use the following commands:"
    
    
    buttons = [
        [
        InlineKeyboardButton("Button 1", callback_data="button1")
        InlineKeyboardButton("Button 2", callback_data="button2")
        InlineKeyboardButton("Button 3", callback_data="button3")
    ],
        [
        InlineKeyboardButton("Button 4", callback_data="button4")
        InlineKeyboardButton("Button 5", callback_data="button5")
        InlineKeyboardButton("Button 6", callback_data="button6")

        ],

      [
        InlineKeyboardButton("Button 7", callback_data="button7")
        InlineKeyboardButton("Button 8", callback_data="button8")
        InlineKeyboardButton("Button 9", callback_data="button9")
      ],
        [
        InlineKeyboardButton("Button 10", callback_data="button10")
    ]
    ],
  
    reply_markup = InlineKeyboardMarkup([buttons])
   
    message.reply_text(help_text, reply_markup=reply_markup)
