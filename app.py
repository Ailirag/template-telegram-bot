from bot import app, mybot, config

if __name__=='__main__':
    if config.THIS_IS_SERVER:
        app.run(host='0.0.0.0', port=config.PORT, ssl_context=(config.PATH_TO_CERT,config.PATH_TO_PKEY))
    else:
        mybot.polling(none_stop=True, interval=5)