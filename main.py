#!/usr/bin/python
# -*- coding: utf-8 -*-
from textblob import TextBlob

from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters
import requests
import re
# import pycountry

def translate(last_message):
    try:
        blob=TextBlob(str(last_message))
        tranlated_text=str(blob.translate(to='am'))
        print(tranlated_text)
         
    except Exception as e:
        print("unable to translate", e)
        return "Unable to detect "
    else:
        return tranlated_text

def sender(bot, update):
    try:
        response=""
        # url = get_url()
        last_message=str(update.message.text)
        print(last_message)
        
        # iso_code=blob.detect_language()
        # language = pycountry.languages.get(alpha_2=iso_code).name

        retruned_text=translate(last_message)
        response=retruned_text
        # if retruned_text:
        #     response="unable to detect"
        # else:
        #     response=retruned_text
    #      return response
        chat_id = update.message.chat_id
        username=update.message.from_user.username
        date=update.message.date
        bot.send_message(chat_id=chat_id, text=response)
        print(response)
    except Exception as e:
        print(e)
def main():
    updater = Updater('TOKEN')
    dp = updater.dispatcher
    echo_handler = MessageHandler(Filters.text, sender)
    dp.add_handler(echo_handler)
    # dp.add_handler(MessageHandler('bop',bop))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
