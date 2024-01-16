import os
from pyrogram import Client, filters
from heroku3 import from_key
from daxxop import daxxop as app
from config import OWNER_ID

# ----------------------- ------# ----------------------- ------

heroku_api_key = '90c67d1a-5bc5-4fe2-898b-93910774096b'

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
