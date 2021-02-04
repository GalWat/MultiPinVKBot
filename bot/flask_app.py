from flask import Flask, request, json

import sentry_init

import settings
import vk_events_responder


app = Flask(__name__)


@app.route('/debug-sentry')
def raise_error():
    1 / 0


@app.route('/')
def website_access():
    return 'This is a VK bot, not website.'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'not vk'

    if data['type'] == 'confirmation':
        return settings.CONFIRM_TOKEN
    if data['type'] == 'message_new':
        return 'ok' if vk_events_responder.respond_on(data['object']['message']) else 'error'

    return 'Unsupported Media Type'
