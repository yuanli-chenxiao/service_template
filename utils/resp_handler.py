import random
from datetime import datetime

from flask import request, current_app

from config.default_config import LEVEL


def before_request_hooks(app):
    
    @app.before_request
    def write_logs():
        date_time_str = datetime.now().strftime("%Y%m%d%H%M%S").__str__()
        random_str = "".join([chr(i) for i in random.choice([i for i in range(65, 91)], k=3)])
        request.sn = f"CUS{date_time_str}{random_str}"

        current_app.logger.log(LEVEL.REQUEST, request.get_data(), extra={"request": request})


def after_request_hooks(app):

    @app.after_request
    def after_app_request(response):
        response_data = response.get_json()

        current_app.logger.log(LEVEL.RESPONSE, response_data, extra={"request": request})
        return response
    
