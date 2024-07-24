import pytest


def pytest_addoption(parser):
    """
    Adds custom command line options to pytest.
    """
    parser.addoption("--intent", action="store", default=50, type=int, help="Pass criteria for intent")
    parser.addoption("--entity", action="store", default=50, type=int, help="Pass criteria for entity")
    parser.addoption("--utterances", action="store", default="", type=str, help="Comma-separated list of utterances")


@pytest.fixture
def pass_criteria(request):
    """
    Pytest fixture to get pass criteria for intent and entity from command line options.
    """
    intent = request.config.getoption("--intent")
    entity = request.config.getoption("--entity")
    return {'intent': intent, 'entity': entity}


@pytest.fixture
def utterances(request):
    """
    Pytest fixture to get a list of utterances from command line options.
    """
    utterances_str = request.config.getoption("--utterances")
    if utterances_str:
        return [utterance.strip() for utterance in utterances_str.split(',')]
