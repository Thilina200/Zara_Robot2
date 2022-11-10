import os
from telethon import Button
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Main Details
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
INLINE_THUMB = os.environ.get("INLINE_THUMB", "https://graph.org/file/3b01319fd2a830edddea3.jpg")
BOT_STARTED = '''
  ___      _     ___ _            _          _ 
 | _ ) ___| |_  / __| |_ __ _ _ _| |_ ___ __| |
 | _ \/ _ \  _| \__ \  _/ _` | '_|  _/ -_) _` |
 |___/\___/\__| |___/\__\__,_|_|  \__\___\__,_|
				O_O Zara Robot ✨ v1.0.2
				Powered By Pyrogram & Telethon
				Using Firebase as a Database
				Developed By Hi Tech Rocket  </>  
'''
LOG_CHNL = os.environ.get("LOG_CHNL", "-1001725384953")
FDBURL = os.environ.get("FDBURL")
# Start Message
START_MSG = os.environ.get("START_MSG", "🌷 Hi There {}🔥,\n**I am Zara Robot ✨...**")
START_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('🌹 Help', callback_data='help'),
		 InlineKeyboardButton('About 🌷', callback_data='about')],
		[InlineKeyboardButton("➕ Add Zara Robot  to Your Group ➕", url="t.me/Miss_Zara_Bot?startgroup=true")]
	])
WELCOME_TEXT = os.environ.get("WELCOME_TEXT", "Hey There, Welcome!")
RULES_TXT = os.environ.get("RULES_TXT", "No Rules. Use Me Freely🤗.")

# Inline About
INLINE_ABOUT_TITLE = os.environ.get("INLINE_ABOUT_TITLE", "Zara Robot ✨")
INLINE_ABOUT_THUMB = os.environ.get("INLINE_ABOUT_THUMB", "")
INLINE_ABOUT_DES = os.environ.get("INLINE_ABOUT_DES", "A Simple Group Managing Bot...")
INLINE_ABOUT_MSG = os.environ.get("INLINE_ABOUT_MSG", "<b><u>✨ A Project Of Hi Tech Bot ⚡</u></b>\n\n🌹 So, You Can Use This Bot Freely...🍁 & Also Please Be Kind Share This Bot With Others If it\'s Not Bad...\n\n💖 If You Have Any Questions... Please Contact Us🤗...🌺")
INLINE_ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('🖤┅𝐌𝐫 𝐃𝐚𝐫𝐤𝐑𝐢𝐝𝐞𝐫*⃟🔥᭄ ᭄ ⦁♡࿔ ', url='https://t.me/DarkRIder2003'),
		 InlineKeyboardButton('$เƚԋเʝα▁ƚԃ [ᴄɢꜱ™]', url='https://t.me/Sithijatd')],
		[InlineKeyboardButton('🤞 Hi Tech Rocket 🤞',
		                      url='https://t.me/HiTechRockets')],
		[InlineKeyboardButton('🍁 Support 🍁',
		                      url='https://t.me/HiTechRockets')],
		[InlineKeyboardButton('🍀 Inline Again 🍀',
		                      switch_inline_query_current_chat='')]
	])


# About Message
ABOUT_MSG = os.environ.get("ABOUT_MSG", "<b><u>✨ A Project Of Team SL Bots ⚡</u></b>\n\n🌹 So, You Can Use This Bot Freely...🍁 & Also Please Be Kind Share This Bot With Others If it\'s Not Bad...\n\n💖 If You Have Any Questions... Please Contact Us🤗...🌺")
ABOUT_BTNS = InlineKeyboardMarkup([
		[InlineKeyboardButton('🖤┅𝐌𝐫 𝐃𝐚𝐫𝐤𝐑𝐢𝐝𝐞𝐫*⃟🔥᭄ ᭄ ⦁♡࿔ ', url='https://t.me/DarkRIder2003'),
		 InlineKeyboardButton('$เƚԋเʝα▁ƚԃ [ᴄɢꜱ™]', url='https://t.me/Sithijatd')],
		[InlineKeyboardButton('🤞 Hi Tech Rocket 🤞',
		                      url='https://t.me/HiTechRockets')],
		[InlineKeyboardButton('🍁 Support 🍁',
		                      url='https://t.me/HiTechRockets')],
		[InlineKeyboardButton('💠 Help', callback_data='help'),
		 InlineKeyboardButton('Close ✖️', callback_data='close')]
	])



