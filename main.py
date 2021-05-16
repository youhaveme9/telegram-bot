from telegram import *
from telegram.ext import *
import requests
import pyowm
import greet

# API keys file
import API_KEY

bot = Bot(API_KEY.key_bot)
updater = Updater(API_KEY.key_bot, use_context=True)
dispatcher = updater.dispatcher
dp = updater.dispatcher




# greet
def greet(update:Update, context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='Welcome to News and weather bot')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='/news - Top 10 headlines')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='/weather - Get weather details')


# news
def news(update:Update, context:CallbackContext):
    url = f'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey={API_KEY.key_news}'
    news = requests.get(url).json()

    headlines = news["articles"]
    newslist1 = []
    for i in headlines:
        newslist1.append(i['title'])
    str1 = ''
    for j in range(len(newslist1)):
        str1 = str(j+1) + ': ' + newslist1[j]
        bot.send_message(chat_id=update.effective_chat.id, 
                        text=str1)
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='/news - Top 10 headlines')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='/weather - Get weather details')

# weather
def weatherD(update:Update, context:CallbackContext):
       
    user_input = update.message.text
    final_inp = user_input.capitalize()
    try:
                          
        obj=pyowm.OWM(API_KEY.key_weather)              
        mgr = obj.weather_manager()
        Weather=mgr.weather_at_place(final_inp) 
        Data=Weather.weather

        temp = Data.temperature('celsius')   
        # variables
        avg_temp = "Average Temp. Currently " + str(temp['temp'])
        max_temp = "Max Temp. Currently " + str(temp['temp_max'])
        min_temp = "Min Temp. Currently " + str(temp['temp_min'])
        
        humidity = Data.humidity  

        humid = "Humidity : " + str(humidity)
        
        cloud = Data.clouds 

        cloud_data = "Cloud Coverage Percentage : " + str(cloud)
        cloud_more = str(Data.status)
        cloud_type = str(Data.detailed_status)
        pressure = str(Data.pressure)
        

        #output
        bot.send_message(chat_id=update.effective_chat.id, text=avg_temp)
        bot.send_message(chat_id=update.effective_chat.id, text=min_temp)
        bot.send_message(chat_id=update.effective_chat.id, text=max_temp)
        bot.send_message(chat_id=update.effective_chat.id, text=humid)
        bot.send_message(chat_id=update.effective_chat.id, text=cloud_data)
        bot.send_message(chat_id=update.effective_chat.id, text=cloud_more)
        bot.send_message(chat_id=update.effective_chat.id, text=cloud_type)
        bot.send_message(chat_id=update.effective_chat.id, text=pressure)
        bot.send_message(chat_id=update.effective_chat.id, 
                        text='/news - Top 10 headlines')
        bot.send_message(chat_id=update.effective_chat.id, 
                        text='/weather - Get weather details')

    except Exception:
        bot.send_message(chat_id=update.effective_chat.id, 
                        text="City not found")
        bot.send_message(chat_id=update.effective_chat.id, 
                        text='/news - Top 10 headlines')
        bot.send_message(chat_id=update.effective_chat.id, 
                        text='/weather - Get weather details')

#user input
def input1(update:Update, context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id, 
                        text="Enter city name")
    dp.add_handler(MessageHandler(Filters.text, weatherD))
    





start = CommandHandler('start', greet.greet())
news = CommandHandler('news', news)
weather = CommandHandler('weather', input1)
updater.start_polling()
dispatcher.add_handler(start)
dispatcher.add_handler(news)
dispatcher.add_handler(weather)
updater.idle()

