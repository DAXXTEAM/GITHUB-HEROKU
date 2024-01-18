import os
import time
import requests
from pyrogram.types import Message
from pyrogram import Client, filters
from heroku3 import from_key
from daxxop import daxxop as app
from config import OWNER_ID

# ----------------------- ------# ----------------------- ------

heroku_api_key = 'ccb94c02-9e60-4605-97b1-3977084781a8'

# ----------------------- ------# ----------------------- ------

def get_heroku_logs(app_name):
    heroku_conn = from_key(heroku_api_key)

    if not heroku_conn.apps().get(app_name):
        return f"App '{app_name}' not found on Heroku."

    app = heroku_conn.apps()[app_name]
    logs = app.get_log()
    
    # Save logs to a file named 'log.txt'
    with open('log.txt', 'w') as file:
        file.write(logs)
    
    return f"Heroku logs for app '{app_name}' saved to 'log.txt'."

@app.on_message(filters.command("herokulogs") & filters.user(OWNER_ID))
async def heroku_logs_command(client, message):
    try:
        _, app_name = message.text.split(" ", 1)
        response = get_heroku_logs(app_name)
        await message.reply_text(response)
        await message.reply_document("log.txt")  # Send the log file
        os.remove("log.txt")  # Remove the file after sending
    except ValueError:
        await message.reply_text("Invalid command format. Use /herokulogs <app_name>")
    except Exception as e:
        await message.reply_text(f"Error fetching Heroku logs: {str(e)}")



#----------------
@app.on_message(filters.command("herokuinfo") & filters.user(OWNER_ID))
async def get_heroku_info(_, message: Message):
    # Heroku API URL for account information
    heroku_account_url = "https://api.heroku.com/account"

    # Heroku API headers with API key
    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {heroku_api_key}",
    }

    try:
        # Make the API request to retrieve account information
        account_response = requests.get(heroku_account_url, headers=headers)

        # Check if the request was successful
        if account_response.status_code == 200:
            account_info = account_response.json()
            
            # Get a list of all apps
            heroku_conn = from_key(heroku_api_key)
            apps = heroku_conn.apps()
            
            # Extract app names and dyno information
            app_info_list = []
            total_dynos = 0
            for heroku_app in apps:
                app_name = heroku_app.name
                dynos_on = any(1 for dyno in heroku_app.dynos() if dyno.state == 'up')
                dyno_count = len(list(heroku_app.dynos()))
                total_dynos += dyno_count
                app_info_list.append((app_name, dynos_on, dyno_count))
            
            total_apps = len(app_info_list)
            
            info_text = (
                f"⍟Mᴜʟᴛɪ-Fᴀᴄᴛᴏʀ Aᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ➪ {account_info['two_factor_authentication']}\n\n"
                f"⍟Eᴍᴀɪʟ Aᴅᴅʀᴇss ➪ {account_info['email']}\n\n"
                f"⍟Nᴀᴍᴇ ➪ {account_info['name']}\n\n\n"
                f"⍟Tᴏᴛᴀʟ Aᴘᴘs➪ {total_apps}\n\n\n"
                f"⍟Tᴏᴛᴀʟ Dʏɴᴏs ➪{total_dynos}\n\n\n"
            )
            
            for app_name, dynos_on, dyno_count in app_info_list:
                info_text += f"\n━━━━━━━━━━━━━━━━━━━━━━Aᴘᴘ: {app_name}, \n Dʏɴᴏs: {'On' if dynos_on else 'Off'}, \n Tᴏᴛᴀʟ Dʏɴᴏs: {dyno_count} ━━━━━━━━━━━━━━━━━━━━━━\n"
            
            await message.reply_text(info_text)
        else:
            await message.reply_text(f"Error retrieving Heroku account information: {account_response.text}")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")
#----------------- ---------------------------------------------

def delete_heroku_app(app_name):
    heroku_conn = from_key(heroku_api_key)

    if not heroku_conn.apps().get(app_name):
        return f"App '{app_name}' not found on Heroku."

    app = heroku_conn.apps()[app_name]
    
    # Delete the Heroku app
    app.delete()
    
    return f"Heroku app '{app_name}' has been deleted."

@app.on_message(filters.command("delheroku") & filters.user(OWNER_ID))
async def delete_heroku_command(client, message):
    try:
        _, app_name = message.text.split(" ", 1)
        response = delete_heroku_app(app_name)
        await message.reply_text(response)
    except ValueError:
        await message.reply_text("Invalid command format. Use /delheroku <app_name>")
    except Exception as e:
        await message.reply_text(f"Error deleting Heroku app: {str(e)}")


# ----------------------- ------# ----------------------- ------# ----------------------- ------# ----------------------- ------
def get_heroku_variables(app_name):
    heroku_conn = from_key(heroku_api_key)

    if not heroku_conn.apps().get(app_name):
        return f"App '{app_name}' not found on Heroku."

    app = heroku_conn.apps()[app_name]
    
    # Get all config vars (environment variables) for the Heroku app
    config_vars = app.config().to_dict()
    
    # Save config vars to a file named 'variables.txt'
    with open('variables.txt', 'w') as file:
        for key, value in config_vars.items():
            file.write(f"{key}={value}\n")
    
    return f"Environment variables for app '{app_name}' saved to 'variables.txt'."

@app.on_message(filters.command("veriable") & filters.user(OWNER_ID))
async def heroku_variables_command(client, message):
    try:
        _, app_name = message.text.split(" ", 1)
        response = get_heroku_variables(app_name)
        await message.reply_text(response)
        await message.reply_document("variables.txt")  # Send the variables file
        os.remove("variables.txt")  # Remove the file after sending
    except ValueError:
        await message.reply_text("Invalid command format. Use /veriable <app_name>")
    except Exception as e:
        await message.reply_text(f"Error fetching Heroku environment variables: {str(e)}")

# ----------------------# ----------------------# ----------------------

def get_all_heroku_apps():
    heroku_conn = from_key(heroku_api_key)
    
    # Get a list of all apps
    apps = heroku_conn.apps()
    
    # Extract app names
    app_names = [app.name for app in apps]
    
    return app_names

@app.on_message(filters.command("apps") & filters.user(OWNER_ID))
async def heroku_apps_command(client, message):
    try:
        app_names = get_all_heroku_apps()
        if app_names:
            response = "\n".join(app_names)
        else:
            response = "No Heroku apps found for the account."
        await message.reply_text(response)
    except Exception as e:
        await message.reply_text(f"Error fetching Heroku apps: {str(e)}")



# --------------------# --------------------# --------------------
def restart_heroku_dynos(app_name):
    heroku_api_url = f"https://api.heroku.com/apps/{app_name}/dynos"

    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {heroku_api_key}",
    }

    # Restart all dynos by deleting them
    response = requests.delete(heroku_api_url, headers=headers)

    print(f"Heroku API Response: {response.status_code}")
    print(f"Heroku API Response Text: {response.text}")

    if response.status_code == 200:
        return True
    else:
        return False

# Command to restart all dynos for a Heroku app
@app.on_message(filters.command("restartdynos") & filters.user(OWNER_ID))
async def heroku_restart_dynos_command(client, message):
    try:
        _, app_name = message.text.split(" ", 1)

        if restart_heroku_dynos(app_name):
            await message.reply_text("Dynos restarted successfully.")
        else:
            await message.reply_text(f"ʀᴇsᴇᴛᴛɪɴɢ.............")
    except ValueError:
        await message.reply_text("Invalid command format. Use /restartdynos <app_name>")
    except Exception as e:
        await message.reply_text(f"Error restarting dynos: {str(e)}")
