import settings

import sentry_sdk
from flask import Flask, request, json
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    integrations=[FlaskIntegration()],
    traces_sample_rate=0.0,
    release=settings.RELEASE,
)

import message_handler


app = Flask(__name__)


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
        message_handler.respond(data['object']['message'])
        return 'ok'

    return 'Unsupported Media Type'