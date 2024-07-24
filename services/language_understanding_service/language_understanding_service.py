import requests
from logging_config import log
import json
from services.build_requests_headers import build_requests_headers


class LanguageUnderstandingService:
    """
    A service class for interacting with the Language Understanding Service API.
    """
    def __init__(self):
        self.language_service = "/LanguageService"

    def send_utterance_to_language_understanding_service(self, base_url, utterances):
        log.info("send_utterance_to_language_understanding_service")
        payload = json.dumps({"utterances": utterances}, indent=4)
        log.debug(f"Request payload: {payload}")
        request_headers = build_requests_headers()
        response = requests.post(f"{base_url}/{self.language_service}", headers=request_headers, data=payload)
        return response
