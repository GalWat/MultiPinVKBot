import importlib
import os

import sentry_decorators
import vk_api
# from handlers.base_handler import command_list, event_list


def load_modules(module_type):
    files = os.listdir(f"bot/{module_type}")
    modules = filter(lambda x: x.endswith(".py"), files)
    for m in modules:
        importlib.import_module(f"{module_type}.{m[0:-3]}")


@sentry_decorators.transaction
def invoke_event(data):
    key = data["action"]["type"]
    text = ""
    for event in event_list:
        if key in event.keys:
            text = event.process(data)
    return text


@sentry_decorators.transaction
def invoke_command(data):
    key = data["text"].lower()
    text = ""
    for command in command_list:
        if key in command.keys:
            text = command.process(data)
    return text


def respond_on(data: dict) -> bool:
    load_modules("command_handlers")
    load_modules("event_handlers")

    peer_id = data["peer_id"]  # Conversation or user id (depends on where message received)
    reply_to = data["id"]

    text = ""
    if data.get("action", False):
        text = invoke_event(data)
    else:
        text = invoke_command(data)

    if text:
        vk_api.send_message(text, peer_id, reply_to)
        return True
    return False
