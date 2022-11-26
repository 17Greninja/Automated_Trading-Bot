from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from bob_telegram_tools.bot import TelegramBot
import matplotlib.pyplot as plt

updater = Updater("5765859800:AAFoxAOAIlU3rt5oaiWvb7UN8aNH_6dcBhA",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hi guys. Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/see_logs - To see the last 100 actions
	/get_graph_of_stock - To get graph of a given stock
	/get_currentPrice_of_stock - To get current price of some stock
	/get_portfolio - To get the details of current investments""")


def see_logs(update: Update, context: CallbackContext):
	update.message.reply_text(
		"do stuff")


def get_graph_of_stock(update: Update, context: CallbackContext):
	update.message.reply_text("Enter stock name")
	# user_input = update.message.text
	# token = '5765859800:AAFoxAOAIlU3rt5oaiWvb7UN8aNH_6dcBhA'
	# user_id = int('1744336909')
	# bot = TelegramBot(token, user_id)
	# plt.plot([1, 2, 3, 4])
	# plt.ylabel('some numbers')
	# bot.send_plot(plt)
	# # This method delete the generetad image
	# bot.clean_tmp_dir()


def get_currentPrice_of_stock(update: Update, context: CallbackContext):
	update.message.reply_text("Enter stock name")
	# user_input = update.message.text
	# update.message.reply_text("do stuff")


def get_portfolio(update: Update, context: CallbackContext):
	update.message.reply_text("do stuff")

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('see_logs',see_logs ))
updater.dispatcher.add_handler(CommandHandler('get_graph_of_stock', get_graph_of_stock))
updater.dispatcher.add_handler(CommandHandler('get_currentPrice_of_stock', get_currentPrice_of_stock))
updater.dispatcher.add_handler(CommandHandler('get_portfolio', get_portfolio))
# we need to use regexes to match stock names, we can start the stock names with # or something
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
