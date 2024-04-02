from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_message():
    service_a_message = 'Hello, this is test Microservice A'
    return f'Message from service A:{service_a_message}, relayed from service B!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)