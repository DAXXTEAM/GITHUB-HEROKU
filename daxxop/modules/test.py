from pyrogram import Client, filters
import subprocess
import os
from github import Github
import requests
from daxxop import daxxop as app 
import config


GITHUB_API_TOKEN = config.GIT_TOKEN

GITHUB_API_URL = "https://api.github.com/user/repos"


LOGGER_GROUP_CHAT_ID = -1001802990747



def send_notification(message):
    app.send_message(LOGGER_GROUP_CHAT_ID, message)


def perform_git_pull(local_repo_path):
    try:
        # Perform git pull in the local repository
        os.chdir(local_repo_path)
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        send_notification(f"Git Pull Result:\n\n{result.stdout}\n\n{result.stderr}")
    except Exception as e:
        send_notification(f"Error during git pull:\n\n{str(e)}")


def get_all_repositories():
    # Use GitHub API to get all repositories associated with the account
    headers = {"Authorization": f"Bearer {GITHUB_API_TOKEN}"}
    response = requests.get(GITHUB_API_URL, headers=headers)
    response.raise_for_status()
    repositories = response.json()
    return repositories


def check_github_for_updates():
    all_repositories = get_all_repositories()

    for repo in all_repositories:
        repo_name = repo["name"]
        local_repo_path = f"/path/to/local/repositories/{repo_name}"  # Adjust the path as needed

        if not os.path.exists(local_repo_path):
            # Clone the repository if it doesn't exist locally
            subprocess.run(["git", "clone", repo["clone_url"], local_repo_path])

        # Check for updates in each repository
        latest_commit_sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=local_repo_path, capture_output=True, text=True).stdout.strip()
        if latest_commit_sha != repo["default_branch"]:
            send_notification(f"New commit detected in {repo_name}. Updating local repository...")
            perform_git_pull(local_repo_path)
