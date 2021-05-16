from telegram import *
from telegram.ext import *

bot = Bot('1670301842:AAED5L-M26u2qeX2SsFOXPZUsof-iVxxb68')
updater = Updater("1670301842:AAED5L-M26u2qeX2SsFOXPZUsof-iVxxb68", use_context=True)
dispatcher = updater.dispatcher
dp = updater.dispatcher

def greet(update:Update, context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='Welcome to News and weather bot')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='/news - Top 10 headlines')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='/weather - Get weather details')