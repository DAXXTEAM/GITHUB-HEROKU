import asyncio, os, time, aiohttp, random, requests
from requests.adapters import HTTPAdapter, Retry
from pyrogram.types import Message, ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegraph import upload_file
from config import OWNER_ID, BOT_USERNAME
import config
import httpx
from datetime import datetime
from pyrogram import filters, Client, enums
from daxxop import daxxop as app
import git, shutil


# --------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

@app.on_message(filters.command('info'))
async def myinfo_command(client, message):
    user = message.from_user

    if len(message.command) > 1:
        
        try:
            user_id = int(message.command[1])
            user = await app.get_users(user_id)
        except ValueError:
            await app.send_message(chat_id=message.chat.id, text="𝖨𝖭𝖵𝖠𝖫𝖨𝖣 𝖴𝖲𝖤𝖱 𝖨𝖣.")
            return

    user_info = (
        f"๏─╼⃝𖠁๏**𝖴𝖲𝖤𝖱 𝖨𝖭𝖥𝖮**๏𖠁⃝╾─๏\n"
        f"┏━━━━━━━━━━━━━━━━━⧫\n"
        f"┠ ◆ **𝖨𝖣: `{user.id}`**\n"
        f"┠ ◆ **𝖴𝖲𝖤𝖱𝖭𝖠𝖬𝖤: @{user.username}**\n"
        f"┠ ◆ **𝖥𝖨𝖱𝖲𝖳 𝖭𝖠𝖬𝖤: {user.first_name}**\n"
        f"┠ ◆ **𝖫𝖠𝖲𝖳 𝖭𝖠𝖬𝖤: {user.last_name}**\n"
        f"┠ ◆ **𝖴𝖲𝖤𝖱 𝖫𝖨𝖭𝖪: {user.mention}**"
        f"┗━━━━━━━━━━━━━━━━━⧫"
    )

    
    await app.send_message(chat_id=message.chat.id, text=user_info)
    

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

@app.on_message(filters.command("repo"))
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/GITHUB-HEROKU/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/DAXXTEAM/GITHUB-HEROKU) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/HEROKUFREECC)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------


def download_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session = requests.Session()
    session.mount('http://', HTTPAdapter(max_retries=retries))

    try:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to download source code. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
@app.on_message(filters.command("html"))
def web_download(client, message):
    # Check if the command has a URL attached
    if len(message.command) == 1:
        message.reply_text("Please enter a URL along with the /html command.")
        return

    url = message.command[1]

    source_code = download_website(url)
    if source_code.startswith('An error occurred') or source_code.startswith('Failed to download'):
        message.reply_text(source_code)
    else:
        # Save the source code to a file
        with open('website.txt', 'w', encoding='utf-8') as file:
            file.write(source_code)

        # Reply with the file
        message.reply_document(document='website.txt', caption=f"Source code of {url}")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
def get_pypi_info(package_name):
    try:
        
        api_url = f"https://pypi.org/pypi/{package_name}/json"
        
        response = requests.get(api_url)
        pypi_info = response.json()
        
        return pypi_info
    
    except Exception as e:
        print(f"Eʀʀᴏʀ ғᴇᴛᴄʜɪɴɢ PʏPɪɴғᴏʀᴍᴀᴛɪᴏɴ: {e}")
        return None
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
@app.on_message(filters.command("pypi", prefixes="/"))
def pypi_info_command(client, message):
    try:
       
        package_name = message.command[1]
        
        
        pypi_info = get_pypi_info(package_name)
        
        if pypi_info:
            
            info_message = f"๏ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ➪ {pypi_info['info']['name']}\n━━━━━━━━━━━━━━━━━━━━━" \
                           f"๏ Lᴀᴛᴇsᴛ ᴠɪʀsɪᴏɴ➪ {pypi_info['info']['version']}\n━━━━━━━━━━━━━━━━━━━━━" \
                           f"๏ Dᴇsᴄʀɪᴘᴛɪᴏɴ➪ {pypi_info['info']['summary']}\n━━━━━━━━━━━━━━━━━━━━━" \
                           f"๏ ᴘʀᴏJᴇᴄᴛ ᴜʀʟ➪ {pypi_info['info']['project_urls']['Homepage']}"
            
            
            client.send_message(message.chat.id, info_message)
        
        else:
            
            client.send_message(message.chat.id, "Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ PʏPI")
    
    except IndexError:

        client.send_message(message.chat.id, "Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ /pypi ᴄᴏᴍᴍᴀɴᴅ.")
       
# -------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("**🎙️ 𝖵𝗈𝗂𝖼𝖾 𝖼𝗁𝖺𝗍 𝗌𝗍𝖺𝗋𝗍𝖾𝖽!**")

# ----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------- #
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**🔇 𝖵𝗈𝗂𝖼𝖾 𝖼𝗁𝖺𝗍 𝖾𝗇𝖽𝖾𝖽. 𝖳𝗁𝖺𝗇𝗄𝗌 𝖿𝗈𝗋 𝗃𝗈𝗂𝗇𝗂𝗇𝗀**")

# ----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------- #
@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ☄️")
           except:
             pass

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("leavegroup")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"ɢᴏᴏᴅ ʙʏᴇ ʙᴀʙʏ🫡"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)
    
# --------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------
@app.on_message(filters.command(["tgm" , "telegraph"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("ᴍᴀᴋɪɴɢ ᴀ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴡᴀɪᴛ ᴀ sᴇᴄ.")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}')
#--------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_message(filters.command("table"))
def multiplication_table(_, message: Message):
    try:
        
        number = int(message.text.split()[1])

        table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 11)])

        
        message.reply_text(f"Multiplication table of {number}:\n\n{table}")
    except IndexError:
        message.reply_text("Please enter a valid number after the command /table.")
    except ValueError:
        message.reply_text("Invalid input. Please enter a valid number.")
# --------------------------------------------------------------------------------- #
#--------------------------------------------------------------------------
@app.on_message(filters.command("id"))
def get_user_chat_id(_: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    response_text = (
        f"ʏᴏᴜʀ ɪᴅ: `{user_id}`\n"
        f"ᴄʜᴀᴛ ɪᴅ: `{chat_id}`"
    )

    message.reply_text(response_text)
# --------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()

# --------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------- #


@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git DAXXTEAM")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']

                caption = f"""ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}
                
ᴜsᴇʀɴᴀᴍᴇ: {username}
ʙɪᴏ: {bio}
ʟɪɴᴋ: [Here]({url})
ᴄᴏᴍᴩᴀɴʏ: {company}
ᴄʀᴇᴀᴛᴇᴅ ᴏɴ: {created_at}
ʀᴇᴩᴏsɪᴛᴏʀɪᴇs: {repositories}
ʙʟᴏɢ: {blog}
ʟᴏᴄᴀᴛɪᴏɴ: {location}
ғᴏʟʟᴏᴡᴇʀs: {followers}
ғᴏʟʟᴏᴡɪɴɢ: {following}"""

            except Exception as e:
                print(str(e))
                pass
# --------------------------------------------------------------------------------- #
    
    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("๏ ᴄʟᴏsᴇ ๏", callback_data="close_data")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])
# --------------------------------------------------------------------------------- #
    
    # Send the message with the inline keyboard
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=inline_keyboard)
# --------------------------------------------------------------------------------- #
# Function to chunk the repository info into smaller parts
def chunk_string(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

@app.on_message(filters.command("allrepo"))
async def all_repo_command(client, message):
    try:
        # Check if there is a GitHub username after the /giverepo command
        if len(message.command) > 1:
            github_username = message.command[1]

            # Fetch information about all repositories of the GitHub user
            repo_info = get_all_repository_info(github_username)

            # Split repository info into smaller chunks
            chunked_repo_info = chunk_string(repo_info, 4000)  # Split into chunks of 4000 characters

            # Send the repository information in chunks as separate messages
            for chunk in chunked_repo_info:
                await message.reply_text(chunk)
        else:
            await message.reply_text("Please enter a GitHub username after the /allrepo command.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
#######

def get_all_repository_info(github_username):
    # Set up the GitHub API URL for user repositories
    github_api_url = f"https://api.github.com/users/{github_username}/repos"

    # Perform the request to the GitHub API
    response = requests.get(github_api_url)
    data = response.json()

    # Extract relevant information from the response
    repo_info = "\n\n".join([
        f"Repository: {repo['full_name']}\n"
        f"Description: {repo['description']}\n"
        f"Stars: {repo['stargazers_count']}\n"
        f"Forks: {repo['forks_count']}\n"
        f"URL: {repo['html_url']}"
        for repo in data
    ])

    return repo_info




#------------------



@app.on_message(filters.command(["downloadrepo"]))
def download_repo(_, message):
    if len(message.command) != 2:
        message.reply_text("Please provide the GitHub repository URL after the command. Example: /downloadrepo Repo Url ")
        return

    repo_url = message.command[1]
    zip_path = download_and_zip_repo(repo_url)

    if zip_path:
        with open(zip_path, "rb") as zip_file:
            message.reply_document(zip_file)
        os.remove(zip_path)
    else:
        message.reply_text("Unable to download the specified GitHub repository.")


def download_and_zip_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"{repo_name}"
        
        # Clone the repository
        repo = git.Repo.clone_from(repo_url, repo_path)
        
        # Create a zip file of the repository
        shutil.make_archive(repo_path, 'zip', repo_path)

        return f"{repo_path}.zip"
    except Exception as e:
        print(f"Error downloading and zipping GitHub repository: {e}")
        return None
    finally:
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
