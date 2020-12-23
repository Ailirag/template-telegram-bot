from bot import app, config, mybot, db
from bot import Users, Properties 
import flask, telebot


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return {'result': 'its work!'}

@app.route(config.WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        mybot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

@mybot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    mybot.reply_to(message,
                 ("Hi there, I am EchoBot mybot.\n"
                  "I am here to echo your kind words back to you."))

# Handle all other messages
@mybot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def commandCenter(message):

    #check user in databese or admin
    mybot.reply_to(message, message.__getattribute__(message.content_type))