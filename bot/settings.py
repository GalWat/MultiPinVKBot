import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get("TOKEN")
CONFIRM_TOKEN = os.environ.get("CONFIRM_TOKEN")
SENTRY_DSN = os.environ.get("SENTRY_DSN")
ENV = os.environ.get("FLASK_ENV")

RELEASE = "PinBot@0.1.0"
