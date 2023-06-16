import os
import json

from google.cloud import dialogflow
from dotenv import load_dotenv


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part
        )
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


def detect_intent_texts(project_id, session_id, texts, language_code='ru'):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(
            text=text,
            language_code=language_code
        )

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        return response.query_result.fulfillment_text


def load_questions(project_id, path):
    with open(path, "r") as my_file:
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