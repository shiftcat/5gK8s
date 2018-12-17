
import os

class Config():
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class ConfigForMySql():
    SQLALCHEMY_DATABASE_URI = \
        "mysql+pymysql://{}:{}@{}:{}/{}".format(
            os.getenv('DATABASE_USER'),  os.getenv('DATABASE_PASSWD'),
            os.getenv('DATABASE_SERVER'), os.getenv('DATABASE_PORT'), os.getenv('DATABASE_NAME'))


class ConfigForDev(Config, ConfigForMySql):
    SQLALCHEMY_ECHO = True


