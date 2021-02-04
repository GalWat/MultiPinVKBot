from .command_handler import CommandHandler


class HelpCommandHandler(CommandHandler):
    def __init__(self):
        super().__init__()

        self.keys = ['закреп помощь']
        self.description = 'Покажу список команд'

    # TODO: help command
    def process(self, data):
        text = ''
        # for c in base_handler.command_list:
        #     text += c.keys[0] + ' - ' + c.description + '\n'
        return text
