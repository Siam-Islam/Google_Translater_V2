from googletrans import Translator
from pyrogram import Client, filters
from helper.database import find , insert

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
          insert(int(message.chat.id))
          await message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",reply_to_message_id = message.id , reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],                 [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical"),InlineKeyboardButton("How To Use",url = "https://youtu.be/dUYvenXiYKE") ]           ]        ) )
            
            
@Client.on_message(filters.private & filters.text)
async def echo(client, message):
              code =find(int(message.chat.id)) 
	  except Exception as e:
	      print("error")
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
					await message.reply_text(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```")
			except Exception as e:
					await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```")
	else:
		await  message.reply_text("Set language first.")
