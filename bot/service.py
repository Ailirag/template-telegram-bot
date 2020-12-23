from bot import config
import time
from telebot import TeleBot

mybot = TeleBot(config.TOKEN)

def activateWebhook():

    mybot.remove_webhook()
    time.sleep(2)
    url = f'https://{config.IP_PORT}'
    mybot.set_webhook(url=url + config.WEBHOOK_URL_PATH,
                certificate=open(config.PATH_TO_CERT, 'r'))

if config.THIS_IS_SERVER:
    activateWebhook()
else:
    mybot.remove_webhook()