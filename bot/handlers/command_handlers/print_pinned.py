from .command_handler import CommandHandler
import save_system


class PrintPinnedHandler(CommandHandler):
    def __init__(self):
        super().__init__()

        self.keys = ['закреп список', 'закреп лист']
        self.description = 'вывод списка закрепленных сообщений'

    def print_pinned(self, data):
        peer_id = data['peer_id']
        messages = save_system.get_pinned(peer_id)

        template = '''_______________________\n
                   >> Пин {0}\n
                   >> от {1}\n
                   {2}\n
                   '''

        text = '\n'.join([template.format(i, val[0], val[1]) for i, val in enumerate(messages)])
        return text
