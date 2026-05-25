import uuid
import requests


AUTH_KEY = "MDE5ZTU0ZjYtZmMwZC03NzZiLTg2MzctYzAwNWY5NmNiNjJkOmIxOTJkZTczLWJhNGMtNGMzOS1iMWQ5LWExMTA2NGY1MTMyNQ=="


def get_access_token():

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
        verify=False
    )

    print("TOKEN RESPONSE:")
    print(response.status_code)
    print(response.text)

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
        verify=False
    )

    print("CHAT RESPONSE:")
    print(response.status_code)
    print(response.text)

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]