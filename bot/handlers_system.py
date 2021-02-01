command_list = []
event_list = []


class Handler:
    def __init__(self):
        self.__keys = []
        self.description = ''

    @property
    def keys(self):
        return self.__keys
    
    @keys.setter
    def keys(self, mas):
        for key in mas:
            self.__keys.append(key.lower())

    def process(self, data):
        pass


class CommandHandler(Handler):
    def __init__(self):
        super().__init__()
        command_list.append(self)


class EventHandler(Handler):
    def __init__(self):
        super().__init__()
        event_list.append(self)