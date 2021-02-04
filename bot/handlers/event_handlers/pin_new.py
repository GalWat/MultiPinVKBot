from .event_handler import EventHandler
import save_system


class PinNewHandler(EventHandler):
    def __init__(self):
        super().__init__()

        self.keys = ['chat_pin_message']
        self.description = ''

    def add_pin(self, data):
        save_system.add(data)
        text = f'Сообщение добавлено в список: {data["action"]["message"]}'
        return text
