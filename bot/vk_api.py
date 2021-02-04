import vk
import random
import settings

session = vk.Session()
api = vk.API(session, v='5.110')


def send_message(message, peer_id, reply_to="", attachment=""):
    api.messages.send(
        access_token=settings.TOKEN,
        peer_id=str(peer_id),
        reply_to=reply_to,
        message=message,
        attachment=attachment,
        random_id=random.getrandbits(64)
    )


def get_messages_by_ids(peer_id, message_ids):
    response = api.messages.getByConversationMessageId(
        access_token=settings.TOKEN, 
        peer_id=peer_id, conversation_message_ids=message_ids
    )
    return response
