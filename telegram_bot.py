# Import necessary classes from the telegram.ext module
from telegram.ext import Updater, CommandHandler

# Replace the following token with your own bot token
Token = "6617675762:AAE793t-0Z3PSPfIvddYuixgHiJoH5h7eJY"

# Create an Updater object with the provided token and enable context support
updater = Updater(token=Token, use_context=True)
# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Command handler function for /start command
def start(update, context):
    update.message.reply_text("Hello! Welcome to my bot!")

# Command handler function for /help command
def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This particular message
        /content -> About various playlists of Simplilearn
        /Python -> The first video from Python playlist
        /SQL -> The first video from SQL playlist
        /Java -> The first video from Java playlist
        /contact -> contact info
        """
    )

# Command handler function for /content command
def content(update, context):
    update.message.reply_text("We have various playlists and articles available")

# Command handler function for /Python command
def Python(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=_xQNeOTRyig")

# Command handler function for /SQL command
def SQL(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=pFq1pgli0OQ")

# Command handler function for /Java command
def Java(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=i6AZdFxTK9I")

# Command handler function for /contact command
def contact(update, context):
    update.message.reply_text("You can contact on the registered mail id provided on the website")

# Register the command handlers with the dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('Python', Python))
dispatcher.add_handler(CommandHandler('SQL', SQL))
dispatcher.add_handler(CommandHandler('Java', Java))
dispatcher.add_handler(CommandHandler('contact', contact))
dispatcher.add_handler(CommandHandler('help', help))

# Start the Bot and continuously polling for updates
updater.start_polling()
# Keep the program running until the user presses Ctrl+C (interrupts the program)
updater.idle()