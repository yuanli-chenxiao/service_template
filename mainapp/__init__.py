
import datetime
import logging.config
from json import JSONEncoder

from flask import Flask

from config.default_config import LEVEL
from mainapp import routes

from utils import shared
from utils.resp_handler import before_request_hooks, after_request_hooks


class CustomJSONEncoder(JSONEncoder):
    """ 自定义全局 json 格式化 """

    def default(self, obj):
        try:
            if isinstance(obj, datetime.datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def init_logger(app):
    logging.config.dictConfig(shared.AppContext.app_settings().get("logger_config"))

    for level, name in LEVEL.level_to_name.items():
        logging.addLevelName(level, name)

    # logger 定义
    logger = logging.getLogger("info_logger")
    else_logger = logging.getLogger("else_logger")

    # logger 注册到 app
    app.logger = logger 
    app.else_logger = else_logger


def create_app(conf_file=None):
    flask_app = Flask(__name__)
    flask_app.json_encoder = CustomJSONEncoder
    
    if conf_file:
        flask_app.config.from_pyfile(conf_file)

    app_settings = shared.AppSettings(flask_app.config["APP_SETTINGS"])
    shared.AppContext.app_settings(app_settings)

    # 请求钩子注册
    before_request_hooks(flask_app)
    after_request_hooks(flask_app)

    # 日志注册
    init_logger(flask_app)

    # api 注册
    routes.init(flask_app)

    return flask_app
