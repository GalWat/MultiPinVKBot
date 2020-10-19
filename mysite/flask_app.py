import message_handler
import settings

from flask import Flask, request, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return settings.confirmation_token
    elif data['type'] == 'message_new':
        message_handler.respond(data['object']['message'])
        return 'ok'