from flask import Flask
from config import Config
import telebot
import peewee

config = Config()

db = peewee.SqliteDatabase(config.DATABASE_URI)

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['DEBUG'] = True

from bot.models import *
from bot.service import mybot
import bot.routes



#from app.mylib import smartDict as sDict