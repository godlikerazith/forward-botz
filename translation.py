# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

import os
from config import Config

class Translation(object):
  START_TXT = """<b>ʜɪ {} ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ?

ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
ɪ ᴄᴀɴ ꜰᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ꜰʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ

ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ</b>"""


  DONATE_TXT = """<blockquote><b>If you liked my service</blockquote>
  <blockquote>Consider make support my developer🧑‍💻</blockquote>
  <blockquote>We don't need donation if you like our service then share with your friends that is donation for us 💙</b></blockquote>"""

  HELP_TXT = """<b><u>🔆 ʜᴇʟᴘ</b></u>

<u>**📚 Available Commands:**</u>
<blockquote><b>⏣ __/start - Check I'm alive__ 
⏣ __/forward - Forward messages__
⏣ __/unequify - Delete duplicate messages in channels__
⏣ __/settings - Configure your settings__
⏣ __/reset - Reset your settings__
⏣ __/donate - Donate to developer__
⏣ __/stop - Cancel your ongoing forwarding__</b></blockquote>

<b><u>💢 Features:</b></u>
<blockquote><b>► __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission__
► __Forward message from private channel to your channel by using userbot(user must be member in there)__
► __Custom caption__
► __Custom button__
► __Support restricted chats__
► __Skip duplicate messages__
► __Filter type of messages__
► __Skip messages based on extensions & keywords & size__</b></blockquote>
"""
# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
<blockquote><b>► __add a bot or userbot__
► __add atleast one to channel__ `(your bot/userbot must be admin in there)`
► __You can add chats or bots by using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
► __Then use /forward to forward messages__</b></blockquote>"""

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay
  
  ABOUT_TXT = """<b>
╔════❰ ᴀᴜᴛᴏ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ʙᴏᴛ : ғᴏʀᴡᴀʀᴅ ʙᴏᴛ
║┣⪼🧑‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://telegram.me/sahedsarker'>sᴀʜᴇᴅ sᴀʀᴋᴇʀ</a>
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : <a href='https://Heroku.com'>ʜᴇʀᴏᴋᴜ</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'> ᴘʏᴛʜᴏɴ 3 </a>
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 1.0.6 [sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay 
  
  STATUS_TXT = """<b>
╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs  ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼👱 ᴛᴏᴛᴀʟ  ᴜsᴇʀs : <code>{}</code>
║┃
║┣⪼🤖 ᴛᴏᴛᴀʟ ʙᴏᴛ : <code>{}</code>
║┃
║┣⪼🔃 ғᴏʀᴡᴀʀᴅɪɴɢs : <code>{}</code>
║┃
║┣⪼🔍 ᴜɴᴇǫᴜɪꜰʏɪɴɢs: <code>0</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>""" 

  SERVER_TXT = """<b>
╔════❰ sᴇʀᴠᴇʀ sᴛᴀᴛs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ ᴛᴏᴛᴀʟ ᴅɪsᴋ sᴘᴀᴄᴇ: <code>679 GB</code>
║┣⪼ ᴜsᴇᴅ: <code>1.54 GB</code>
║┣⪼ ꜰʀᴇᴇ: <code>36.46 GB</code>
║┣⪼ ᴄᴘᴜ: <code>{}%</code>
║┣⪼ ʀᴀᴍ: <code>{}%</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪</b>"""
  
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"

  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"

  SKIP_MSG = "<b><u>sᴇᴛ ɴᴏ. ᴏғ ᴍᴇssᴀɢᴇs ᴛᴏ sᴋɪᴘ 📃</u></b>\n\n<b>You can skip a certain number of messages and forward the rest.\n\nDefault Skip Number = 0</b>\n\n<b><i>Example: If you enter 0, no messages will be skipped.\nIf you enter 5, the first 5 messages will be skipped.</i></b>\n/cancel <b>- cancel this process</b>"

  CANCEL = "<b>Process Cancelled Succefully !</b>"

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"

  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """<b>╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs  ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼<b>𖨠 ᴛᴏᴛᴀʟ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ғᴇᴄʜᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ғᴏʀᴡᴀʀᴅᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴅᴇʟᴇᴛᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 sᴋɪᴘᴘᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ғɪʟᴛᴇʀᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴘᴇʀᴄᴇɴᴛᴀɢᴇ: </b> <code>{}</code>%
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ <b>{}</b> ❱══❍⊱❁"""

# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay

  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay
 
  DOUBLE_CHECK = """<b><u>ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋɪɴɢ 📋</b></u>

<b>ʙᴇꜰᴏʀᴇ ꜰᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ ᴍᴇssᴀɢᴇs ᴄʟɪᴄᴋ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴏɴʟʏ ᴀꜰᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ</b>


<b>★ ʏᴏᴜʀ ʙᴏᴛ: {botname}</b>
<b>★ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ: {from_chat}</b>
<b>★ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ: {to_chat}</b>
<b>★ sᴋɪᴘ ᴍᴇssᴀɢᴇs: {skip}</b>

<i><b>° {botname} ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ</i> ({to_chat})</b>
<i><b>° ɪꜰ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ ɪs ᴘʀɪᴠᴀᴛᴇ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴍᴇᴍʙᴇʀ ᴏʀ ʏᴏᴜʀ ʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇʀᴇ ᴀʟsᴏ</b></i>

<b>ɪꜰ ᴛʜᴇ ᴀʙᴏᴠᴇ ɪs ᴄʜᴇᴄᴋᴇᴅ ᴛʜᴇɴ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴄᴀɴ ʙᴇ ᴄʟɪᴄᴋᴇᴅ</b>"""


# Repo By @SahedSarker
# Don't Remove Editing Credit 
# If You Already Removed, Congratulations You Are Gay
