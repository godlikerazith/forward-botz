import datetime
from os import environ 

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

class Config:
    API_ID = environ.get("API_ID", "26656618")
    API_HASH = environ.get("API_HASH", "2850721c73dbc207b5cf15362c28a66c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8044056667:AAE7KbKndJ6iL7mwxgZwKhE4Jgw9rdg-kEs") 
    BOT_SESSION = environ.get("BOT_SESSION", "RS_Forward_Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ghostcm83:2YpZjH8pafFc9ZJh@cluster0.ohbn7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1918079773').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002423270359'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay
