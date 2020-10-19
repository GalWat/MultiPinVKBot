import command_system

def hello(*_):
   text = 'Привет!'
   return text

command = command_system.Command()

command.keys = ['привет']
command.description = 'приветствует вас'
command.process = hello