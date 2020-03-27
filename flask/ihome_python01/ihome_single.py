# coding:utf-8

from flask import flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)

class Config(object):
    """配置信息"""
    DEBUG = True

    SECRER_KEY = "wangxx**wjkskf0923nn"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python01"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_POST = 6379

app.config.from_object(Config)

# 数据库
db = SQLAlchemy(app)

# redis
redis_store = redis.S



@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    app.run()