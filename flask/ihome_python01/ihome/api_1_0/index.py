# coding:utf-8

from . import api
#from ihome import db, models
# import logging
from flask import current_app

@api.route("/index")
def index():
    # logging.error("xxx")    # 错误级别
    # logging.warning("")     # 警告级别
    # logging.info("")     # 消息提示级别
    # logging.debug()     # 调试级别
    current_app.logger.error("error info")
    current_app.logger.warn("warn info")
    current_app.logger.info("info info")
    current_app.logger.debug("debug info")

    return "index page"
