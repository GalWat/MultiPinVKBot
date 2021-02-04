from .command_handler import CommandHandler


class HelloCommandHandler(CommandHandler):

    def __init__(self):
        super().__init__()

        self.keys = ['привет']
        self.description = 'приветствует вас'

    def process(self, _):
        return 'Привет!'
