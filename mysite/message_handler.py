import os
import importlib

import monitoring

import vkapi
from handlers_system import command_list, event_list


def load_modules(module_type):
    files = os.listdir(f"mysite/{module_type}")
    modules = filter(lambda x: x.endswith(".py"), files)
    for m in modules:
        importlib.import_module(f"{module_type}.{m[0:-3]}")


@monitoring.transaction
def invoke_event(data):
    key = data["action"]["type"]
    text = ""
    for event in event_list:
        if key in event.keys:
            text = event.process(data)
    return text


@monitoring.transaction
def invoke_command(data):
    key = data["text"].lower()
    text = ""
    for command in command_list:
        if key in command.keys:
            text = command.process(data)
    return text


def respond(data):
    load_modules("commands")
    load_modules("events")

    peer_id = data["peer_id"]  # Идентификатор беседы, либо пользователя
    reply_to = data["id"]

    text = ""
    if data.get("action", False):
        text = invoke_event(data)
    else:
        text = invoke_command(data)

    if text:
        vkapi.send_message(text, peer_id, reply_to)
