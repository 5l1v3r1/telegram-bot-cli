#!/usr/bin/env python3

import telegram
from optparse import OptionParser
import config

def get_options():
    parser = OptionParser()
    parser.add_option("-j", "--job", dest="job", type="string", help="select a job name (required)")
    parser.add_option("-d", "--details", dest="details", type="string", help="add details to the job (50 characters max)")
    parser.add_option("-u", "--username", dest="username", type="string", help="add your username if you want the bot to highlight you")
    (options, args) = parser.parse_args()
    if not options.job:
        parser.error('Job name not given')
    elif options.details:
        if len(options.details) > 50:
            parser.error('Details too long')
    return options

if __name__ == "__main__":
    # Preparing script options
    options = get_options()
    # We need the telegram bot token and group id to send the message. I think this check can be done more gracefully.
    try:
        if config.BOT_TOKEN == "" or not config.BOT_TOKEN:
            print('Error: BOT_TOKEN is not set')
            quit()
        if config.BOT_TOKEN == "" or not config.GROUP_ID:
            print('Error: GROUP_ID is not set')
            quit()
    except:
        print('Error: parsing config file, BOT_TOKEN or GROUP_ID may be missing')
        quit()
    # Preparing bot
    bot = telegram.Bot(token=config.BOT_TOKEN)
    # Preparing simple message and adding details and/or username if needed
    message = "*[CLI Job]* the command-line job *" + options.job + "* has ended"
    if options.details:
        message += " (" + options.details + ")"
    if options.username:
        message += " for @" + options.username
    # Sending message
    bot.send_message(config.GROUP_ID, message, parse_mode=telegram.ParseMode.MARKDOWN)
