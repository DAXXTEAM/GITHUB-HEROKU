from pyrogram import Client, filters
from pyrogram.types import Message
from daxxop import daxxop as app

@app.on_message(filters.command("id"))
def get_user_chat_id(_: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    response_text = (
        f"ʏᴏᴜʀ ɪᴅ: `{user_id}`\n"
        f"ᴄʜᴀᴛ ɪᴅ: `{chat_id}`"
    )

    message.reply_text(response_text)
