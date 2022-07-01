import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int('') # insert API id
API_HASH = '' # API HASh
BOT_TOKEN = '' # Bot

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in ''.split()] # insert admin id
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in ''.split()] # insert channel id
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()] #auth users
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = '' #auth channel
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = '' #database URL
DATABASE_NAME = '' #database name
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hola!! 💖 **

`Use the below buttons to search files or send me the name of file to search.`
😊😊😊😊😊😊😊😊
"""

START_MSG = environ.get('START_MSG', default_start_msg)
