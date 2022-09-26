import os
import telebot
 
# my_secret = os.environ['TOKEN'] #instead of TOKEN put a token of your bot here
bot= telebot.TeleBot(my_secret) 
@bot.message_handler(commands=["start"])  
def st(message):
  bot.send_message(message.chat.id,"hi")

sticker = "CAACAgIAAxkBAAEFyg1jGzVaX5cXVYdQ4jDY8-sEgSwZCAAChxUAAj0PUEnem2b91sejvykE"
@bot.message_handler(commands=["help"])
def help(message):
  bot.send_sticker(message.chat.id, sticker)

photo1 = 'https://cdn.igromania.ru/mnt/news/9/7/5/3/6/4/103232/437766a33cbf86a7_848x477.jpg'
@bot.message_handler(commands=["photo"])
def photo(message):
  bot.send_photo(message.chat.id, photo1)
 
@bot.message_handler(content_types=['text'])
def text_handler(message):
  if message.text.lower()=="привет":
    bot.send_message(message.chat.id,"И тебе привет!")
  else:
    bot.reply_to(message.chat.id,"Сообщение не равно привет!")

@bot.message_handler(['textme'])
def textme(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
          'Text Salima',url='telegram.me/mad_hatter01'
       )
   )
   bot.send_message(message.chat.id,"If you have any issues about my bot, please contact me by the button below",reply_markup=keyboard)
 
bot.polling(none_stop=True)
