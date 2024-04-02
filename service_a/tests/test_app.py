from flask_testing import TestCase
from app.app import create_app

class MyTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, this is test Microservice A')