import handlers_system

def info(*_):
   text = ''
   for c in handlers_system.command_list:
        text += c.keys[0] + ' - ' + c.description + '\n'
   return text

command_handler = handlers_system.CommandHandler()

command_handler.keys = ['закреп помощь']
command_handler.desciption = 'Покажу список команд'
command_handler.process = info