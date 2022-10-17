from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from helper.database import find , insert
from helper.list import list

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
          insert(int(message.chat.id))
          await message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",reply_to_message_id = message.id , reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],                 [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical"),InlineKeyboardButton("How To Use",url = "https://youtu.be/dUYvenXiYKE") ]           ]        ) )
            
            
@Client.on_message(filters.private & filters.text)
async def echo(client, message):
	keybord1= InlineKeyboardMarkup( [
        [ 
            InlineKeyboardButton("Afrikaans", callback_data='af'),
             InlineKeyboardButton("Albanian", callback_data='sq'),
            InlineKeyboardButton("Amharic",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Armenian", callback_data='hy'),      
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Basque",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusian",callback_data ="be"),       	
	InlineKeyboardButton("Bengali",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnian",callback_data = "bs"),
	InlineKeyboardButton("Bulgarian",callback_data ="bg"),
	InlineKeyboardButton("Catalan",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Corsican",callback_data ="co"),
	InlineKeyboardButton("Croatian",callback_data = "hr"),
	InlineKeyboardButton("Czech", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danish",callback_data = "da"),
	InlineKeyboardButton("Dutch",callback_data = "nl"),
	InlineKeyboardButton("Esperanto",callback_data = "eo")	 
	]
	] )
	try:
		code =find(int(message.chat.id))
	except Exception as e:
		await message.reply_text(f" Error : {e}\nclick /start ........")
		return 
		
	if code :
			try:
				translator = Translator()
				translation = translator.translate(message.text,dest = code)
			except Exception as e:
				await message.reply_text(f"Error : {e}")
				return
			try:
					for i in list:
						if list[i]==translation.src:
							fromt = i
						if list[i] == translation.dest:
							to = i
					await message.reply_text(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```\n\n join @lntechnical")
			except Exception as e:
					await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```\n\n join @lntechnical")
	else:
		await  message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup =keybord1)
