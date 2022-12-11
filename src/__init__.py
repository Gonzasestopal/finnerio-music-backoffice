import logging

from flask import Flask, request as req

from src.controllers import pages


def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.blueprint)

    app.logger.setLevel(logging.NOTSET)

    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    return app
