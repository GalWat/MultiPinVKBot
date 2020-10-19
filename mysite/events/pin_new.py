import event_system
import save_system

def add_pin(data):
    save_system.add(data)
    text = f'Сообщение добавлено в список: {data["action"]["message"]}'
    return text

event = event_system.Event()

event.keys = ['chat_pin_message']
event.description = ''
event.process = add_pin