import requests
import config
from config import BOT_USERNAME

def bot_start(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")

telegram_bot_token = config.BOT_TOKEN
telegram_chat_id = '@herokufreecc'
start_message = """{BOT_USERNAME} sᴜᴄᴄᴇssғᴜʟ sᴛᴀʀᴛᴇᴅ"""

bot_start(telegram_bot_token, telegram_chat_id, start_message)
