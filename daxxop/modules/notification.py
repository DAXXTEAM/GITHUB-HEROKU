import requests
import config

def get_latest_commit(username, repo, token):
    
    api_url = f"https://api.github.com/repos/{username}/{repo}/commits"
    
    
    headers = {'Authorization': f'token {token}'}

    
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        
        latest_commit = response.json()[0]
        commit_message = latest_commit['commit']['message']
        commit_author = latest_commit['commit']['author']['name']
        
        return f"Latest commit by {commit_author}: {commit_message}"
    else:
        return f"Failed to fetch latest commit. Status code: {response.status_code}"

def send_telegram_notification(token, chat_id, message):
    
    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    
    params = {'chat_id': chat_id, 'text': message}

    
    response = requests.post(telegram_url, params=params)

    if response.status_code != 200:
        print(f"Failed to send notification to Telegram. Status code: {response.status_code}")


github_username = 'daxxteam'
github_repo = 'daxxmusic'
telegram_bot_token = config.BOT_TOKEN
github_token = config.GIT_TOKEN
telegram_chat_id = '@herokufreecc'


latest_commit_message = get_latest_commit(github_username, github_repo, github_token)


send_telegram_notification(telegram_bot_token, telegram_chat_id, latest_commit_message)
  
