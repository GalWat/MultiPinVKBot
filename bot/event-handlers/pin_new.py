import handlers_system
import save_system

def add_pin(data):
    save_system.add(data)
    text = f'Сообщение добавлено в список: {data["action"]["message"]}'
    return text

event_handler = handlers_system.EventHandler()

event_handler.keys = ['chat_pin_message']
event_handler.description = ''
event_handler.process = add_pin