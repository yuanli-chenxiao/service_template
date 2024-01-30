import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LEVEL(object):
    REQUEST = 24
    RESPONSE = 26

    level_to_name = {
        REQUEST: "REQUEST",
        RESPONSE: "RESPONSE"
    }


LOGGER_CONFIG = {
    "version": 1,
    "disable_existing_logger": False,
    "formatters": {
        # 主 logger
        "simple": {
            "class": "utils.logger_handler.MessageFormatter",
            "format": "{asctime} - {lineno} - {message}",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{"
        },
        # 主 logger 模板
        "complete": {
            "class": "utils.logger_handler.MessageFormatter",
            "format": "-----------------------------------------------------\n"
                      "datetime: {asctime}\n"
                      "level: {levelname}\n"
                      "path: {filename} - {lineno}\n"
                      "sn: [sn]\n"
                      "ip: [ip]\n"
                      "path: [path]\n"
                      "content: {message}\n"
                      "-----------------------------------------------------\n",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{"
        },
        # 其它 logger 定义（后期需要自定义按照此格式）
        "else_logger": {
            "class": "utils.logger_handler.MessageFormatter",
            "format": "{asctime} - {lineno} - {message}",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{"
        },
        # 其它 logger 模板
        "else_logger_complete": {
            "class": "utils.logger_handler.MessageFormatter",
            "format": "-----------------------------------------------------\n"
                      "datetime: {asctime}\n"
                      "level: {levelname}\n"
                      "path: {filename} - {lineno}\n"
                      "content: {message}\n"
                      "-----------------------------------------------------\n",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{"
        }
    },
    "filters": {
        "only_debug_filter": {
            "()": "utils.logger_handler.OnlyDebugFilter",
        },
        "info_filter": {
            "()": "utils.logger_handler.InfoFilter",
        },
        "else_logger_filter": {
            "()": "utils.logger_handler.InfoFilter",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filters": ["only_debug_filter", ]
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "complete",
            "filename": f"{BASE_DIR}/logs/server.log",
            "when": "MIDNIGHT",
            "interval": 1,
            "encoding": "utf8",
            "backupCount": 30,
            "filters": ["info_filter", ]
        },
        "else_logger_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "else_logger_complete",
            "filename": f"{BASE_DIR}/logs/else_server.log",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 2,
            "encoding": "utf8",
            "filters": ["info_filter", ]
        },
    },
    "loggers": {
        "debug_logger": {
            "handlers": ["console", ],
            "level": "DEBUG"
        },
        "info_logger": {
            "handlers": ["file", ],
            "level": "DEBUG"
        },
        "else_logger": {
            "handlers": ["else_logger_file", ],
            "level": "INFO"
        }
    }
}


# 系统业务配置
APP_SETTINGS = {
    "is_debug": True,
    "logger_config": LOGGER_CONFIG
}
