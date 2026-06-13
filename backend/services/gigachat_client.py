import os
import uuid

import requests


AUTH_KEY = os.getenv(
    "GIGACHAT_AUTH_KEY",
    ""
)

VERIFY_SSL = os.getenv(
    "GIGACHAT_VERIFY_SSL",
    "True"
) == "True"


def get_access_token():

    if not AUTH_KEY:
        raise ValueError("GIGACHAT_AUTH_KEY is not set")

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    headers = {
        "Authorization": f"Basic {AUTH_KEY}",
        "RqUID": str(uuid.uuid4()),
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "scope": "GIGACHAT_API_PERS"
    }

    response = requests.post(
        url,
        headers=headers,
        data=payload,
        verify=VERIFY_SSL,
        timeout=30
    )

    response.raise_for_status()

    return response.json()["access_token"]


def request_gigachat(prompt):

    access_token = get_access_token()

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        verify=VERIFY_SSL,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]
