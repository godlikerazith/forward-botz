import datetime
from os import environ 

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

class Config:
    API_ID = environ.get("API_ID", "")
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7245210989:AAGCtSmRdHzaN6SroGKqiASKBBdrsdZb11k") 
    BOT_SESSION = environ.get("BOT_SESSION", "RS_Forward_Bot") 
    DATABASE_URI = environ.get("DATABASE", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5072829406 1918079773').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/movie344") 
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
