def simulate_api_response(utterance):
    """
    Simulates the response from an API for given utterances.
    Return the mock response for the given utterance or a default response if not found.
    """
    mock_responses = {
        "Set temperature to 25 degrees": {"intent": "SetTemperature", "entities": {"temperature": 25}},
        "Increase temperature": {"intent": "IncreaseTemperature", "entities": {"action": "decrease"}},
    }
    return mock_responses.get(utterance, {"intent": "InvalidCommand", "entities": {}})

