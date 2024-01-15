from pyrogram import Client, filters
import requests
from daxxop import daxxop as bot


# Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
github_token = "YOUR GIT TOKEN"

@bot.on_message(filters.command(["gitprivate", "gitpublic"]))
def change_repo_visibility(client, message):
    try:
        # Ensure that only the owner can use these commands
        if message.from_user.id != OWNER_ID:
            message.reply_text("You are not authorized to use this command.")
            return

        # Extracting GitHub repository URL from the command
        url = message.text.split(" ", 1)[1].strip()

        # Assuming the URL is in the format 'https://github.com/user/repo'
        parts = url.split("/")
        username, repo_name = parts[-2], parts[-1]

        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
        headers = {"Authorization": f"token {github_token}"}

        # Determine whether to set the repository to private or public
        is_private = True if message.command[0] == "gitprivate" else False

        # Change repository visibility using GitHub API
        response = requests.patch(f"https://api.github.com/repos/{username}/{repo_name}", json={"private": is_private}, headers=headers)

        if response.status_code == 200:
            visibility_status = "private" if is_private else "public"
            message.reply_text(f"Repository {username}/{repo_name} set to {visibility_status}.")
        else:
            message.reply_text(f"Failed to set repository visibility. Status code: {response.status_code}")

    except IndexError:
        message.reply_text(f"Please provide a valid GitHub repository URL after the /{message.command[0]} command.")
    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")