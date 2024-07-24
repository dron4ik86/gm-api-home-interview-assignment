def format_entities(entities):
    """
    Formats the entities into a readable string. If no entities are provided, returns "Invalid command".
    """
    if not entities:
        return "Invalid command"
    return ", ".join(f"{key}={value}" for key, value in entities.items())


def calculate_similarity(actual, expected):
    """
    Compares the actual and expected values to determine similarity.
    """
    return 'Similar' if actual == expected else 'Non-similar'


def calculate_pass_rate(results, criteria):
    """
    Calculates the pass rate for intents and entities based on the criteria.
    """
    similar_intents = sum(1 for result in results if result['intent_similarity'] == 'Similar')
    similar_entities = sum(1 for result in results if result['entity_similarity'] == 'Similar')

    total_utterances = len(results)
    intent_pass_rate = (similar_intents / total_utterances) * 100
    entity_pass_rate = (similar_entities / total_utterances) * 100

    test_passed = intent_pass_rate >= criteria['intent'] and entity_pass_rate >= criteria['entity']

    print(f"\nIntent Pass Rate: {intent_pass_rate:.2f}%")
    print(f"Entity Pass Rate: {entity_pass_rate:.2f}%")
    print(f"Test {'Passed' if test_passed else 'Failed'}")

    return intent_pass_rate, entity_pass_rate, test_passed
