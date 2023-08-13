import requests

BOT_TOKEN = ''   # bot token
chat_username = ''  # If the group has a username

url = f'https://api.telegram.org/bot{BOT_TOKEN}/getChat?chat_id=@{chat_username}'

response = requests.get(url)
data = response.json()

# The chat ID can be extracted from the response
chat_id = data['result']['id']

print(f"The chat ID of the group is: {chat_id}")
