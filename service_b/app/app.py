from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def get_message():
        service_a_message = 'Hello, this is test Microservice A'
        return f'Message from service A: {service_a_message}, relayed from service B!'

    return app