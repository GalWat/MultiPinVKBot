import command_system

def info(*_):
   text = ''
   for c in command_system.command_list:
        text += c.keys[0] + ' - ' + c.description + '\n'
   return text

command = command_system.Command()

command.keys = ['Закреп помощь']
command.desciption = 'Покажу список команд'
command.process = info