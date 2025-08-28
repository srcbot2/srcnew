#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21240850"))
API_HASH = environ.get("API_HASH", "593eec13b2638de5e9bb4284ea8631ec")
BOT_TOKEN = environ.get("BOT_TOKEN", "s8427961753:AAEfQ5LSfcfuM4IlDzwfI6a4qJOV6yXoMaA")

OWNER = int(environ.get("OWNER", "6662470778"))
CREDIT = environ.get("CREDIT", "💞𝗔𝗹𝗲𝘅 𝗔𝗿𝘆𝗮💞")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set




