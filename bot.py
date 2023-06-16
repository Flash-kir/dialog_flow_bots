import os
import random
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from dialog_flow_utils import detect_intent_texts


def echo(event, vk_api):
    message_text = [event.text]
    answer_text = detect_intent_texts(
                        os.environ.get('PROJECT_ID'),
                        event.user_id,
                        message_text
    )
    if answer_text:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer_text,
            random_id=random.randint(1, 1000)
        )


def main():
    load_dotenv()
    vk_session = vk.VkApi(token=os.environ.get('VK_GROUP_TOKEN'))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)


if __name__ == '__main__':
    main()
