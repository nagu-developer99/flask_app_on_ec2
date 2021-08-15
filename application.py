from flask import Flask
from flask_restx import Resource, Api
import socket

app = Flask(__name__)
api = Api(app)

@api.route('/get_hostname')
class HelloWorld(Resource):
    def get(self):
        return {'executed_from': f'{socket.gethostbyname(socket.gethostname())}'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
