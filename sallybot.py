import bot
import os
 
sallybot = bot.Bot(token = os.environ.get(my_token))
sallybot.listen()