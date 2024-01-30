import json
import logging
from logging import LogRecord
import logging.config
import traceback

from utils.shared import AppContext


class MessageFormatter(logging.Formatter):

    def formatMessage(self, record: LogRecord) -> str:
        is_inner_exception = False

        try:
            if isinstance(record.msg, (list, dict)):
                record.message = json.dumps(record.msg)

            elif isinstance(record.msg, Exception):
                is_inner_exception = True
                raise record.msg
            
            else:
                record.message = str(record.msg)

        except Exception:
            if is_inner_exception:
                record.message = traceback.format_exc(limit=3)

            else:
                record.message = str(record.msg)

        return self._style.format(record)
    
    def format(self, record):
        s = super().format(record)

        if hasattr(record, "request"):
            s = s.replace("[sn]", record.request.sn).replace("[ip]", record.request.remote_addr).replace("[path]", record.request.path)

        else:
            s = s.replace("[sn]", "").replace("[ip]", "").replace("[path]", "")

        return s
    

class OnlyDebugFilter(logging.Filter):

    def filter(self, record: LogRecord) -> bool:
        
        if logging.DEBUG == record.levelno:
            return super().filter(record)

        else:
            return 0
        

class InfoFilter(logging.Filter):

    def filter(self, record: LogRecord) -> bool:
        
        if AppContext.app_settings().get("is_debug"):
            if logging.DEBUG <= record.levelno:
                return super().filter(record)
            
        else:
            if logging.INFO <= record.levelno:
                return super().filter(record)
            else:
                return 0
