import datetime
from os import environ 

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

class Config:
    API_ID = environ.get("API_ID", "20059547")
    API_HASH = environ.get("API_HASH", "b399bfcd23ffc95ba7b20904fa5cb35f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7245210989:AAGCtSmRdHzaN6SroGKqiASKBBdrsdZb11k") 
    BOT_SESSION = environ.get("BOT_SESSION", "RS_Forward_Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ghostcm83:2YpZjH8pafFc9ZJh@cluster0.ohbn7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1918079773').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002423270359'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/All_In_One_Linkz") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
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
