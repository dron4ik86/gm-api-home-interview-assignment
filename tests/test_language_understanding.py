import pandas as pd
from services.mocks.simulate_api import simulate_api_response
from utils.utils import format_entities, calculate_similarity, calculate_pass_rate
from test_data.test_data import expected_intents_entities
from services.language_understanding_service.language_understanding_service import LanguageUnderstandingService
import config as cfg


def test_language_understanding(pass_criteria, utterances):
    results = []

    for utterance, expected in zip(utterances, expected_intents_entities):
        # response_data = LanguageUnderstandingService().send_utterance_to_language_understanding_service(
        #     cfg.BASE_URL, utterances)
        response_data = simulate_api_response(utterance)
        actual_intent = response_data['intent']
        actual_entities = response_data['entities']
        expected_intent = expected['intent']
        expected_entities = expected['entities']

        intent_similarity = calculate_similarity(actual_intent, expected_intent)
        entity_similarity = 'Similar'

        if actual_intent == "InvalidCommand":
            entity_similarity = 'Non-similar'
            intent_similarity = 'Non-similar'
        else:
            for entity_key, entity_value in expected_entities.items():
                if entity_key not in actual_entities or actual_entities[entity_key] != entity_value:
                    entity_similarity = 'Non-similar'
                    break

        results.append({
            'utterance': utterance,
            'api_intent': expected_intent,
            'actual_intent': actual_intent,
            'api_entity': format_entities(expected_entities),
            'actual_entity': format_entities(actual_entities),
            'intent_similarity': intent_similarity,
            'entity_similarity': entity_similarity
        })

    intent_pass_rate, entity_pass_rate, test_passed = calculate_pass_rate(results, pass_criteria)

    df = pd.DataFrame(results)
    file_name = 'language_understanding_test_results.xlsx'
    df.to_excel(file_name, index=False)

    assert test_passed, \
        f"Test failed with Intent Pass Rate: {intent_pass_rate:.2f}%, Entity Pass Rate: {entity_pass_rate:.2f}%"

