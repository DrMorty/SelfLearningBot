#! /usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

updater = Updater(token='608604606:AAFvstqF0Lvn4jXbOZG-UnzSmhFyFbXaxkI')
dispatcher = updater.dispatcher

def startCommand(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Привет! Давай общаться')

def textMessage(bot, update):#посылаем сообщение на серевер Dialogflow
    request = apiai.ApiAI('1cb0776afa8f446bb63bc409262a05c3').text_request()
    request.lang = 'ru' 
    request.session_id = 'SelfLearningBot'
    request.query = update.message.text 
    request.query = update.message.text 
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] 
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не до конца понял :(')

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()   
