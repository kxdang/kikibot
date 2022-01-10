
import logging
import secret
import telegram
import schedule
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

chat_id = secret.chat_id
token = secret.token
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

bot = telegram.Bot(token=token)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Kikibot is at your service.')


def humidifier_reminder():
    bot.sendMessage(
        chat_id=chat_id, text='Yo refill your humidifier and switch the filter around')


def humidifier_cleaner_reminder():
    bot.sendMessage(
        chat_id=chat_id, text="Clean your humidifier. It's been a week")


def do_laundry_reminder():
    bot.sendMessage(
        chat_id=chat_id, text='Do laundry pls')

def vitamin_d():
    bot.sendMessage(
        chat_id=chat_id, text='Take Vitamin D')

def husk():
    bot.sendMessage(
        chat_id=chat_id, text='Take psyllium husk')

def feedCats():
    bot.sendMessage(
        chat_id=chat_id, text='Feeding time for Mushu and Minou')

def scheduled_message():
    schedule.every().day.at("09:00").do(feedCats)
    schedule.every().day.at("21:00").do(feedCats)
    schedule.every().day.at("09:30").do(vitamin_d)
    schedule.every().saturday.at("10:30").do(do_laundry_reminder)

    while True:
        schedule.run_pending()
        time.sleep(1)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def id_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.chat_id)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('Noted')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("id", id_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    scheduled_message()
    bot.sendMessage(chat_id=chat_id, text='Kikibot Booted')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
