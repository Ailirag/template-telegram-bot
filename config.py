import os

basedir = os.path.abspath(os.path.dirname(__file__))
serverfile = os.path.join(basedir, 'thisserver')

class Config(object):
    def __init__(self):
        self.TOKEN = 'BOT_TOKEN'
        self.DATABASE_URI = os.path.join(basedir, 'app.db')
        self.DOWNLOAD_FOLDER = os.path.join(basedir, 'downloads/')
        self.TEMP_FOLDER = os.path.join(basedir, 'tmp/')
        self.IP = 'VPS_IP'
        self.PORT = 'PORT'
        self.IP_PORT = f'{self.IP}:{self.PORT}'
        self.PATH_TO_CERT = './webhook_cert.pem' #os.path.join(basedir, 'cert/example.pem')
        self.PATH_TO_PKEY = './webhook_pkey.pem' #os.path.join(basedir, 'cert/example.key')
        self.ADMIN = 'TG_NAME'
        self.SECRET_KEY = 'FOR_FLASK_APP'
        self.WEBHOOK_URL_PATH = "/%s/" % (self.TOKEN)
        self.THIS_IS_SERVER = os.path.exists(serverfile)

# Quick'n'dirty SSL certificate generation:
#
# openssl genrsa -out webhook_pkey.pem 2048
# openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in IP
