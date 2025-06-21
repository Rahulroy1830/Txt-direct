#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22069945"))
API_HASH = environ.get("API_HASH", "132b647b2919a6954ddc1d4f378fcb55")
BOT_TOKEN = environ.get("BOT_TOKEN", "8080946229:AAH--TPimuKdE1mliBtArpvV79p4oR0zJ6I")
OWNER = int(environ.get("OWNER", "1447424345"))
CREDIT = "Rahul roy"
AUTH_USER = os.environ.get('AUTH_USERS', '1447424345').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
