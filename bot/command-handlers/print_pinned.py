import handlers_system
import save_system

def print_pinned(data):
   peer_id = data['peer_id']
   messages = save_system.get_pinned(peer_id)

   template = ('_______________________\n'
               '>> Пин {0}\n'
               '>> от {1}\n'
               '{2}\n'
              )

   text = '\n'.join([template.format(i, val[0], val[1]) for i, val in enumerate(messages)])
   return text

command_handler = handlers_system.CommandHandler()

command_handler.keys = ['закреп список', 'закреп лист']
command_handler.description = 'вывод списка закрепленных сообщений'
command_handler.process = print_pinned