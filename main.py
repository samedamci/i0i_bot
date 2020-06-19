#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import logging
import requests

import settings

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)
updater = None


def start(update, context):
    update.message.reply_text("""
Available commands:

/short <link>  -  shorten link
""")


def short(update, context):
    try:
        command = context.args[0].lower()
        shorten = requests.post("https://i0i.wtf", data={"url": command})
        update.message.reply_text(shorten.text)
    except IndexError:
        update.message.reply_text("You must give me URL as argument!")


def main():
    global updater
    updater = Updater(settings.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("short", short))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
