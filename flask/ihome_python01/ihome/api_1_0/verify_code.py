# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store, constants
from flask import current_app, jsonify, make_response
from ihome.utils.response_code import RET


# GET 127.0.0.1/api/v1.0/image_codes/<image_code_id>

@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证码
    :param image_code_id: 图片验证码编号
    :return: 正常：验证码图片 异常：返回json
    """
    # 业务逻辑处理
    # 生成验证码图片
    # 名字，真是文本，图片数据
    name, text, image_data = captcha.generate_captcha()

    # 将验证码真实值与编号保存到redis中，设置有效期
    # redis： 字符串 列表 哈希 set(集合)
    # "key"：xxx
    # image_codes:{"id1":"", "id2":""} 哈希 hset()
    #redis_store.set("image_code_%s" % image_code_id, text)
    #redis_store.expire("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
    #                                   id              有效期                             记录：
    try:
        redis_store.setex("image_code_%s" %image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        # 记录日志
        current_app.logger.error(e)
        # return jsonify(errno=RET.DATAERR, errmsg="save image code id failed")
        return jsonify(errno=RET.DATAERR, errmsg="保存图片验证码失败")

    # 返回图片
    resp = make_response(image_data)
    resp.headers["Content-type"] = "image/jpg"
    return resp


