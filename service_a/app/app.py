from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, this is test Microservice A'

    return app