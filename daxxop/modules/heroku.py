import os
import time
import requests
import config
from pyrogram.types import Message
from pyrogram import Client, filters
from heroku3 import from_key
from daxxop import daxxop as app
from config import OWNER_ID, HEROKU_API

# ----------------------- ------# ----------------------- ------

HEROKU_API = config.HEROKU_API

# ----------------------- ------# ----------------------- ------
# --------------------------------------------------------------------------------

@app.on_message(filters.command("createapp") & filters.user(OWNER_ID))
async def create_app_command(client, message):
    
    app_name = message.text.split("/createapp")[1].strip()

    
    if not app_name:
        await message.reply("Please provide a name for the Heroku app.")
        return

    
    heroku_api_url = "https://api.heroku.com/apps"

    
    headers = {
        "Accept": "application/vnd.heroku+json; version=3",
        "Authorization": f"Bearer {HEROKU_API}",
    }

    
    payload = {"name": app_name}

    
    response = requests.post(heroku_api_url, json=payload, headers=headers)

    
    if response.status_code == 201:
        await message.reply(f"Heroku app '{app_name}' created successfully!")
    else:
        await message.reply(f"Failed to create Heroku app. Error: {response.text}")



# --------------------------------------------------------------------------------------------


 #Function to add collaboration
def add_collaboration(app_name, email):
    heroku_conn = from_key(HEROKU_API)
    
    if not heroku_conn.apps().get(app_name):
        return f"App '{app_name}' not found on Heroku."
    
    app_instance = heroku_conn.apps()[app_name]
    
    try:
        collaborator = app_instance.add_collaborator(email)
        return f"Collaboration added for app '{app_name}' with email '{email}'."
    except Exception as e:
        return f"Error adding collaboration: {str(e)}"

# Function to remove collaboration
def remove_collaboration(app_name, email):
    heroku_conn = from_key(HEROKU_API)
    
    if not heroku_conn.apps().get(app_name):
        return f"App '{app_name}' not found on Heroku."
    
    app_instance = heroku_conn.apps()[app_name]
    
    try:
        collaborator = app_instance.remove_collaborator(email)
        return f"Collaboration removed for app '{app_name}' with email '{email}'."
    except Exception as e:
        return f"Error removing collaboration: {str(e)}"

# Command to add collaboration
@app.on_message(filters.command("addapp") & filters.user(OWNER_ID))
async def add_collaboration_command(client, message):
    try:
        _, app_name, email = message.text.split(" ", 2)
        response = add_collaboration(app_name, email)
        await message.reply_text(response)
    except ValueError:
        await message.reply_text("Invalid command format. Use /addapp <app_name> <email>")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")

# Command to remove collaboration
@app.on_message(filters.command("removeapp") & filters.user(OWNER_ID))
async def remove_collaboration_command(client, message):
    try:
        _, app_name, email = message.text.split(" ", 2)
        response = remove_collaboration(app_name, email)
        await message.reply_text(response)
    except ValueError:
        await message.reply_text("Invalid command format. Use /removeapp <app_name> <email>")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")

#---------------
def get_heroku_logs(app_name):
    heroku_conn = from_key(HEROKU_API)

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
        "Authorization": f"Bearer {HEROKU_API}",
    }

    try:
        # Make the API request to retrieve account information
        account_response = requests.get(heroku_account_url, headers=headers)

        # Check if the request was successful
        if account_response.status_code == 200:
            account_info = account_response.json()
            
            # Get a list of all apps
            heroku_conn = from_key(HEROKU_API)
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
                f"⍟Mᴜʟᴛɪ-Fᴀᴄᴛᴏʀ Aᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ➪ {account_info['two_factor_authentication']}\n"
                f"⍟Eᴍᴀɪʟ Aᴅᴅʀᴇss ➪ {account_info['email']}\n"
                f"⍟Nᴀᴍᴇ ➪ {account_info['name']}\n"
                f"⍟Tᴏᴛᴀʟ Aᴘᴘs➪ {total_apps}\n"
                f"⍟Tᴏᴛᴀʟ Dʏɴᴏs ➪{total_dynos}\n"
            )
            
            for app_name, dynos_on, dyno_count in app_info_list:
                info_text += f"\n━━━━━━━━━━━━━━━━━━━━━━\nAᴘᴘ: {app_name}, \n Dʏɴᴏs: {'On' if dynos_on else 'Off'}, \n Tᴏᴛᴀʟ Dʏɴᴏs: {dyno_count}\n━━━━━━━━━━━━━━━━━━━━━━\n"
            
            await message.reply_text(info_text)
        else:
            await message.reply_text(f"Error retrieving Heroku account information: {account_response.text}")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")
#----------------- ---------------------------------------------

def delete_heroku_app(app_name):
    heroku_conn = from_key(HEROKU_API)

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
    heroku_conn = from_key(HEROKU_API)

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
    heroku_conn = from_key(HEROKU_API)
    
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
        "Authorization": f"Bearer {HEROKU_API}",
    }

    # Restart all dynos by deleting them
    response = requests.delete(heroku_api_url, headers=headers)

    print(f"Heroku API Response: {response.status_code}")
    print(f"Heroku API Response Text: {response.text}")

    if response.status_code == 200:
        return True
    else:
        return False

# --------------------------
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



# ----------------------------


@app.on_message(filters.command("rename") & filters.user(OWNER_ID))
def rename_app(client, message):
    # ----------------------------------------------------------------
    command_parts = message.text.split()
    
    if len(command_parts) != 3:
        # ------------------------------------------------------------
        response_text = "Enter a valid command: /rename {old_app_name} {new_app_name} "
        message.reply_text(response_text)
        return

    _, old_app_name, new_app_name = command_parts

    heroku_api_key = config.HEROKU_API

    # -------------------------------------------------------------------------
    headers = {
        "Authorization": f"Bearer {heroku_api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
    }

    # -------------------------------------------------------------------
    app_info_url = f"https://api.heroku.com/apps/{old_app_name}"
    app_info_response = requests.get(app_info_url, headers=headers)
    app_info_response.raise_for_status()
    app_info = app_info_response.json()

    # --------------------------------------------------------------------
    rename_url = f"https://api.heroku.com/apps/{app_info['id']}"
    rename_payload = {"name": new_app_name}
    rename_response = requests.patch(rename_url, json=rename_payload, headers=headers)
    rename_response.raise_for_status()

    # --------------------------------
    response_text = f"Heroku app '{old_app_name}' has been renamed to '{new_app_name}'."
    message.reply_text(response_text)


#---------------
