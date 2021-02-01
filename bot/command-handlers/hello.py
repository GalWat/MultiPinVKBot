import handlers_system


def hello(*_):
    text = "Привет!"
    return text


command_handler = handlers_system.CommandHandler()

command_handler.keys = ["привет"]
command_handler.description = "приветствует вас"
command_handler.process = hello
