import os
import json
import argparse

from dotenv import load_dotenv
from dialog_flow_utils import create_intent


def main():
    parser = argparse.ArgumentParser(
        description='Программа загружает вопросы и ответы и создает intent-ы для бота в DialogFlow'
    )
    parser.add_argument(
        'path',
        help='Путь к файлу с вопросами и ответами в формате *.json'
    )
    args = parser.parse_args()

    load_dotenv()
    project_id = os.environ.get('PROJECT_ID')
    with open(args.path, "r") as my_file:
        questions_json = my_file.read()

    questions = json.loads(questions_json)

    for intent_name in questions.keys():
        intent = questions[intent_name]
        create_intent(
            project_id,
            intent_name,
            intent['questions'],
            [intent['answer']],
        )


if __name__ == '__main__':
    main()
