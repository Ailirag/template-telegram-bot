from bot import db
import peewee

class Users(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField()
    admin = peewee.BooleanField()
    chatid = peewee.CharField()

    class Meta:
        database = db


class Properties(peewee.Model):
    name = peewee.CharField()
    value = peewee.CharField()

    class Meta:
        database = db


class NonActiveKey(peewee.Model):
    id = peewee.PrimaryKeyField()
    secret_key = peewee.CharField()
    date_generation = peewee.DateField()
    user_gen = peewee.CharField()

    class Meta:
        database = db


class StorageKeys(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField()
    name_telegram = peewee.CharField()
    secret_key = peewee.CharField()
    name_pc = peewee.CharField()
    api_key = peewee.CharField()
    active = peewee.BooleanField()

    class Meta:
        database = db


class CommandsToDo(peewee.Model):
    id = peewee.PrimaryKeyField()
    name_telegram = peewee.CharField()
    command = peewee.CharField()
    args = peewee.CharField()

    class Meta:
        database = db


Users.create_table()
Properties.create_table()
NonActiveKey.create_table()
StorageKeys.create_table()
CommandsToDo.create_table()