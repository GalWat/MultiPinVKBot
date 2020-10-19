import command_system
import save_system

def print_pinned(data):
   peer_id = data['peer_id']
   messages = save_system.get_list(peer_id)

   template = ('_______________________\n'
               '>> Пин {0}\n'
               '>> от {1}\n'
               '{2}\n'
              )

   text = '\n'.join([template.format(i, val[0], val[1]) for i, val in enumerate(messages)])
   return text

command = command_system.Command()

command.keys = ['закреп список', 'закреп лист']
command.description = 'вывод списка закрепленных сообщений'
command.process = print_pinned