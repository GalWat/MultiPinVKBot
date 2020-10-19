import json
import datetime

import vkapi

pinned_messages = {}


def add(data):
    global pinned_messages
    peer_id = data['peer_id']
    pinned_messages.setdefault(peer_id, [])
    message = vkapi.get_messages_by_ids(
                peer_id, 
                data['action']['conversation_message_id']
            )['items'][0]
    date = datetime.datetime.fromtimestamp(message['date'])
    pinned_messages[peer_id].append( (date.strftime('%Y-%m-%d %H:%M'), message['text']) )
    # write_to_file()


def remove(data):
    pass


def get_list(peer_id):
    return pinned_messages[peer_id]



# read_from_file()