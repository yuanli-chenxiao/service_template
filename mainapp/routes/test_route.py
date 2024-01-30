from flask import Blueprint, current_app, jsonify, request

bp = Blueprint("test_route", __name__)


# 接口测试
@bp.route("/", methods=["GET"])
def route_test():
    current_app.else_logger.info("else route")
    current_app.logger.info("请求测试", extra={"request": request})


    return jsonify(msg="route test")

