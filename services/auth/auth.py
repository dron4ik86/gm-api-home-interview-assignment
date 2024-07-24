import json
import config as cfg
from logging_config import log
import requests


class Auth:
    def __init__(self, user_name, password):
        self.auth_url = f"{cfg.IDS_URL}/connect/token"
        self.user_name = user_name
        self.password = password

    def auth(self):
        """
        Fixture for logging in as a specified user, which yields an access token.
        """
        log.info("access_token")
        request_headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json"
        }

        payload = {
            "grant_type": "password",
            "username": self.user_name,
            "password": self.password,
        }

        pretty_json_string = json.dumps(payload, indent=4)
        log.debug(f"Request payload: {pretty_json_string}")
        response = requests.post(self.auth_url, headers=request_headers, data=payload)
        access_token = response.json()["access_token"]
        return access_token



