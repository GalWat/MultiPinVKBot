import datetime

import vkapi

pinned_messages = {}


def add(
    data,
):  # Silence global statement issue (will be fixed in future) skipcq: PYL-W0603
    global pinned_messages
    peer_id = data["peer_id"]
    pinned_messages.setdefault(peer_id, [])
    message = vkapi.get_messages_by_ids(
        peer_id, data["action"]["conversation_message_id"]
    )["items"][0]
    date = datetime.datetime.fromtimestamp(message["date"])
    pinned_messages[peer_id].append((date.strftime("%Y-%m-%d %H:%M"), message["text"]))


def remove(data):  # Silence unused variable issue: skipcq: PYL-W0613
    pass


def get_pinned(peer_id):
    return pinned_messages.get(peer_id, [])


# read_from_file()
